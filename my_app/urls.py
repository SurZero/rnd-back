from django.urls import path

from .views import PatientFormCreateApiView, UpdatePsitionsAPIView, PatientFormCreateApiView

urlpatterns = [
    path('create/', PatientFormCreateApiView.as_view(), name='create'),
    path('update-positions/', UpdatePsitionsAPIView.as_view(), name='update'),
    path('positions/', PatientFormCreateApiView.as_view(), name='positions'),
]
