from django.shortcuts import render


def visitor_register(request):

    context = {}
    return render(request, "registrar_visitante.html", context)
