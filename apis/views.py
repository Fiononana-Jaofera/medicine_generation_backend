from rest_framework import viewsets, views, response
from medicine.models import Medicine, Symptom, Effect
from .serializers  import MedicineSerializer, SymptomSerializer, EffectSerializer

class MedicineViewSet( viewsets.ModelViewSet ):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer

class SymptomViewSet( viewsets.ModelViewSet ):
    queryset = Symptom.objects.all()
    serializer_class = SymptomSerializer

class EffectViewSet( viewsets.ModelViewSet ):
    queryset = Effect.objects.all()
    serializer_class = EffectSerializer

class ConsulationView ( views.APIView ):
    def post(self, request):

        data = request.data
        medicine_fields = Medicine.objects.raw("SELECT name, price from medicine_medicine")
        for p in medicine_fields:
            print(p.name, p.price)

        message = "operation performed successfully"

        return response.Response({'message': message})