from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View

from .models import Category, Course
from rest_framework import viewsets, generics
from .serializers import CateSerializer, CourseSerializer
from .paginator import CourseSetPagination

# Create your views here.


class CateViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CateSerializer


class CourseViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    pagination_class = CourseSetPagination


class CategoryView(View):

    def get(self, request):
        cats = Category.objects.all()
        return render(request, 'courses/list.html', {
            'categories': cats
        })

    def post(self, request):
        pass

def index(request):
    return HttpResponse('HELLO CS2001')

def list(request, course_id):
    return HttpResponse(f'COURSE {course_id}')
