from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406423401',
        'name': 'Fitto Fadhelli Voltanie Ariyana',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)