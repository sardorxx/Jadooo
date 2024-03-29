from django.contrib import admin
from features.models import QuestionAnswer, News


class QuestionAnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'question')


admin.site.register([QuestionAnswer, News])
