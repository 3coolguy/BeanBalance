from django.shortcuts import render

# Create your views here.
def payment_action(request):
    return render(request, 'payment.html')