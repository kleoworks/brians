from django.shortcuts import render, redirect
import random
from datetime import datetime

def index(request):

    # if new session, create variable to track gold won and list for activity log
    # activities will be stored in session but passed to index.html using context
    if 'gold' not in request.session:
        request.session['gold'] = 0;

    if 'activities' not in request.session:
        request.session['activities'] = []

    # store activities in context and reverse the order
    context = {
        'activities': request.session['activities']
    }
    context['activities'].reverse()

    return render(request, 'ninja_gold/index.html', context)


###################################
# 1st attempt using hidden inputs #
###################################

# def process_money(request):
#
#     # if someone made it to this page without form post, redirect to index
#     if request.method != 'POST':
#         return redirect('/')
#
#     # check WHICH building using the form's hidden inputs
#     # calculate random gold
#     # if casino, set gamble (0 = loose, 1 = win)
#     # store activity as tuple (css class, amount of gold, building name, date)
#     # use template to render activity text
#     # redirect to main page
#
#     if request.POST['building'] == 'farm':
#         gold = random.randint(10,20)
#         request.session['gold'] += gold
#         request.session['activities'].append(('won', gold, request.POST['building'], datetime.now().strftime('%Y/%m/%d %I:%M %p')))
#
#     elif request.POST['building'] == 'cave':
#         gold = random.randint(5,10)
#         request.session['gold'] += gold
#         request.session['activities'].append(('won', gold, request.POST['building'], datetime.now().strftime('%Y/%m/%d %I:%M %p')))
#
#
#     elif request.POST['building'] == 'house':
#         gold = random.randint(2,5)
#         request.session['gold'] += gold
#         request.session['activities'].append(('won', gold, request.POST['building'], datetime.now().strftime('%Y/%m/%d %I:%M %p')))
#
#
#     elif request.POST['building'] == 'casino':
#         gamble = random.randint(0,1)
#         if gamble:
#             # ninja wins gold
#             gold = random.randint(0,50)
#             request.session['gold'] += gold
#             request.session['activities'].append(('won', gold, request.POST['building'], datetime.now().strftime('%Y/%m/%d %I:%M %p')))
#
#         else:
#             # ninja looses gold
#             gold = random.randint(0,50)
#             request.session['gold'] -= gold
#             request.session['activities'].append(('loss', gold, request.POST['building'], datetime.now().strftime('%Y/%m/%d %I:%M %p')))
#
#     return redirect('/')


##########################################
#  ------------------------------------  #
# | refactored using routes parameters | #
#  ------------------------------------  #
##########################################

def process_money(request, building):

    # if someone made it to this page without form post, redirect to index
    if request.method != 'POST':
        return redirect('/')

    # check WHICH building using route parameter
    # calculate random gold
    # if casino, set gamble (0 = loose, 1 = win)
    # store activity as tuple (css class, amount of gold, building name, date)
    # use template to render activity text
    # redirect to main page

    if building == 'farm':
        gold = random.randint(10,20)
        request.session['gold'] += gold
        request.session['activities'].append(('won', gold, building, datetime.now().strftime('%Y/%m/%d %I:%M %p')))

    elif building == 'cave':
        gold = random.randint(5,10)
        request.session['gold'] += gold
        request.session['activities'].append(('won', gold, building, datetime.now().strftime('%Y/%m/%d %I:%M %p')))


    elif building == 'house':
        gold = random.randint(2,5)
        request.session['gold'] += gold
        request.session['activities'].append(('won', gold, building, datetime.now().strftime('%Y/%m/%d %I:%M %p')))


    elif building == 'casino':
        gamble = random.randint(0,1)
        if gamble:
            # ninja wins gold
            gold = random.randint(0,50)
            request.session['gold'] += gold
            request.session['activities'].append(('won', gold, building, datetime.now().strftime('%Y/%m/%d %I:%M %p')))

        else:
            # ninja looses gold
            gold = random.randint(0,50)
            request.session['gold'] -= gold
            request.session['activities'].append(('loss', gold, building, datetime.now().strftime('%Y/%m/%d %I:%M %p')))


    return redirect('/')
