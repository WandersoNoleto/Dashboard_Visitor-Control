from django.shortcuts import render
from visitors.models import Visitor


def index(request):

    all_visitors = Visitor.objects.all()

    context = {
        "page_name": "Home | Dashboard",
        "all_visitors": all_visitors

    }


    return render(request, "index.html", context)
