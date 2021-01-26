from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from .models import Product
from .forms import ProductForm


def product_create_view_raw_form(request):
    context = {}
    return render(request, "product/product_create_raw_form.html",context)


def product_create_view(request):
    form  = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form  = ProductForm()
    context = {
        "form": form
    }
    return render(request, "product/product_create.html",context)

def product_detail_view(request,*args,**kwargs):
    obj = Product.objects.get(id=1)
    # context = {
    #     "title":obj.title,
    #     "summary":obj.summary

    # }

    context = {
        "object":obj
    }
    return render(request, "product/product_detail.html",context)

# Create your views here.
def hello(request,*args,**kwargs):
    print(request.user,args,kwargs)
    #return HttpResponse("<h1>Hello World</h1>")
    return render(request,'home.html',{})

def contact(request,*args,**kwargs):
    #return HttpResponse("<h1>Hello Contact</h1>")
    return render(request,'contact.html',{})

def about(request,*args,**kwargs):
    #return HttpResponse("<h1>About About</h1>")
    context = {
        "my_text":"abc this is about me",
        "my_number": 123,
        "my_list" : [1,2,3,4],
        "my_condition":True,
        "my_html":"<h1>To be viewed as html : Hello world</h1>",
        "my_nest":{
            "my_home":{
                "my_room":"200111"
            }
        }
    }
    return render(request,'about.html',context)

