from django.urls import path
from . import views

urlpatterns = [
    path('patients/', views.PatientList.as_view(), name="patients"),
    path('patient/<int:pk>/', views.PatientDetail.as_view()),
    
]