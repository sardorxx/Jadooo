from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from features.models import QuestionAnswer, News


# Create your views here.

@login_required
def answer_question(request):
    question_answer = QuestionAnswer.objects.all()
    context = {
        'question_answer': question_answer
    }
    return render(request, 'left_sidebar/setting_privicy.html', context)


@login_required
def news_list(request):
    news = News.objects.all()
    context = {
        'news_list': news
    }
    return render(request, 'left_sidebar/news.html', context=context)
