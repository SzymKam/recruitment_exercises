# models.py
from django.db import models

class Entities(models.Model):
    '''Podmiot.'''
    name = models.TextField(verbose_name="Podmiot")
    address = models.TextField(verbose_name ="Adres", blank=True, null=True)

    # add Model into class name, delete description -> it gives no additional info now,
    # for name use, char field, use english for description/names

class Invoice(models.Model):
    '''Faktura.'''
    name = models.CharField(verbose_name='nr faktury', unique=True)
    created_at = models.DateTimeField(verbose_name='data utworzenia', auto_now_add=True)
    value = models.FloatField(verbose_name='kwota netto')
    entity = models.OneToOneField(Entities, on_delete=models.SET_NULL, null=True, blank=True)

    # add Model into class name, delete description -> it gives no additional info now,
    # use english for description/names

    TAX = 23

    # if want tax as constant, move it into separate file

    def update_value(self):
        self.value = 0
        for item in self.item_set().all():
            self.value += item.product.value

        self.save(update_fields=['value'])

    # item_set doesn't exist, cant get queryset from db. Logic like this should be in views.
    # it's model class

    @property
    def value_with_tax(self):
        return self.value * self.TAX

    # maybe just use here tax value, instead of constants value. Its used just one, and created inside class.
    # tax value should be value += 0,23 * value


class Product(models.Model):
    """Produkt."""
    name = models.TextField(verbose_name="Produkt")
    value = models.FloatField(verbose_name="kwota netto")
    tax = models.FloatField(verbose_name="podatek")

 # add Model into class name, delete description -> it gives no additional info now,
 # use char field in name,


class Item(models.Model):
    """Pozycje na fakturze."""
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    invoice = models.ForeignKey(Invoice, on_delete =models.CASCADE)

# add Model into class name, delete description -> it gives no additional info now,
# can add just one product as item. Maybe add field item to Invoice
# why protect? when delete product it should be deleted from invoice?


# exports.py
import csv
# from .models import *
from django.db.models import Sum

def exportInvoceFiles():
    with open ('zamówienia', 'w') as _f:
        stream = csv.writer(_f)
        stream.writerow(['Podmiot', 'Ile ma zamówień', 'Na łączną kwotę'])
        for entity in Entities.objects.all():
            stream.writerow ([
                entity.name , Invoice.objects.filter(entity=entity).count(),
                Invoice.objects.filter(entity=entity).aggregate(sum=Sum('value'))['sum'] * Invoice.TAX
            ])

# class name should not use CamelCase, maybe use select related or prefetch one request into db, now we have 2n+1
# database requests


def export_data_invoice(invoice_id):
    """Generator, który zwraca kolejne wiersze do wyświetlenia/zapisania do pliku."""
    invoice = Invoice.objects.get(id=invoice_id)
    yield invoice.entity.name
    value = 0
    for item in invoice.item_set().all():
        yield item.product.name, item.product.value, item.product.tax
        value += item.product.value * item.product.tax

    yield f'\n\n Do zapłaty: {value} zł (brutto)'

# add typing,
# function never used,
# why yield all of these information?
# invoice entity name -> next request into db
# what is invoice.item_set().all(): ?
# value sohuld be increased every time by item value += item value * tax
