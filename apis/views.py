from rest_framework import generics, response, views
from medicine.models import Medicine, Symptom, Effect
from .serializers  import MedicineSerializer, SymptomSerializer, EffectSerializer
from .algo import *

# class EffectViewSet( viewsets.ModelViewSet ):
#     queryset = Effect.objects.all()
#     serializer_class = EffectSerializer

class MedicineList(generics.ListCreateAPIView):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer
class MedicineDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer

class SymptomList(generics.ListCreateAPIView):
    queryset = Symptom.objects.all()
    serializer_class = SymptomSerializer
class SymptomDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Symptom.objects.all()
    serializer_class = SymptomSerializer

class EffectView( views.APIView ):
    def get( self, request ):
        medicines = Medicine.objects.raw(f"SELECT name FROM {Medicine._meta.db_table}")
        symptoms = Symptom.objects.raw(f"SELECT name FROM {Symptom._meta.db_table}")
        m_e_data = Effect.objects.raw(f"SELECT id, effect FROM {Effect._meta.db_table}")

# class ConsulationView ( views.APIView ):
#     def post(self, request):

#         s = request.data
#         s = sort_dict_by_key(s)
#         s = list(s.values())

#         m_p_data = Medicine.objects.raw(f"SELECT name, price FROM {Medicine._meta.db_table}")
#         m_e_data = Effect.objects.raw(f"SELECT id, effect FROM {Effect._meta.db_table}")

#         # s_data = Symptom.objects.raw(f"SELECT name FROM {Symptom._meta.db_table}")
#         # symptom = []
#         # for m in s_data:
#         #     symptom.append(m.name)
#         # symptom.sort()

#         m_p = {}
#         for m in m_p_data:
#             m_p.update({m.name: m.price})

#         m_e = {m.name: {} for m in m_p_data}
#         for m in m_e_data:
#             m_e[m.medicine.name].update({m.symptom.name: m.effect})
#             m_e[m.medicine.name] = sort_dict_by_key(m_e[m.medicine.name])

#         for k, v in m_e.items():
#             m_e[k] = list(v.values())


#         cas_possible = allwords(m_e, [], [], sum(s), s)
#         liste_prix = calcul_prix(cas_possible, m_p)
#         prix_minimal = min(liste_prix)
#         index_liste_optimale = liste_prix.index(prix_minimal)
#         liste_optimale = cas_possible[index_liste_optimale]


#         return response.Response({"liste optimale": liste_optimale, "prix minimal": prix_minimal})