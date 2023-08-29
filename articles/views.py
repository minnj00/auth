from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    articles = Article.objects.all()
    
    context = {
        'articles': articles
    }
    return render(request, 'index.html', context)

@login_required
def create(request):
    # if not request.user.is_authenticated:
    #     return redirect('accounts:login')
    #login_required

    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False) # ArticleForm으로는 user에 대한 정보를 받지 못했으니깐 저장을 잠깐 멈춤.
            
            # article 테이블의 user 컬럼에 정보를 할당할 것.
            article.user = request.user  # 에러 창에서 request 항목을 보면 user 는 현재 로그인 된 user로 되어있음
            article.save()
            return redirect('articles:index')

    else:
        form = ArticleForm()
    
    context = {
        'form': form
    }

    return render(request, 'form.html', context )
        