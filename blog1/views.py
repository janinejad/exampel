from django.shortcuts import render
# from django.shortcuts import HttpResponse
from django.http import HttpResponse


def hello(request):
    return render(request, 'home.html', {})


def contact(request):
    return render(request, 'contact.html', {})


def about(request):
    return render(request, 'about.html', {})


def get_plan(request, day_id=None):
    plans = ['اسکات پا 4*10 - لانگ 3*12', 'استراخت', 'پرس سینه 4*12 - جلوبازو 4*12', 'زیربغل سیم کش 4*12 ', 'استراحت',
            'سرشانه آرنولدی 3*12- نشر خم 3*12', 'استراحت']
    days = ['شنبه','یکشنبه','دوشنبه','سشنبه','چهارشنبه','پنج شنبه','جمعه']
    try:
        plan = ''
        day = ''
        plan = plans[day_id]
        day = days[day_id]
    except:
        plan = 'روز مورد نظر یافت نشد'
        day = 'روز مورد نظر یافت نشد'

    context = {
        'plan' : plan,
        'day': day
    }

    return render(request,'bodibuilding-plan.html',context)
