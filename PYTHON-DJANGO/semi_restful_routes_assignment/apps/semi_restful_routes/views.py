from django.shortcuts import render, redirect
from .models import Product
from django.contrib import messages

def index(request):

    # GET -- show all products
    if request.method != 'GET':

        return redirect('products:index')


    else:

        context = {

            'products': Product.objects.all()

        }

        request.session['last_url'] = 'products:index'

        return render(request, 'semi_restful_routes/index.html', context)


def new(request):

    # GET -- display form to add new product
    if request.method != 'GET':
        return redirect('products:index')

    else:

        return render(request, 'semi_restful_routes/new.html')


def create(request):

    # POST -- add new product

    if request.method != 'POST':


        return redirect('products:index')

    else:

        response = Product.objects.new(request.POST)

        if response[0] == False:
            for message in response[1]:
                messages.error(request, message)
            return redirect('products:new')

        else:
            for message in response[1]:
                messages.success(request, message)
            return redirect('products:index')


def show(request, id):

    # GET -- show specific product
    if request.method != 'GET':
        return redirect('products:index')

    else:
        context = {

            'product': Product.objects.get(id=id)

        }

        return render(request, 'semi_restful_routes/show.html', context)


def edit(request, id):

    try:

        print '*'*50
        print request.META['HTTP_REFERER']
        print '*'*50

    except:
        pass

    # GET -- display form to edit specific product
    if request.method != 'GET':
        return redirect('products:index')

    else:

        context = {

            'product': Product.objects.get(id=id)
        }

        return render(request, 'semi_restful_routes/edit.html', context)


def update(request, id):

    # POST -- update specific product
    if request.method != 'POST':

        return redirect('products:index')

    else:

        response = Product.objects.edit(id, request.POST)

        if response[0] == False:

            for message in response[1]:
                messages.error(request, message)

            return redirect('products:edit', id=id)

        else:

            for message in response[1]:
                messages.success(request, message)

            return redirect('products:index')


def destroy(request, id):

    # POST -- delete specific product
    if request.method != 'POST':
        return redirect('products:index')

    else:
        Product.objects.destroy(id)
        return redirect('products:index')
