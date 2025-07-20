from django.urls import path
from django.shortcuts import redirect  # ✅ Add this import
from . import views

urlpatterns = [
    path('', lambda request: redirect('generate')),  # ✅ Redirect root to /generate/
    path('generate/', views.share_location, name='generate'),
    path('view/<uuid:id>/', views.view_location, name='view_location'),
]
