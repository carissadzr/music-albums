from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
def show_main(request):
    context = {
        'name': 'Manusia - Tulus',
        'amount': '10',
        'description':'This album represents the various dynamics of human emotions, including the spirit of preserving youth, amidst the fluctuations of the heart and feelings, followed by questions about life, self-appreciation, and a variety of emotions in celebrating life'
    }

    return render(request, "main.html", context)