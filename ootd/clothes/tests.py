import requests
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.patches as patches
import sys
import argparse
from PIL import Image, ImageFilter
from pilkit.processors import Thumbnail
from clothes.models import Closet

url = "https://kapi.kakao.com/v1/vision/product/detect"
MYAPP_KEY = '678c513cf06694d22f0ba87719ae6b82'
headers = {'Authorization': 'KakaoAK {}'.format(MYAPP_KEY)}

def detect_thumbnail(filename, width, height):
    headers = {'Authorization': 'KakaoAK {}'.format(MYAPP_KEY)}

    try:
        files = { 'file' : open(filename, 'rb')}
        params = {'width': width, 'height': height}
        resp = requests.post(MYAPP_KEY, headers=headers, data=params, files=files)
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        print(str(e))
        sys.exit(0)

def show_thumbnail(filename, detection_result, width, height):
    image = Image.open(filename)
    rect = detection_result['result']['thumbnail']
    thumbnail = image.crop((rect['x'], rect['y'], rect['x'] + rect['width'], rect['y'] + rect['height']))
    thumbnail = thumbnail.resize((width, height))

    return thumbnail



filename = 'photo/girls2.jpg'
# clothes/photo/boy1.jpg
files = { 'file' : open(filename, 'rb')}

response = requests.post(url, headers=headers, files=files)

# %matplotlib inline

result = response.json()
fig_w, fig_h = result['result']['width'], result['result']['height']

img = mpimg.imread('photo/girls2.jpg')
crop_img = Image.open('photo/girls2.jpg')

fig,ax = plt.subplots(figsize=(10,10))

user_clothes = {
    't-shirts':[],'pants':[], 'tote bag':[], 'one-piece':[], 'sandals':[],
    'hat':[], 'glasses':[], 'shirts':[], 'outer':[], 'sports shoes':[],
    'watch':[], 'swimming suit':[], 'backpack':[], 'baggage':[], 'underwear bra':[], 'underwear panty':[]
}

for each in result['result']['objects']:
    x, y = each['x1']*fig_w, each['y1']*fig_h
    w, h = each['x2']*fig_w - x, each['y2']*fig_h - y
    rect = patches.Rectangle((x, y), w, h, lw=5, edgecolor='c', facecolor='none')
    ax.add_patch(rect)
    plt.text(x,y-10, each['class'], size=18, color='red')
    crop = (each['x1']*fig_w, each['y1']*fig_h, each['x2']*fig_w,each['y2']*fig_h)
    cimg = (crop_img.crop(crop))
    # user_clothes[each['class']].append(cimg)
    print(each['class'])
    thumbname=str(filename.replace(".jpg","_")+str(each['class']+".jpg"))
    # image.show()

    cimg.show()
    cimg

# ax.imshow(img)
# plt.show()




