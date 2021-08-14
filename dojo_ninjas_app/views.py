from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def index(request):
    context = {
                'dojos':  Dojo.objects.all(),
                'ninjas': Ninja.objects.all()
              }
    return render(request, 'index.html', context)


def add_a_dojo(request):
    Dojo.objects.create(
                      name=request.POST['dojo_name'],
                      city=request.POST['dojo_city'],
                      state=request.POST['dojo_state']
                    )
    return redirect('/')


def add_a_ninja(request):
    dojo = Dojo.objects.get(id=request.POST['ninja_dojo'])
    Ninja.objects.create(
                      dojo_id=dojo,
                      first_name=request.POST['ninja_first_name'],
                      last_name=request.POST['ninja_last_name']
                    )
    return redirect('/')


def delete_a_dojo(request, dojo_id):
    dojo = Dojo.objects.get(id=dojo_id)
    dojo.delete()
    return redirect('/')


def delete_a_ninja(request, ninja_id):
    ninja = Ninja.objects.get(id=ninja_id)
    ninja.delete()
    return redirect('/')
