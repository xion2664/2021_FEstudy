from first.models import First
from django.shortcuts import render

# Create your views here.


def home(request):
    firsts = First.objects.all()
    search_text = request.GET.get('search_text')
    if search_text:
        firsts = firsts.filter(title__icontains=search_text)
        return render(request, 'home.html', {'firsts': firsts})

    return render(request, 'home.html', {'firsts': firsts})
