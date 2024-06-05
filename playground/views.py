from django.shortcuts import render
# from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q,F
from store.models import Product
def say_hello(request):
    # query_set=Product.objects.filter(inventory=F('unit_price'))
    # query_set=Product.objects.order_by('title')
    #0,1,2,3,4
    # query_set=Product.objects.all()[:5]
    #5,6,7,8,9
    # query_set=Product.objects.all()[5:5]
    
    #dictionary
    # query_set=Product.objects.values('id','title','collection__title')
    
    query_set=Product.objects.filter(id__in=Product.objects.values('id').distinct()).order_by('title')
    # query_set=Product.objects.values('id').distinct()
    #dictionary as tuple 
    # query_set=Product.objects.values_list('id','title','collection__title')
    
    # product=Product.objects.order_by('unit_price')[0]
    # product=Product.objects.earliest('unit_price')
    # product=Product.objects.latest('unit_price')  
    
    return render(request,'hello.html',{'name':'Mosh','products':list(query_set)})
