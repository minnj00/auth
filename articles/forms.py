from django import forms
from .models import Article

# ModelForm 은 model 을 알려주기만 하면 자동으로 form을 만들어줌

class ArticleForm(forms.ModelForm):
    
    class Meta:
        model = Article
        # fields = '__all__'
        # fields = ('title', 'content',)
        exclude = ('user',)