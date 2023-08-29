from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass
    # article_set = 자동으로 추가 (article.models 에 foreignkey를 생성했기 때문에)
    # comment_set 