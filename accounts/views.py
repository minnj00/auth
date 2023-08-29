from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout


# Create your views here.

def signup(request):
    if request.user.is_authenticated:
        # 로그인을 한 상태에서는 index 로 가도록
        return redirect('article:index')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        # 여기에서의 form은 인스턴스화가 되었긴 하지만 아직까지 modelform 클래스인 것.
        if form.is_valid():
            user = form.save() # form 을 save를 해야만 그 안의 데이터들이 밖으로 나오게 됨.
            # user에 form.save()한 인스턴스가 할당됨(User클래스의(결국 AbstractUser클래스의) column 데이터들이 할당됨.
            auth_login(request, user)
            return redirect('accounts:login')

            # 좋은 UX를 생각해보기(회원가입 후 어떤 창으로 이동되는게 좋은지

    else: # get방식으로 요청을 했을 때(입력한 데이터들이 없을 때)
        form = CustomUserCreationForm()
    
    context = {
        'form': form,
    }

    return render(request, 'account_form.html', context) 
    # 저번 플젝과 바뀐 점은 다른 class를 상속받아서 사용한 것 뿐

def login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        # 첫 인자로 request를 넣어야 함(공식문서참고)
        if form.is_valid():
            auth_login(request, form.get_user())
            # http://127.0.0.1:8000/accounts/login/?next=/articles/create/
            next_url = request.GET.get('next')


            return redirect(next_url or 'articles:index')
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
    return render(request, 'account_form.html', context)
    # 이때 signup.html 과 login.html 은 완전히 똑같은 구조
    # 따라서 나중에 form.html로 같이 쓰는 거 연습해보기
def logout(request):
    auth_logout(request)
    return redirect ('accounts:login')
