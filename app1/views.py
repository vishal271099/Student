from django.shortcuts import render, redirect
from .models import StudentDetail, GuardianDetail
from .serializer import (
    Studentserializer,
    Guardianserializer,
    AuthTokenSerializer,
    RegisterSerializer
)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.authentication import SessionAuthentication
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import login, logout
from rest_framework import status
from .serializer import AuthTokenSerializer
from .utils import Util
import email.message
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth import get_user_model
from rest_framework.renderers import TemplateHTMLRenderer
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMessage
from email.mime.text import MIMEText
from django.core.mail import EmailMultiAlternatives
from email.mime.multipart import MIMEMultipart
from .task import send_mail_task
from django.http import HttpResponse


UserModel = get_user_model()


class MyPageNumberPagination(PageNumberPagination):
    page_size = 10


class StudentList(ListAPIView):
    queryset = StudentDetail.objects.all()
    serializer_class = Studentserializer
    pagination_class = MyPageNumberPagination


class StudentAPI(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id=None):
        if id:
            student = StudentDetail.objects.get(id=id)
            serializer = Studentserializer(student)
            return Response(serializer.data)
        student = StudentDetail.objects.all()
        serializer = Studentserializer(student, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = Studentserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def put(self, request, id):
        student = StudentDetail.objects.get(id=id)
        serializer = Studentserializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id):
        student = StudentDetail.objects.get(id=id)
        student.delete()
        return Response(serializer.data)


class RegisterAPIView(APIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            login(request, user)
            send_mail_task.delay(user.id)
            return Response({"msg": "login successfully"}, status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class LoginAPIView(APIView):
    serializer_class = AuthTokenSerializer
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        serializer = AuthTokenSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data['user']
            login(request, user)
            return Response({"msg": "login successfully"}, status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class LogoutAPIView(APIView):

    serializer_class = AuthTokenSerializer

    def post(self, request):
        logout(request)
        data = {'success': 'Sucessfully logged out'}
        return Response(data=data, status=status.HTTP_200_OK)

def index(request):
    return HttpResponse("Helo")
