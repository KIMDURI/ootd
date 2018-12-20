from django.db import models
from django.conf import settings
from PIL import Image

from random import choice
import string # string.ascii_letters : ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz


def user_path(instance, filename): #파라미터 instance는 Photo 모델을 의미 filename은 업로드 된 파일의 파일 이름
    arr = [choice(string.ascii_letters) for _ in range(8)]
    pid = ''.join(arr) # 8자리 임의의 문자를 만들어 파일명으로 지정
    extension = filename.split('.')[-1] # 배열로 만들어 마지막 요소를 추출하여 파일확장자로 지정
   # file will be uploaded to MEDIA_ROOT/user_<id>/<random>
    return '%s/%s.%s' % (instance.owner.username, pid, extension) # 예 : wayhome/abcdefgs.png

class Closet(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete='SET_NULL')
    created_date = models.DateTimeField(auto_now_add = True)
    origin_img = models.ImageField(upload_to = user_path) # 어디로 업로드 할지 지정

class Thumb_closet(models.Model):
    def path(instance, filename): #파라미터 instance는 Photo 모델을 의미 filename은 업로드 된 파일의 파일 이름
        arr = [choice(string.ascii_letters) for _ in range(8)]
        pid = ''.join(arr) # 8자리 임의의 문자를 만들어 파일명으로 지정
        extension = filename.split('.')[-1] # 배열로 만들어 마지막 요소를 추출하여 파일확장자로 지정
       # file will be uploaded to MEDIA_ROOT/user_<id>/<random>
        return '%s/%s.%s' % (instance.owner,instance.type,extension) # 예 : wayhome/abcdefgs.png
    CLOTHES = (
        ("t-shirts", "t-shirts"),
        ("pants", "pants"),
        ("shoes", "shoes"),
        ("tote bag", "tote bag"),
        ("one-piece", "one-piece"),
        ("sandals","sandals"),
        ("hat", "hat"),
        ("glasses", "glasses"),
        ("shirts","shirts"),
        ("skirt","skirt"),
        ("outer","outer"),
        ("sports shoes","sports shoes"),
        ("watch", "watch"),
        ("swimming suit","swimming suit"),
        ("backpack","backpack"),
        ("baggage","baggage"),
        ("underwear bra","underwear bra"),
        ("underwear panty","underwear panty")
    )
    origin = models.ForeignKey(Closet, on_delete='CASCADE')
    type = models.CharField(choices=CLOTHES,  blank=True, null=True, default=0, max_length=20)
    thumb = models.ImageField(upload_to = path)
    owner = models.CharField(max_length=100)


