from django.shortcuts import render, redirect

# Create your views here.
def index(request):

    return render(request, 'disappearing_ninjas/index.html')


def show_all(request):

    return render(request, 'disappearing_ninjas/ninjas.html')


def show_one(request, color):

    if color == 'blue':
        name = "Leonardo"
        kind = 'turtle'

    elif color == 'orange':
        name = "Michelangelo"
        kind = 'turtle'

    elif color == "red":
        name = "Raphael"
        kind = 'turtle'

    elif color == "purple":
        name = "Donatello"
        kind = 'turtle'

    else:
        name = "Megan Fox"
        kind = 'troll'

    context = {

        'color': color,
        'name': name,
        'kind': kind

    }

    return render(request, 'disappearing_ninjas/ninja.html', context)
