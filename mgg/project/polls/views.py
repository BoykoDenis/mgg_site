from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world. You r in the polls index.")
# Create your views here.

def detail(request, question_id):
    return HttpResponse("you r looking at question %s." % question_id)

def results(request, question_id):
    response = "U r looking ath the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    print('hello')
    return HttpResponse("U r votin on question %s." % question_id)
