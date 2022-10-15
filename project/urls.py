from django.contrib import admin
from django.urls import path
from users.views import index
from visitors.views import visit_completed, visitor_info, visitor_register

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name = "Home"),
    path ("registrar-visitante/", visitor_register, name="visitor_register"),
    path("visitantes/<int:id>/", visitor_info, name="visitor_info"),
    path("visitantes/<int:id>/finalizar/", visit_completed, name="visit_completed")
]
