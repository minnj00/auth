from django.db import models
from accounts.models import User
from django.conf import settings
from django.contrib.auth import get_user_model

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    # commnet_set = 장고가 자동으로 추가해주는 컬럼

    # 유저모델을 참조하는 경우
    # 방법 1. (권장하지않음) 왜냐하면 변경 가능성 있는 변수는 변수화를 하는게 좋음(ex. AUTH_USER_MODEL 설정한 것을 이용)
    # user = models.ForeignKey(User, on_delete = models.CASCADE)
    # 방법 2. (권장) settings.AUTH_USER_MODEL = 'acoounts.User'
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # 방법 3. (권장)
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    # user_id 장고가 자동으로 추가해주는 컬럼, 실제 sql db에는 숫자만 사용할 수 있으므로 user_id만 저장



class Comment(models.Model):
    content = models.TextField()
    article = models.ForeignKey(Article, on_delete = models.CASCADE)
    # article_id 는 장고가 자동으로 추가해주는 컬럼

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    # user_id 컬럼을 장고가 자동으로 추가

# 어떤 a라는 게시물을 작성한 user이 단 comment 
# a에서 user에 접근 user model에서 comment_set 접근
# a.user.comment_set.all 

