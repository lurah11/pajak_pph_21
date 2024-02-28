from django.shortcuts import render
from .forms import PajakForm
from .models import Tier,Cat
from django.http import JsonResponse

# Create your views here.

def get_category(marriage_status,no_of_children): 
    result = ""
    if "tidak" in marriage_status: 
        result += "TK/"
    else : 
        result += "K/"
    no_child = no_of_children if no_of_children < 3 else 3
    result += str(no_child)
    return result 

def home(request):       
    return render(request,'pajak/home.html')

def calculate(request): 
        if request.method == 'POST': 
            form = PajakForm(request.POST)
            if form.is_valid(): 
                marriage_status = form.cleaned_data['marriage']
                print(marriage_status)
                no_of_children = form.cleaned_data['no_of_children']
                income = form.cleaned_data['income']
                category = get_category(marriage_status,no_of_children)
                cat_obj = Cat.objects.get(category=category)
                tier_pajak = Tier.objects.filter(cat=cat_obj.group,from_value__lt=income,to_value__gte=income)
                print(tier_pajak)
                context = {
                    'rate_pajak':tier_pajak[0].rate*100,
                    'total_pajak':tier_pajak[0].rate*income
                }
                return JsonResponse(context)
