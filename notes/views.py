from django.shortcuts import render
from django.utils import timezone
from .models import Note

def note_list(request):
    notes = Note.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'notes/note_list.html',{'notes':notes})
