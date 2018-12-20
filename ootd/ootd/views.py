from django.shortcuts import render
import random
import sys
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from pyowm import OWM

import clothes.models

@login_required(login_url="/users/login/")
def home(request):
    
    # model = Clothes

    API_key = '5010bcb0746e9daf22c7a1ca3de8cbce'

    owm = OWM(API_key)
    obs = owm.weather_at_place('Seoul')
    w = obs.get_weather()
    temp = int(w.get_temperature(unit='celsius')['temp'])


    mycloset = clothes.models.Thumb_closet.objects.filter(owner= request.user.username)
    r = []
    
    if mycloset :
        recommand = []
        
        clo={ # 0= 사계절, -n = 최고 n일 때부터 그 이하까지, n= 최고~n까지
                't-shirts': 23,   'pants': 0, 'shoes': 0,
                "tote bag": 0,  "one-piece":23, "sandals": 20,
                "hat": 0, "glasses": 0, "shirts": 23,
                "skirt":12, "outer": -20, "sports shoes": 0,
                "watch":0, "swimming suit":28,  "backpack":0,
                "baggage":0
            }#.get(c, "null")
            
        for i in mycloset:
            print(i)
            choice = clo.get(i.type, "null")
            print(i.type)
            if choice<0 and temp<= -choice:
                recommand.append(i)
            elif choice>0 and temp >= choice:
                recommand.append(i)
            
            if choice == 0:
                recommand.append(i)
        print(type(recommand))
        print(recommand)
    
        if recommand.__len__()<3 : n=recommand.__len__()
        else : n = 3
        n = random.sample(range(0,recommand.__len__()),n)
        
        for i in n:    r.append(recommand[i])

    print("R =")
    print(r)
    return render(request, "home.html",{
            "weather": w.get_status(),
            "temperature": temp,
            "recommand" : r,
            })
    



