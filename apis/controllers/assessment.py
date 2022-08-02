from apis.models import User, Assessment, AssessmentPerformance, Question, QuestionPerformance
from apis.serializers.user import UserSerializer
from apis.serializers.assessment import AssessmentSerializer, QuestionSerializer, BasicQuestionPerformanceSerializer, BasicAssessmentPerformanceSerializer
from apis.helpers.utility import prepare_response
from apis.helpers.exceptions import BadRequest, Forbidden, NotFound
from django.db import transaction
from django.db import models

def list_assessments(filters, user):
    page = filters.get('page', 1)
    size = filters.get('size', 10)
    limit = int(size)
    offset = (int(page)-1)*limit

    level = filters.get('level')
    category = filters.get('category')

    assessments = Assessment.objects.filter(is_deleted=False)
    if level:
        assessments = assessments.filter(level=level)

    if category:
        assessments = assessments.filter(category=category)

    assessments = assessments.order_by('-created_on')[offset:offset+limit]

    resp = AssessmentSerializer(assessments, many=True).data

    return prepare_response(resp)

def get_assessment(assessment_id, user):
    assessment = Assessment.objects.filter(id=assessment_id, is_deleted=False).first()
    questions = Question.objects.filter(assessment=assessment, is_deleted=False)
    resp = AssessmentSerializer(assessment).data
    resp['questions'] = QuestionSerializer(questions, many=True).data
    return prepare_response(resp)

@transaction.atomic
def save_performance(data, user):
    assessment_id = data['assessment']
    assessment = Assessment.objects.get(id=assessment_id)
    a_performance = AssessmentPerformance.objects.create(
        user = user,
        assessment = assessment
    )
    q_ids = [entry['question'] for entry in data['performances']]
    questions = Question.objects.filter(id__in=q_ids)
    q_map = {}
    for q in questions:
        q_map[str(q.id)] = q
   
    performances = []
    for entry in data['performances']:
        question = q_map[str(entry['question'])]
        performance = QuestionPerformance()
        performance.user = user
        performance.question = question
        performance.assessment_performance = a_performance
        performance.score = question.weightage

        for choice in entry['choices']:
            if choice not in question.correct_choices:
                performance.score = 0
                break

        performances.append(performance)


    ps = QuestionPerformance.objects.bulk_create(performances)

    return 

def _prepare_report(performances):
    weightage = 0
    total_score = 0
    strengths = []
    weaknesses = []
    study_plan = []

    for p in performances:
        weightage += p.question.weightage
        total_score += p.score or 0
        if p.score:
            strengths.extend(p.question.strengths_required or [])
        else:
            weaknesses.extend(p.question.strengths_required or [])
            if p.question.study_plan:
                study_plan.append(p.question.study_plan)
    resp = {}
    resp['weightage'] = weightage
    resp['score'] = total_score
    resp['strengths'] = strengths
    resp['weaknesses'] = weaknesses
    resp['study_plan'] = study_plan

    return resp

def find_performance(filters, user):
    assessment_id = filters.get('assessment')
    level = filters.get('level')
    category = filters.get('category')

    a_performance = AssessmentPerformance.objects.filter(user=user, is_deleted=False)
    if assessment_id:
        a_performance = a_performance.filter(assessment__id=assessment_id)
    if level:
        a_performance = a_performance.filter(assessment__level=level)
    if category:
        a_performance = a_performance.filter(assessment__category=category)

    try:
        a_performance = a_performance.latest('created_on')
    except AssessmentPerformance.DoesNotExist as ne:
        raise NotFound()

    resp = None
    if not a_performance.report:
        performances = QuestionPerformance.objects.filter(user=user, assessment_performance=a_performance, is_deleted=False)
        report = _prepare_report(performances)
        a_performance.report = report
        a_performance.save()

    resp = BasicAssessmentPerformanceSerializer(a_performance).data
    return prepare_response(resp)
