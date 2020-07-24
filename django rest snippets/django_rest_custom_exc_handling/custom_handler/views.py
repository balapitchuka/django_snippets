from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.serializers import ErrorDetail
from custom_handler.serializers import StudentSerializer

# Create your views here.
class CreateStudentView(APIView):

    def post(self, request):
        student_data = StudentSerializer(data=request.data)
        if student_data.is_valid():
            pass
        else:
            response_data = {
                "code" : status.HTTP_400_BAD_REQUEST,
                "message" : "Invalid Data, Validation Failed",
                "details" : {

                }
            }
            for key, value in student_data.errors.items():
                response_data["details"][key] = " ".join(value)
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)