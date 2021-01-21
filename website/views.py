from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import send_mail

# Create your views here.
def home(request):
    
    if request.method =="POST" and request.is_ajax(): 
        name_form = request.POST['name_form']
        email_form = request.POST['email_form']
        message_form = request.POST['message_form']
        
        # send an email

        send_mail(name_form ,message_form,email_form,['ricardo9285@gmail.com'])

        return JsonResponse({"name_form":name_form}, status=200)
        return render(request, 'home.html', {"name_form" : name_form})
        
    else:
        return render(request, 'home.html',{})
    
    return render(request, 'home.html',{})

def contact(request):
    print("contacto")
  
        

    
