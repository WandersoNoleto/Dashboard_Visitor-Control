from django.contrib import messages
from django.shortcuts import redirect, render

from visitors.forms import VisitorForm


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

    return render(request, "registrar_visitante.html", context)
