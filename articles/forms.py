from django import forms
from .models import Article, Comment

# ModelForm 은 model 을 알려주기만 하면 자동으로 form을 만들어줌

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label = 'Title',
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    
    
    class Meta:
        model = Article
        # fields = '__all__'
        # fields = ('title', 'content',)
        exclude = ('user',)
        # widgets = {
        #     'title': forms.TextInput(attrs={'class': 'form-contrl'}),
        #     'content': forms.Textarea(attrs={'class': 'form-control'})
        # }
        
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('content',)