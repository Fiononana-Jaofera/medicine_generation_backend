from django.db import models

class Medicine( models.Model ):
    name = models.CharField(max_length=100, primary_key=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.name
    

class Symptom( models.Model ):
    name = models.CharField(max_length=100, primary_key=True)
    medicine = models.ManyToManyField(Medicine, through="Effect")
    def __str__(self):
        return self.name
    

class Effect( models.Model ):
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    symptom = models.ForeignKey(Symptom, on_delete=models.CASCADE)
    effect = models.PositiveIntegerField()
    
    class Meta:
        unique_together = ('medicine', 'symptom')

    def __str__(self):
        return str(self.medicine) + ' - ' + str(self.symptom)