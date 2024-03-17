from rest_framework.serializers import ModelSerializer

from .models import Course, Category


class CateSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'created_date', 'updated_date']


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        exclude = ('tags',)