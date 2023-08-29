from .models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class CustomUserCreationForm(UserCreationForm):

    # 원래 UserCreationForm 의 클래스에는 Meta 클래스가 원래의 User를 사용하고 있음.
    # 우리가 새로 만든 User로 바꿔줘야함. 
    class Meta:
        model = User
        fields = ('username', )

class CustomAuthenticationForm(AuthenticationForm):
    pass
