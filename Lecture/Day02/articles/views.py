from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'name': '서울2반'
    }
    return render(request, 'articles/index.html', context)

def login(request):
    '''
    사용자에게 로그인 화면을 제공
    로그인 화면에 데이터를 채워야 할까? 없음 => context 필요 없음
    '''
    return render(request, 'articles/login.html')

def auth(request):
    '''
    사용자의 로그인 정보를 바탕으로 로그인을 처리하는 역할
    사용자의 요청 정보는 request 객체에 다 들어있다.
    '''
    # request.GET.get('name속성값')
    userid = request.GET.get('userid')
    password = request.GET.get('pw')

    #userid 님, 로그인을 환영합니다!
    context = {
        'userid': userid,
    }
    return render(request, 'articles/welcome.html', context)