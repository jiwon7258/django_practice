from django.contrib import admin
from polls.models import Question, Choice

# Register your models here.
# admin 사이트의 UI를 변경하는 작업은 보통 여기에서 진행한다


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2


# Question에 대한 admin UI를 설정하는 클래스
# 나중에 register할 때 인자로 넘겨준다
class QuestionAdmin(admin.ModelAdmin):
    # Question 자체의 UI에 대한 속성들을 정의
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        (
            "Date information",
            {"fields": ["pub_date"], "classes": ["collapse"]},
        ),  # collpase 속성이므로 기본적으로 hide 처리되어 있다
    ]
    # Choice 모델 클래스 같이 보기
    inlines = [ChoiceInline]
    # 레코드 리스트의 컬럼 항목 지정
    list_display = ("question_text", "pub_date")
    list_filter = ["pub_date"]
    search_fields = ["question_text"]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
