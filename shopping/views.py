from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Brand, Feature


def shopping_page(request):
    shops = Feature.objects.all()
    return render(request, "shopping.html", {'shops': shops})


def detail(request, my_id):
    #queryset = Brand.objects.filter(select=select)
    shop = get_object_or_404(Feature, id=my_id)
    return render(request, "detail.html", {'shop': shop})


# Create your views heres
