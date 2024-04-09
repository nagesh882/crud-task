from django.shortcuts import render, redirect
from app1.models import User
from app1.forms import UserRegistration
from django.contrib import messages
import random
from django.core.mail import send_mail
from django.contrib.auth import logout



def generate_otp():
    return str(random.randint(100000, 999999))

def sign_up(request):
    if request.method == 'POST':
        sign_up_form = UserRegistration(request.POST)
        if sign_up_form.is_valid():
            firstname = sign_up_form.cleaned_data['first_name']
            lname = sign_up_form.cleaned_data['last_name']
            mnumber = sign_up_form.cleaned_data['mobile']
            emailid = sign_up_form.cleaned_data['email']
            
            if User.objects.filter(email=emailid).first():
                messages.warning(request, 'This Email already exists !!!')
                return redirect('signup')
            
            user_data = User(first_name = firstname, last_name=lname, mobile=mnumber, email=emailid
            )
            user_data.save()
            messages.success(request, 'User Register Successfully !!!')
            return redirect('login')
    else:
        sign_up_form = UserRegistration()
    return render(request, 'login_templates/sign-up.html', {'form':sign_up_form})


def login(request):
    if request.method == 'POST':
        enter_email = request.POST.get('enter_email')

        try:
            user = User.objects.get(email=enter_email)
        except User.DoesNotExist:
            messages.warning(request, 'Please enter valid email!')
            return redirect('login')

        OTP = generate_otp()
        email_subject = 'This Message For OTP Authentication'
        email_message =  f'Use the following One Time Password(OTP) for Login.....\n\n{OTP}'
        send_mail(
            email_subject,
            email_message,
            '{{user_email}}',
            [enter_email],
            fail_silently=False,
        )

        request.session['OTP'] = OTP
        request.session['enter_email'] = enter_email

        return redirect('otp_verify')

    return render(request,'login_templates/login.html')


def otp_verify(request):
    if request.method == "POST":
        user_entered_otp = request.POST.get('otp')
        email_store = request.session.get('enter_email')
        print(email_store)
        stored_otp = request.session.get('OTP')

        if user_entered_otp == stored_otp :
            data = User.objects.filter(email=email_store)
            return redirect('home')
        else:
            messages.warning(request, 'Please enter valid OTP!')
            return redirect('otp_verify')

    return render(request, 'login_templates/otp-verify.html')

def logout_page(request):
    logout(request)
    return redirect('login')