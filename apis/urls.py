from django.urls import path
from .views import MedicineList, MedicineDetail, SymptomDetail, SymptomList, EffectList, EffectDetail, CombineDataView

urlpatterns = [
    path("medicines/<int:pk>/", MedicineDetail.as_view(), name="medicine_detail"),
    path("medicines/", MedicineList.as_view(), name="medicine_list"),
    path("symptoms/<int:pk>/", SymptomDetail.as_view(), name="symptom_detail"),
    path("symptoms/", SymptomList.as_view(), name="symptom_list"),
    path("effects/<str:pk>/", CombineDataView.as_view(), name="effects_detail"),
    path("effects/", CombineDataView.as_view(), name="effects_list"),
]