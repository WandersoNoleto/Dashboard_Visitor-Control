from django.contrib import admin
from django.urls import path
from users.views import index
from visitors.views import visitor_register

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name = "Home"),
    path ("registrar-visitante/", visitor_register, name="registrar_visitante")
]
