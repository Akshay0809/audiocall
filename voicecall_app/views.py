
from django.shortcuts import render, redirect
import random
import string

def generate_pin():
    return ''.join(random.choices(string.digits, k=6))

def index(request):
    if request.method == 'POST':
        if 'generate' in request.POST:
            pin_code = generate_pin()
            return render(request, 'voicecall_app/call.html', {'pin_code': pin_code})
        elif 'join' in request.POST:
            pin_code = request.POST.get('pin_code')
            return redirect('call', pin_code=pin_code)
    return render(request, 'voicecall_app/main.html')

def call(request, pin_code):
    return render(request, 'voicecall_app/call.html', {'pin_code': pin_code})
