from rest_framework import serializers

from medicine.models import Medicine, Symptom, Effect

class MedicineSerializer( serializers.ModelSerializer ):
    class Meta:
        model = Medicine
        fields = ["id","name", "price"]


class SymptomSerializer( serializers.ModelSerializer ):
    class Meta:
        model = Symptom
        fields = ["id","name"]

class EffectSerializer( serializers.ModelSerializer ):
    class Meta:
        model = Effect
        fields = ["id", "medicine","symptom","effect"]    