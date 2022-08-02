from rest_framework import serializers
from apis.serializers.user import UserSerializer, GradeSerializer
from apis.models import Assessment, QuestionPerformance, Question, AssessmentPerformance

class AssessmentSerializer(serializers.ModelSerializer):
    grade = GradeSerializer()
    class Meta:
        model= Assessment
        fields=["id", 'level', "category", 'grade', 'weightage']

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
