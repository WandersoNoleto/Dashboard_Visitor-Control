from django.shortcuts import render


def index(request):

    context = {
        "page_name": "Home | Dashboard",

    }


    return render(request, "index.html", context)
