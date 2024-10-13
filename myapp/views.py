from django.shortcuts import render

# Create your views here.
def random_number_page(request):
    return render(request, 'random_number.html')