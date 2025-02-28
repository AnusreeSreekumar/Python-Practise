from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def product_list(request):
    """_summary_
    returns product list page   
    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    return render(request, 'products.html')

def product_details(request):
    return render(request, 'product_details.html')
