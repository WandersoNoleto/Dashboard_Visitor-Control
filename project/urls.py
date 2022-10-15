from apps.dashboard.views import index
from apps.visitors.views import visit_completed, visitor_info, visitor_register
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/", 
        auth_views.LoginView.as_view(
            template_name="login.html"
        ), name="Login"
    ),
    path("logout/",
        auth_views.LogoutView.as_view(
            template_name="logout.html"
        ), name="Logout"
    ),
    path("", index, name = "Home"),
    path ("registrar-visitante/", visitor_register, name="visitor_register"),
    path("visitantes/<int:id>/", visitor_info, name="visitor_info"),
    path("visitantes/<int:id>/finalizar/", visit_completed, name="visit_completed")
]
