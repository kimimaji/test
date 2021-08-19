from django.shortcuts import render
from django.http import HttpResponseRedirect
from .infoCtrl import webGet

def partsSearch(request):
    keyword = ''
    
    if len(request.POST):
        keyword = request.POST['keyword']
        keysearch = webGet()
        all_items = keysearch.PageTitle( keyword )

    else:
        all_items = {}

    return render(request, 'parts/search.html',
        {
            'keyword': keyword,
            'all_items': all_items,
        })
