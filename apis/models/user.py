from django.db import models
from django.conf import settings

class BaseModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    class Meta:
        abstract = True

class Grade(BaseModel):
    title = models.CharField(max_length=20)

    def __str__(self):
        return "%s-%s"%(self.title, self.id)

class User(BaseModel):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    password = models.CharField(max_length=200)
    grade = models.ForeignKey('Grade', on_delete=models.DO_NOTHING, null=True, blank=True)
    parent = models.ForeignKey('User', on_delete=models.DO_NOTHING, null=True, blank=True)
    is_institute = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)

    def __str__(self):
        return "%s_%s"%(self.first_name, self.id)

    def get_username(self):
        return "%s_%s"%(settings.USERNAME_PREFIX, self.id)
