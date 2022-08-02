from django.contrib import admin

from apis.models import User, Grade, Assessment, AssessmentPerformance, Question, QuestionPerformance

class UserAdmin(admin.ModelAdmin):
    readonly_fields = ('username',)

    def username(self, instance):
        return instance.get_username()


admin.site.register(User, UserAdmin)
admin.site.register(Grade)
admin.site.register(Assessment)
admin.site.register(AssessmentPerformance)
admin.site.register(QuestionPerformance)
admin.site.register(Question)

