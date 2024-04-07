from rest_framework import generics, response, views
from medicine.models import Medicine, Symptom, Effect
from .serializers  import MedicineSerializer, SymptomSerializer, EffectSerializer
from .algo import *

# class EffectViewSet( viewsets.ModelViewSet ):
#     queryset = Effect.objects.all()
#     serializer_class = EffectSerializer

class MedicineList( generics.ListCreateAPIView ):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer
class MedicineDetail( generics.RetrieveUpdateDestroyAPIView ):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer

class SymptomList( generics.ListCreateAPIView ):
    queryset = Symptom.objects.all()
    serializer_class = SymptomSerializer
class SymptomDetail( generics.RetrieveUpdateDestroyAPIView ):
    queryset = Symptom.objects.all()
    serializer_class = SymptomSerializer

class EffectList( generics.ListCreateAPIView ):
    queryset = Effect.objects.all()
    serializer_class = EffectSerializer
class EffectDetail( generics.RetrieveUpdateDestroyAPIView ):
    queryset = Effect.objects.all()
    serializer_class = EffectSerializer

class CombineDataView( views.APIView ):
    def get( self, request ):
        medicines_data = Medicine.objects.all()
        symptoms_data = Symptom.objects.all()
        effects_data = Effect.objects.all()

        if len(effects_data) == 0:
            for m in medicines_data:
                for s in symptoms_data:
                    e = Effect(medicine=m, symptom=s, effect=0)
                    e.save()
        elif len(effects_data) != (len(medicines_data) * len(symptoms_data)):
            container = list(effects_data.values("medicine_id", "symptom_id"))
            for m in medicines_data:
                for s in symptoms_data:
                    if {'medicine_id': m.id, 'symptom_id': s.id} in container:
                        continue
                    else:
                        e = Effect(medicine=m, symptom=s, effect=0)
                        e.save()

        container = list(effects_data.values())
        for c in container:
            c['medicine_id'] = Medicine.objects.raw(f"SELECT id, name FROM {Medicine._meta.db_table} WHERE id={c['medicine_id']}")[0].name
            c['symptom_id'] = Symptom.objects.raw(f"SELECT id, name FROM {Symptom._meta.db_table} WHERE id={c['symptom_id']}")[0].name

        return response.Response(container)

        


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