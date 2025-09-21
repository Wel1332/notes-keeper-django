from django.shortcuts import render, redirect
from .models import Note

def home(request):
    notes = Note.objects.all().order_by('-created')
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        if title and content:
            Note.objects.create(title=title, content=content)
        return redirect('home')
    return render(request, 'notes/home.html', {'notes': notes})

def delete_note(request, note_id):
    Note.objects.get(id=note_id).delete()
    return redirect('home')
