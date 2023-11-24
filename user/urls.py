from django.urls import path, include
from . import views

urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path('join/', views.CustomRegisterView.as_view(), name='custom_register'),
    # path('join/', include('dj_rest_auth.registration.urls')),
]