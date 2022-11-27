from django.shortcuts import render, redirect
from .models import Member

# Create your views here.

def bebidas(request):
    return render(request, 'crud/bebidas.html')

def evento(request):
    return render(request, 'crud/evento.html')

def local(request):
    return render(request, 'crud/local.html')

def index(request):
    return render(request, 'crud/index.html')



def participantes(request):
    members = Member.objects.all()
    context = {'members': members}
    return render(request, 'crud/participantes.html', context)

def create(request):
    member = Member(firstname=request.POST['firstname'], lastname=request.POST['lastname'])
    member.save()
    return redirect('/crud/participantes.html')

def edit(request, id):
    members = Member.objects.get(id=id)
    context = {'members': members}
    return render(request, 'crud/edit.html', context)

def update(request, id):
    member = Member.objects.get(id=id)
    member.firstname = request.POST['firstname']
    member.lastname = request.POST['lastname']
    member.save()
    return redirect('/crud/participantes.html')

def delete(request, id):
    member = Member.objects.get(id=id)
    member.delete()
    return redirect('/crud/participantes.html')