import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from visitors.models import Visitor


@login_required
def index(request):

    all_visitors = Visitor.objects.order_by(
        "-arrival_time"
    )

    visitor_waiting = all_visitors.filter(
        status="AGUARDANDO"
    )

    visitor_in_visit = all_visitors.filter(
        status="EM_VISITA"
    )

    visit_finished = all_visitors.filter(
        status="FINALIZADO"
    )

    visitors_in_month = all_visitors.filter(
        arrival_time__month = datetime.date.today().month
    )

    context = {
        "page_name": "Home | Dashboard",
        "all_visitors": all_visitors,
        "visitor_waiting": visitor_waiting.count(), 
        "visitor_in_visit": visitor_in_visit.count(),
        "visit_finished": visit_finished.count(),
        "visitors_in_month": visitors_in_month.count()
    }


    return render(request, "index.html", context)
