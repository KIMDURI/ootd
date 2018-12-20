from django.shortcuts import render, redirect
from django.conf import settings
from .forms import ClosettForm
from .models import Thumb_closet, Closet

import requests
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.patches as patches
from PIL import Image
from random import choice
import string


def upload(request):
    if request.method == 'POST':
        form = ClosettForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.owner = request.user
            forms = form.save()

            form.save()
            return redirect('mypage')
    else:
        form = ClosettForm()
    return render(request, 'closet/upload.html', {
        'form': form
    })

def Thumb(request):
    last = Closet.objects.all().order_by('-id').first()

    url = "https://kapi.kakao.com/v1/vision/product/detect"
    MYAPP_KEY = '678c513cf06694d22f0ba87719ae6b82'
    headers = {'Authorization': 'KakaoAK {}'.format(MYAPP_KEY)}

    filename = str(Closet.objects.get(id=last.id).origin_img)
    filename = 'clothes/media/'+filename
    print(filename)
    # clothes/photo/boy1.jpg
    files = { 'file' : open(filename, 'rb')}

    response = requests.post(url, headers=headers, files=files)

    result = response.json()
    fig_w, fig_h = result['result']['width'], result['result']['height']

    cropList=[]
    my=[]
    img = mpimg.imread(filename)
    crop_img = Image.open(filename)

    fig,ax = plt.subplots(figsize=(10,10))

    for each in result['result']['objects']:
        x, y = each['x1']*fig_w, each['y1']*fig_h
        w, h = each['x2']*fig_w - x, each['y2']*fig_h - y
        rect = patches.Rectangle((x, y), w, h, lw=5, edgecolor='c', facecolor='none')
        ax.add_patch(rect)
        plt.text(x,y-10, each['class'], size=18, color='red')
        crop = (each['x1']*fig_w, each['y1']*fig_h, each['x2']*fig_w,each['y2']*fig_h)
        cimg = (crop_img.crop(crop))
        cropList.append(cimg)
        my.append(each['class'])
        
        arr = [choice(string.ascii_letters) for _ in range(3)]
        pid = ''.join(arr)
        
        # thumbname=str(settings.MEDIA_URL+str(request.user.get_username()) + "/"+pid + "_" + each['class'] + ".jpg")
        thumbname=str(filename.replace(".jpg","")+pid + "_" + each['class'] + ".jpg")
        
        
        print(thumbname)
        cimg.save(thumbname, 'JPEG')
        
        thumbtype=str(each['class'])
        print(request.user.get_username())
        thumb = Thumb_closet.objects.create(origin=last, type=thumbtype, thumb=thumbname, owner=request.user.get_username())
      
        print(thumbtype)
        
        
    
    return redirect('usercloset')
   
    

def Usercloset(request):

     t = Thumb_closet.objects.filter(owner= request.user.username)
     # c = Closet.objects.get(id=1)
     
     # print(c.origin_img)
     print(t)


     return render(request, 'closet/myroom.html', {
            't':t,
            'user':request.user.username,
            # 'closet':c,
        })
