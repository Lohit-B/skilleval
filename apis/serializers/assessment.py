from rest_framework import serializers
from apis.serializers.user import UserSerializer, GradeSerializer
from apis.models import Assessment, QuestionPerformance, Question, AssessmentPerformance
from apis.models.assessment import ASSESSMENT_CATEGORY

class AssessmentSerializer(serializers.ModelSerializer):
    grade = GradeSerializer()
    category_title = serializers.SerializerMethodField()

    def get_category_title(self, assessment):
        for tpl in ASSESSMENT_CATEGORY:
            if tpl[0] == assessment.category:
                return tpl[1]

    class Meta:
        model= Assessment
        fields=["id", 'level', "category_title", "category", 'grade', 'weightage']

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model= Question
        fields=["id", 'strengths_required', "study_plan", 'content', 'choices', 'correct_choices', 'weightage', 'is_multiple_choice']

class BasicQuestionPerformanceSerializer(serializers.ModelSerializer):
    #question = QuestionSerializer()
    #user = UserSerializer()
    class Meta:
        model=QuestionPerformance
        #fields=["id", 'question', "user", 'score']
        fields=["id", 'score']

class BasicAssessmentPerformanceSerializer(serializers.ModelSerializer):
    #question = QuestionSerializer()
    #user = UserSerializer()
    class Meta:
        model=AssessmentPerformance
        #fields=["id", 'question', "user", 'score']
        fields=["id", 'report']
