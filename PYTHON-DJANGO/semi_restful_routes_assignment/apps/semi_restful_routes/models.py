from __future__ import unicode_literals
from django.db import models
import re
from decimal import *

price_regex = re.compile(r'^\d+[.]?[\d]?[\d]?$')

class ProductManager(models.Manager):

    def new(self, postData):

        # validate form data
        # a tuple is returned in the format of (Bool, messages)
        #   if False, then don't add to DB
        #   if True, messages will be an empty list, add product to DB, and add a success message to list
        # return the response
        response = self.validate_product(postData)

        if response[0] == False:
            return response

        else:

            # add product to DB
            Product.objects.create(name=postData['name'], description=postData['description'], price=Decimal(postData['price']))

            response[1].append('Successfully added {}'.format(postData['name']))

            return response


    def edit(self, id, postData):

        response = self.validate_product(postData)

        if response[0] == False:

            return response

        else:
            product = Product.objects.get(id=id)

            product.name = postData['name']
            product.description = postData['description']
            product.price = Decimal(postData['price'])
            product.save()

            response[1].append('Product id {} ({}) successfully updated'.format(id, product.name))

            return response


    def validate_product(self, postData):

        messages = []

        # basic validations
        if postData['name'] == "":
            messages.append('Name cannot be blank')

        if postData['description'] == "":
            messages.append('Description cannot be blank')

        if postData['price'] == "":
            messages.append('Price cannot be blank')

        elif not re.match(price_regex, postData['price']):
            messages.append('Please enter price in format 0.00')

        if messages:
            return (False, messages)

        else:
            return (True, messages)


    def destroy(self, id):

        Product.objects.get(id=id).delete()



class Product(models.Model):

    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ProductManager()

    def __str__(self):
        print self.name
