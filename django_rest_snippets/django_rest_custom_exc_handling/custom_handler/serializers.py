from rest_framework import serializers


class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name =  serializers.CharField()
    date_of_birth = serializers.DateField()
    
    