from django.urls import path,include
from django.contrib.auth.views import LogoutView

app_name = "accounts"

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path('api/', include('accounts.api.urls')),
    path('logout/', LogoutView.as_view(), name='logout'),
]