# models.py
from django.db import models

class Entities ( models . Model ):
    '''Podmiot.'''
    name = models . TextField ( verbose_name = "Podmiot" )
    address = models . TextField ( verbose_name = "Adres" , blank = True , null = True )


class Invoice ( models . Model ):
    '''Faktura.'''
    name = models . CharField ( verbose_name = 'nr faktury' , unique = True )
    created_at = models . DateTimeField ( verbose_name = 'data utworzenia' , auto_now_add = True )
    value = models . FloatField ( verbose_name = 'kwota netto' )
    entity = models . OneToOneField ( Entities , on_delete = models . SET_NULL , null = True , blank = True )


    TAX = 23
    def update_value ( self ):
        self . value = 0
        for item in self . item_set () . all ():
            self . value += item . product . value

        self . save ( update_fields = [ 'value' ])

    @property
    def value_with_tax ( self ):
        return self . value * self . TAX


class Product ( models . Model ):
    """Produkt."""
    name = models . TextField ( verbose_name = "Produkt" )
    value = models . FloatField ( verbose_name = "kwota netto" )
    tax = models . FloatField ( verbose_name = "podatek" )

class Item ( models . Model ):
    """Pozycje na fakturze."""
    product = models . ForeignKey ( Product , on_delete = models . PROTECT )
    invoice = models . ForeignKey ( Invoice , on_delete = models . CASCADE )

# exports.py
import csv
from .models import *
from django.db.models import Sum

def exportInvoceFiles ():
with open ( 'zamówienia' , 'w' ) as _f :
stream = csv . writer ( _f )
stream . writerow ([ 'Podmiot' , 'Ile ma zamówień' , 'Na łączną kwotę' ])
for entity in Entities . objects . all ():
stream . writerow ([
entity . name , Invoice . objects . filter ( entity = entity ) . count (),
Invoice . objects . filter ( entity = entity ) . aggregate ( sum = Sum ( 'value' ))[ 'sum' ] * Invoice . TAX
])

def export_data_invoice ( invoice_id ):
"""Generator, który zwraca kolejne wiersze do wyświetlenia/zapisania do pliku."""
invoice = Invoice . objects . get ( id = invoice_id )
yield invoice . entity . name
value = 0
for item in invoice . item_set () . all ():
yield item . product . name , item . product . value , item . product . tax
value += item . product . value * item . product . tax

yield f ' \n\n Do zapłaty: {value} zł (brutto)'