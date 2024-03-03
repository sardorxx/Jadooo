from django.contrib import admin
from features.models import QuestionAnswer


class QuestionAnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'question')


admin.site.register(QuestionAnswer)
