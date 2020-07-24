from django.urls import path
from custom_handler.views import CreateStudentView

urlpatterns = [
    path('student/', CreateStudentView.as_view(), name='student_create'),
]
