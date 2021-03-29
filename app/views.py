from django.shortcuts import render
from .models import Customer,Product,Cart,OrderPlaced
from django.views import View
# def home(request):
#  return render(request, 'app/home.html')
class ProductView(View):
    def get(self,request):
        gold=Product.objects.filter(category='G')
        silver=Product.objects.filter(category='S')
        platinum=Product.objects.filter(category='P')
        return render(request, 'app/home.html',{'gold':gold,'silver':silver,'platinum':platinum})


# def product_detail(request):
#  return render(request, 'app/productdetail.html')

class ProductDetailView(View):
    def get(self,request,pk):
        product=Product.objects.get(pk=pk)
        return render(request, 'app/productdetail.html',{'product':product})

def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

def gold(request,price=None):
    if price == None:
        gold=Product.objects.filter(category='G')
    elif price == '100':
        gold=Product.objects.filter(category='G').filter(discounted_price__lte=100)
    elif price == '300':
        gold=Product.objects.filter(category='G').filter(discounted_price__lte=300).filter(discounted_price__gte=100)
    elif price == '500':
        gold=Product.objects.filter(category='G').filter(discounted_price__lte=500).filter(discounted_price__gte=300)
    elif price == 'above500':
        gold=Product.objects.filter(category='G').filter(discounted_price__gte=500)

        

    return render(request, 'app/gold.html',{'gold':gold})

def silver(request,price=None):
    if price == None:
        silver=Product.objects.filter(category='S')
    elif price == '100':
        silver=Product.objects.filter(category='S').filter(discounted_price__lte=100)
    elif price == '300':
        silver=Product.objects.filter(category='S').filter(discounted_price__lte=300).filter(discounted_price__gte=100)
    elif price == '500':
        silver=Product.objects.filter(category='S').filter(discounted_price__lte=500).filter(discounted_price__gte=300)
    elif price == 'above500':
        silver=Product.objects.filter(category='S').filter(discounted_price__gte=500)

        

    return render(request, 'app/silver.html',{'silver':silver})

def login(request):
 return render(request, 'app/login.html')

def customerregistration(request):
 return render(request, 'app/customerregistration.html')

def checkout(request):
 return render(request, 'app/checkout.html')
