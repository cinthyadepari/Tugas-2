
from django.shortcuts import render, redirect
from mywatchlist.models import ModelMyWatchList
from django.http import HttpResponse
from django.core import serializers

def readHtml(request):
    all_watchlist = ModelMyWatchList.objects.all()

    context = {
        'all_watchlist' : all_watchlist,
        'title' : 'All Watch List'
    }
    print(all_watchlist)

    return render(request, 'read.html', context)


def readXml(request):
    all_watchlist = ModelMyWatchList.objects.all()

    return HttpResponse(serializers.serialize("xml", all_watchlist), content_type="application/xml")

def readJson(request):
    all_watchlist = ModelMyWatchList.objects.all()

    context = {
        'all_watchlist' : all_watchlist,
        'title' : 'All Watch List'
    }
    print(all_watchlist)

    return HttpResponse(serializers.serialize("json", all_watchlist), content_type="application/json")

