from django.shortcuts import render

# Create your views here.
def hello(request):
    '''
    사용자에게 Hello Django 페이지를 출력하는 기능
    '''
    return render(request, 'my_app/hello.html')