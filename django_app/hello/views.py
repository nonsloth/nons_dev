from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Profile
# from .forms import HelloForm
from .forms import ProfileForm
from .forms import FindForm
from django.db.models import Q

def index(request):
    data = Profile.objects.all()
    params = {
        'title': 'Hello/INDEX',
        'data': data,
        'goto': 'create',
    }
    return render(request, 'hello/index.html', params)

# create model
def create(request):
    if (request.method == 'POST'):
        obj = Profile()
        profile = ProfileForm(request.POST, instance=obj)
        profile.save()
        return redirect(to='/hello')
    params = {
        'title': 'Hello/CREATE',
        'form': ProfileForm(),
        'goto': 'index',
    }
    
    return render(request, 'hello/create.html', params)

# edit model
def edit(request, num):
    obj = Profile.objects.get(id=num)
    if (request.method == 'POST'):
        profile = ProfileForm(request.POST, instance=obj)
        profile.save()
        return redirect(to='/hello')
    params = {
        'title': 'Hello/EDIT',
        'id': num,
        'form': ProfileForm(instance=obj),
        'goto': 'index',
    }
    
    return render(request, 'hello/edit.html', params)

# delete model
def delete(request, num):
    profile = Profile.objects.get(id=num)
    if (request.method == 'POST'):
        profile.delete()
        return redirect(to='/hello')
    params = {
        'title': 'Hello/DELETE',
        'id': num,
        'obj': profile,
        'goto': 'index',
    }
    
    return render(request, 'hello/delete.html', params)

def find(request):
    if (request.method == 'POST'):
        msg = 'search result:'
        form = FindForm(request.POST)
        str = request.POST['find']
        list = str.split()
        data = Profile.objects.filter(profile_name__in=list)
    else:
        msg = 'search words...'
        form = FindForm()
        data = Profile.objects.all()
    params = {
        'title': 'Hello/SEARCH',
        'message': msg,
        'form': form,
        'data': data,
        'goto': 'index',
    }
    return render(request, 'hello/find.html', params)