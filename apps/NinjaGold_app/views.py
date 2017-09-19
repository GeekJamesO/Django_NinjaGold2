from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib import messages
from random import random, randint
from datetime import datetime
def index(request):
    try:
        yourgold = request.session['yourGold']
        history = request.session['history']
    except Exception as e:
        return redirect('/reset')
    context = { }
    return render(request, "NinjaGold_app/index.html", context)

def process_money(request, methods=['POST']):
    try:
        yourgold = request.session['yourGold']
        # history = request.session['history']
        building = request.POST['building']
    except Exception as e:
        print e.message
        messages.error(request, 'You must do this from the home page.' + e.message)
        return redirect('/')
    low = 10
    high = 20
    resultMsg = ''
    theTime = datetime.now()
    if building == 'Farm':
        low = 10
        high = 20
    elif building == 'Cave':
        low = 5
        high = 10
    elif building == 'House':
        low = 2
        high = 5
    else:   # building == 'Casino':
        low = -50
        high = 50
    earnedGold = randint(low, high)
    yourgold += earnedGold
    request.session['yourGold'] += earnedGold
    if earnedGold >= 0:
        resultMsg = "<div class='green'>Earned {} gold from the {}!<//div>".format(earnedGold, building, theTime)
    else:
        resultMsg = "<div class='red'>Entered a {} and lost {} gold!<//div>".format(building, -1 * earnedGold, theTime)
    request.session['history'].append(resultMsg)
    return redirect('/')

def reset(request, methods=['POST']):
    request.session['yourGold'] = 0
    request.session['history'] = []
    return redirect('/')
