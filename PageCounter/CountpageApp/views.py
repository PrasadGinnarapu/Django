from django.shortcuts import render

# Create your views here.
val = 0
price =0
def home(request):
    if request.method == 'POST':
        global val, price
        val += 1
        price = val*5
    return render(request, 'home.html', {'val':val, 'price':price})