from django.shortcuts import redirect, render, get_object_or_404 
from .models import Scrap

# Create your views here.
def main(request) :
    return render(request, 'main.html')

def hobby(request) :
    return render(request, 'hobby.html')

def place(request) :
    return render(request, 'place.html')

def music(request) :
    return render(request, 'music.html')

def photo(request) :
    return render(request, 'photo.html' )

def scrap(request) :
    scraps = Scrap.objects.all()
    return render(request, 'scrap.html', {'scraps': scraps})

def detail(request, yeram_id) :
    details = get_object_or_404(Scrap, pk= yeram_id )
    return render(request, 'detail.html', {'details': details})

def new(request) : 
    return render(request, 'new.html' )

def create(request) : #입력받은 내용을 DB에 넣어주는 함수
    scrap = Scrap()
    scrap.title = request.POST['title']
    scrap.author = request.POST['author']
    scrap.body = request.POST['body']
    scrap.save()
    return redirect('detail', scrap.id)

def edit(request, yeram_id) : 
    edit = Scrap.objects.get(id= yeram_id)
    return redirect('/scrap/'+str(scrap.id)+'/edit/',{'edit':edit})


def update(request, yeram_id) :
    update = Scrap.objects.get(id= yeram_id)
    update.title = request.POST['title']
    update.author = request.POST['author']
    update.body = request.POST['body']
    update.save()
    return redirect('/scrap/'+str(scrap.id)+'/update/',{'update':update})

def delete(request, yeram_id):
    delete = Scrap.objects.get(id=yeram_id)
    delete.delete()
    return redirect('scrap')
