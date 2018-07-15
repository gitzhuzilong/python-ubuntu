# -*- coding:utf-8 -*-
from rest_framework import serializers
from axf.models import Product,MainDescription,Slideshow

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        mdoel = Product
        fields = ('name','longName','productId','storeNums','specifics','sort','marketPrice','price','categoryId','childId','img','keywords','brandId','brandName','safeDay','safeUnit','safeUnitDesc')

class MDSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainDescription
        fields = ('categoryld','categoryName','sort','img','product1','product2','product3')

class SlideshowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slideshow
        fields = ('trackid','name','img','sort')
