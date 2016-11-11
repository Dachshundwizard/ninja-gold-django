from django.shortcuts import render, redirect
import random

# Create your views here.
def index(request):
    return render(request, 'gold/index.html')#takes in at least two perameter, reuqest is the object that contains info from the HTTP request.

def process(request):
    if 'gold' not in request.session: # if there isnt a value, set it to 0
        request.session['gold'] = 0 #this will save the session info for the whole time
    if 'activity' not in request.session:
        request.session['activity'] = []

    if request.POST['building'] == 'farm':
        farm_gold = random.randint(10,20)
        request.session['gold'] += farm_gold
        request.session['activity'].append('you went to the farm and made' + str(farm_gold))

    elif request.POST['building'] == 'cave':
        cave_gold = random.randint(5,10)
        request.session['gold'] += cave_gold
        request.session['activity'].append('you went to the cave and made' + str(cave_gold))

    elif request.POST['building'] == 'house':
        house_gold = random.randint(2,5)
        request.session['gold'] += house_gold
        request.session['activity'].append('you went to the house and made' + str(house_gold))

    elif request.POST['building'] == 'casino':
        casino_gold = random.randint(-50,50)
        request.session['gold'] += casino_gold
        request.session['activity'].append('you went to the casino and made' + str(casino_gold))

    return redirect('/')#do not need a request in redirect

def reset(request):
    del request.session['gold']
    del request.session['activity']
    return redirect('/')
