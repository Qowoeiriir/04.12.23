from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    host = request.META['HTTP_HOST']
    user_agent = request.META['HTTP_USER_AGENT']
    path = request.path

    return HttpResponse(f'host: {host} <br>browser: {user_agent} <br> Path: {path} <br>',
                        headers={'SecretCOde': '1254478'})

def user(request, login='nologin', name_post='none_name', id_post=0):
    return HttpResponse(f'login: {login} <br> name_post: {name_post} <br>, id_post: {id_post}',)

def error (request):
    return HttpResponse('К сожалению произошла ошибка', status=400, reason="ERROOOORRR")



       