from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:signup')

            # 좋은 UX를 생각해보기(회원가입 후 어떤 창으로 이동되는게 좋은지

    else: # get방식으로 요청을 했을 때(입력한 데이터들이 없을 때)
        form = CustomUserCreationForm()
    
    context = {
        'form': form,
    }

    return render(request, 'signup.html', context) 
    # 저번 플젝과 바뀐 점은 다른 class를 상속받아서 사용한 것 뿐

def login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        # 첫 인자로 request를 넣어야 함(공식문서참고)
        if form.is_valid():
            auth_login(request, form.get_user())
            # http://127.0.0.1:8000/accounts/login/?next=/articles/create/
            next_url = request.GET.get('next')


            return redirect(next_url or 'accounts:index')
            # -> 단축평가가 적용됨
            # next 인자가 url에 있을 때 => '/articles/create/'(=T, 어떤 값이 있으니깐) or 'articles:index'
            # next 인자가 url에 없을 때 => None(F)or 'articles:index' 이므로 뒤에있는 값을 사용
            # 그냥 로그인을 해서 성공을 하면 index로 가지만
            # 로그아웃 상태에서 create로 가서 로그인을 성공하면 create위치로 다시 돌아감.


    else:
        form = CustomAuthenticationForm()

    context ={
        'form': form,

    }
    return render(request, 'login.html', context)
    # 이때 signup.html 과 login.html 은 완전히 똑같은 구조
    # 따라서 나중에 form.html로 같이 쓰는 거 연습해보기
def logout(request):
    auth_logout(request)
    return redirect ('accounts:login')
