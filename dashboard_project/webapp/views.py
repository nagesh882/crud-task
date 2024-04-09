from app1.models import User
from django.shortcuts import render, redirect
from webapp.models import CRUD
from .forms import CRUDForm
from django.core.exceptions import ObjectDoesNotExist

def home_page(request):
    storeemail = request.session.get('enter_email')
    user_data = User.objects.filter(email=storeemail).first()
    context = {'data':user_data}
    return render(request, 'dashboard_templates/home.html', context)

def profile_page(request):
    storeemail = request.session.get('enter_email')
    user_data = User.objects.filter(email=storeemail).first()
    context = {'data':user_data}
    return render(request, 'dashboard_templates/profile.html',context)

def user_data(request):
    to_do_list = CRUD.objects.all().order_by('-id')
    storeemail = request.session.get('enter_email')
    user_data = User.objects.filter(email=storeemail).first()
    storeemail = request.session.get('enter_email')
    user_data = User.objects.filter(email=storeemail).first()
    return render(request, 'dashboard_templates/index.html', {'task_list':to_do_list, 'data':user_data})


def to_do_create_view(request):
    storeemail = request.session.get('enter_email')
    user_data = User.objects.filter(email=storeemail).first()
    if request.method == "POST":
        to_do_form = CRUDForm(request.POST)
        if to_do_form.is_valid():
            to_do_form.save()
            to_do_form = CRUDForm()
            return redirect('userdata')
    else:
        to_do_form = CRUDForm()
        
    return render(request, 'crud/to-do-add.html', {'form':to_do_form, 'data':user_data})


def to_do_update_view(request, slug):
    storeemail = request.session.get('enter_email')
    user_data = User.objects.filter(email=storeemail).first()
    try:
        if CRUD.objects.get(slug=slug):
            to_do_update = CRUD.objects.get(slug=slug)
            if request.method == 'POST':
                to_do_form = CRUDForm(request.POST, instance=to_do_update)
                if to_do_form.is_valid():
                    to_do_form.save()
                    return redirect('userdata')
            else:
                to_do_form = CRUDForm(instance=to_do_update)
                return render(request, 'crud/to-do-update.html', {'form':to_do_form,'to_do_update': to_do_update, 'data':user_data})
        else:
            to_do_update = CRUD.objects.get(slug=slug)
    except ObjectDoesNotExist:
            exception_error = ObjectDoesNotExist('404 Not Found!')
            return render(request, 'crud/to-do-update.html', {'exception_error':exception_error})
         

def to_do_delete_view(request, slug):
    task = CRUD.objects.get(slug=slug)
    task.delete()
    return redirect('userdata')

