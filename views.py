from django.shortcuts import render
from django.http import HttpResponse
import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from models import search
from models import site
import time;

def index(request):
    page = "index"

    search_keyword = request.GET.get("keyword")
    search_page = int(request.GET.get("page",1))

    start = time.time()
    search_result = search.result(request.GET.get("keyword"),search_page)
    done = time.time()
    search_result_time = done - start

    return render(request,"index.html",{"page":page,"keyword":search_keyword,"search_result":search_result,"search_result_time":search_result_time})

def images(request):
    page = "images"

    search_keyword = request.GET.get("keyword")
    search_page = int(request.GET.get("page",1))

    start = time.time()
    search_result = search.result(request.GET.get("keyword"),search_page)
    done = time.time()
    search_result_time = done - start

    return render(request,"index.html",{"page":page,"keyword":search_keyword,"search_result":search_result,"search_result_time":search_result_time})

@api_view(['POST'])
def search_suggest(request):
    keyword = request.POST.get("keyword")

    data = {
        'is_taken': keyword
    }
    return JsonResponse(data)

@api_view(['POST'])
def site_visit(request):
    id = request.GET.get("id")
    keyword = request.GET.get("keyword")

    site.visit(id,keyword)

    data = {
        'keyword': keyword
    }
    return JsonResponse(data)

