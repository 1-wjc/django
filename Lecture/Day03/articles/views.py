from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'name': 'SSAFY',
    }
    return render(request, 'articles/index.html', context)

def search(request):
    return render(request, 'articles/search.html')

def find(request):
    '''
    사용자가 입력한 키워드를 받아서 화면에 출력
    '''
    user_data = request.GET.get('q')
    context = {
        'user_data': user_data,
    }
    return render(request, 'articles/find.html', context)