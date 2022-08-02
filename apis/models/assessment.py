from django.db import models
from apis.models.user import BaseModel
from django.contrib.postgres.fields import ArrayField

ASSESSMENT_LEVEL = [('E', "Easy"), ('I', 'Intermediate'), ('H', 'Hard')]
ASSESSMENT_CATEGORY = [('SK', "Skill"), ('PR', 'Personality'), ('AP', 'Aptitude')]

class Assessment(BaseModel):
    grade = models.ForeignKey('Grade', on_delete=models.DO_NOTHING)
    level = models.CharField(max_length=10, choices=ASSESSMENT_LEVEL)
    category = models.CharField(max_length=10, choices=ASSESSMENT_CATEGORY)
    weightage = models.IntegerField()

    def __str__(self):
        return "%s-%s-%s"%(self.grade, self.category, self.level)

class Question(BaseModel):
    content = models.TextField(null=False, blank=False)
    assessment = models.ForeignKey('Assessment', on_delete=models.DO_NOTHING, null=False, blank=False)
    is_multiple_choice = models.BooleanField(default=False)
    choices = ArrayField(models.CharField(max_length=100, blank=True), null=False, blank=False)
    correct_choices = ArrayField(models.CharField(max_length=100, blank=False))
    weightage = models.IntegerField(null=False, blank=False)
    study_plan = models.JSONField(null=True, blank=True)
    strengths_required = ArrayField(models.CharField(max_length=100), blank=True, null=True)

class AssessmentPerformance(BaseModel):
    assessment = models.ForeignKey('Assessment', on_delete=models.DO_NOTHING, null=False, blank=False)
    user = models.ForeignKey('User', on_delete=models.DO_NOTHING, null=False, blank=False)
    report = models.JSONField(null=True, blank=True)
    
class QuestionPerformance(BaseModel):
    assessment_performance = models.ForeignKey('AssessmentPerformance', on_delete=models.DO_NOTHING, null=False, blank=False)
    question = models.ForeignKey('Question', on_delete=models.DO_NOTHING, null=False, blank=False)
    user = models.ForeignKey('User', on_delete=models.DO_NOTHING, null=False, blank=False)
    score = models.IntegerField(null=False, blank=False)

