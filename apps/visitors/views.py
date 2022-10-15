from curses.ascii import HT

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotAllowed
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from visitors.forms import VisitorForm, VisitorFormAuthorized
from visitors.models import Visitor


@login_required
def visitor_register(request):
    form = VisitorForm()

    if request.method == "POST":
        form = VisitorForm(request.POST)

        if form.is_valid():
            visitor = form.save(commit=False)

            visitor.concierge = request.user.concierge
            visitor.save()

            messages.success(
                request,
                "Visitante registrado com sucesso"
            )

            return redirect("Home")



    context = {
        "page_name": "Registrar visitante",
        "form": form
    }

    return render(request, "visitor_register.html", context)


@login_required
def visitor_info(request, id):

    visitor = get_object_or_404(
        Visitor,
        id=id
    )

    form = VisitorFormAuthorized()

    if request.method == "POST":
        form = VisitorFormAuthorized(
        request.POST,
        instance=visitor
        )
        if form.is_valid():
            visitor = form.save(commit=False)

            visitor.status = "EM_VISITA"
            visitor.authorization_time = timezone.now()

            visitor.save()

            messages.success(
                request, "Entrada de visitante autorizada"
            )
            return redirect("Home")

    context = {
        "page_name": "Informações de visitante",
        "visitor": visitor,
        "form": form
    }

    return render(request, "visitor_info.html", context)

@login_required
def visit_completed(request, id):

    if request.method == "POST":
        visitor = get_object_or_404(
            Visitor,
            id=id
        )

        visitor.status = "FINALIZADO"
        visitor.departure_time = timezone.now()

        visitor.save()

        messages.success(
            request,
            "Visita finalizada com sucesso"
        )

        return redirect("Home")
    
    else:
        return HttpResponseNotAllowed(
            ["POST"],
            "Método não permitido"
        )


