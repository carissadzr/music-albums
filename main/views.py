from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Carissa Aida Zahra',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)