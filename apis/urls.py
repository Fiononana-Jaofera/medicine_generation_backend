from django.urls import path
# from rest_framework.routers import SimpleRouter
from .views import MedicineList, MedicineDetail, SymptomDetail, SymptomList, EffectList, EffectDetail, CombineDataView
# router = SimpleRouter()

# router.register("medicines", MedicineViewSet, basename="medicine")
# router.register("symptoms", SymptomViewSet, basename="symptoms")
# router.register("effects", EffectViewSet, basename="effects")

# urlpatterns = router.urls + [
#     path('consultation/', ConsulationView.as_view(), name='consultation'),
# ]

urlpatterns = [
    path("medicines/<int:pk>/", MedicineDetail.as_view(), name="medicine_detail"),
    path("medicines/", MedicineList.as_view(), name="medicine_list"),
    path("symptoms/<int:pk>/", SymptomDetail.as_view(), name="symptom_detail"),
    path("symptoms/", SymptomList.as_view(), name="symptom_list"),
    path("effects_dev/<int:pk>/", EffectDetail.as_view(), name="effects_detail_dev"),
    path("effects_dev/", EffectList.as_view(), name="effects_list_dev"),
    path("effects/", CombineDataView.as_view(), name="effects_list"),
    path("effects/<str:pk>/", CombineDataView.as_view(), name="effects_detail"),
]