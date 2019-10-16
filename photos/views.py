from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import Location,Category,Image



# Create your views here.
# def welcome(request):
#     return render(request, 'welcome.html')

def welcome(request):
    images = Image.objects.all()
    locations = Location.objects.all()
    categories = Category.objects.all()
    title = 'Home'

    return render(request,'welcome.html', {'images':images,'locations':locations,'categories':categories, 'title':title})


def search_results(request):
    locations = Location.objects.all()
    categories = Category.objects.all()
    title = 'Search'

    if 'gallery' in request.GET and request.GET["gallery"]:
        search_term = request.GET.get("gallery")
        searched_images = Image.search_by_category(search_term)
        message = f"Results for: {search_term}"

        return render(request, 'welcome.html',{"message":message,"images": searched_images,'locations':locations,'categories':categories, 'title':title})

    else:
        message = "You haven't searched for any things."
        return render(request, 'welcome.html' ,{"message":message})
def categoryPage(request,category):
    locations = Location.objects.all()
    categories = Category.objects.all()
    title = f"{category}"
    category_results = Image.search_by_category(category)
    return render(request,'welcome.html',{'images':category_results,'locations':locations,'categories':categories, 'title':title})

def locationPage(request,location):
    locations = Location.objects.all()
    categories = Category.objects.all()
    title = f"{location}"
    location_results = Image.filter_location(location)
    return render(request,'welcome.html',{'images':location_results,'locations':locations,'categories':categories, 'title':title})
