# models 모듈을 import
from django.db import models
from . import views

# models 모듈의 Model 클래스를 상속
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)