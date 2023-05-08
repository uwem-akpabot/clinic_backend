from rest_framework import serializers
from . import models

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Patient
        fields = ['id', 'fname', 'sname', 'gender', 'address', 'phone', 'email', 'contact_person', 
            'contact_person_phone', 'updated', 'created']