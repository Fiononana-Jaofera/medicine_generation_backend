from rest_framework import generics
from medicine.models import Medicine, Symptom, Effect
from .serializers  import MedicineSerializer, SymptomSerializer, EffectSerializer

class MedicineAPIView( generics.ListAPIView ):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer

class MedicineDetail( generics.RetrieveAPIView ):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer

class SymptomAPIView( generics.ListAPIView ):
    queryset = Symptom.objects.all()
    serializer_class = SymptomSerializer

class SymptomDetail( generics.RetrieveAPIView ):
    queryset = Symptom.objects.all()
    serializer_class = SymptomSerializer

class EffectAPIView( generics.ListAPIView ):
    queryset = Effect.objects.all()
    serializer_class = EffectSerializer

class EffectDetail( generics.RetrieveAPIView ):
    queryset = Effect.objects.all()
    serializer_class = EffectSerializer
