from django.http import request
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from .models import Question, Choice

# Create your views here.
def index(request):
    # DB에서 Question 객체를 가져온다
    latest_question_list = Question.objects.all().order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)


def detail(request, question_id):
    # Question 모델 클래스로부터 pk=question_id 검색 조건에 맞는 객체를 조회
    question = get_object_or_404(Question, pk=question_id)
    # 이 함수는 question 객체를 context 인자의 형태로 템플릿에 넘겨준다
    return render(request, "polls/detail.html", {"question": question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        # Choice 테이블의 레코드들을 담고 있는 객체
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # 설문 투표 폼을 다시 보여준다
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        """ 
        POST 데이터를 정상적으로 처리하였으면,
        항상 HTTPResponseRedirect를 반환하여 리다이렉션 처리함
        (리다이렉트 응답을 받은 웹브라우저가 리다이렉트 URL로 다시 요청을 보냄)
         """
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})
