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
        m_p_data = Medicine.objects.raw(f"SELECT name, price FROM {Medicine._meta.db_table}")
        m_e_data = Effect.objects.raw(f"SELECT id, effect FROM {Effect._meta.db_table}")
        m_s_data = Symptom.objects.raw(f"SELECT name FROM {Symptom._meta.db_table}")
        m_p = {}
        for m in m_p_data:
            m_p.update({m.name: m.price})

        m_e = {m.name: {} for m in m_p_data}
        for m in m_e_data:
            m_e[m.medicine.name].update({m.symptom.name: m.effect})

        print(m_e)


        return response.Response(m_p)