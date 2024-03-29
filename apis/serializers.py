from rest_framework import serializers

from medicine.models import Medicine, Symptom, Effect

class MedicineSerializer( serializers.ModelSerializer ):
    class Meta:
        model = Medicine
        fields = ["name", "price"]


class SymptomSerializer( serializers.ModelSerializer ):
    class Meta:
        model = Symptom
        fields = ["name"]

class EffectSerializer( serializers.ModelSerializer ):
    class Meta:
        model = Effect
        fields = ["id", "medicine","symptom","effect"]