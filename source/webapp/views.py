from django.shortcuts import render


def IndexView(request):
    if request.method == 'GET':
        return render(request, 'index.html')
