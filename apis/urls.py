from django.urls import path
from .views import MedicineAPIView, MedicineDetail, SymptomAPIView, SymptomDetail, EffectAPIView, EffectDetail

urlpatterns = [
    path("medicines/", MedicineAPIView.as_view(), name="medicine_list"),
    path("medicines/<int:pk>/", MedicineDetail.as_view(), name="medicine_detail"),
    path("symptoms/", SymptomAPIView.as_view(), name="symptom_list"),
    path("symptoms/<int:pk>/", SymptomDetail.as_view(), name="symptom_detail"),
    path("effects/", EffectAPIView.as_view(), name="effect_list"),
    path("effects/<int:pk>/", EffectDetail.as_view(), name="effect_detail")
]