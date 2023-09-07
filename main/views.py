from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Clement Samuel Marly',
        'class': 'PBP C',
        'appname': 'Game Stock'
    }

    return render(request, "main.html", context)
