from django.contrib import admin
from .models import Medicine, Symptom, Effect

# Register your models here.
admin.site.register(Medicine)
admin.site.register(Symptom)
admin.site.register(Effect)
