from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import MedicineViewSet, SymptomViewSet, EffectViewSet, ConsulationView
router = SimpleRouter()

router.register("medicines", MedicineViewSet, basename="medicine")
router.register("symptoms", SymptomViewSet, basename="symptoms")
router.register("effects", EffectViewSet, basename="effects")

urlpatterns = router.urls + [
    path('consultation/', ConsulationView.as_view(), name='consultation'),
]