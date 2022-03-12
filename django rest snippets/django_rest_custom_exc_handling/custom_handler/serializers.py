from rest_framework import serializers


class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name =  serializers.CharField()
    date_of_birth = serializers.DateField()

    def validate_date_of_birth(self, dob):
        raise serializers.ValidationError("You are not eligible for the task")
        

    