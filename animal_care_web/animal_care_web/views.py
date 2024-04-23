from django.shortcuts import render


def main(request):
    return render(request, 'home.html')

def disease_information(request):
    return render(request, 'disease_information.html')