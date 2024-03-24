from .models import Category, Course, Lesson, User, Tag
from rest_framework import serializers


class ImageSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField(source="image")

    def get_image(self, obj):
        request = self.context.get("request")
        if obj.image:
            if request:
                return request.build_absolute_uri("/static/%s" % obj.image.name)
            return "/static/%s" % obj.image.name

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ["id", "name"]


class CourseSerializer(ImageSerializer):
    tags = TagSerializer(many=True)
    category = CategorySerializer()


    class Meta:
        model = Course
        fields = '__all__'


class LessonSerializer(ImageSerializer):
    tags = TagSerializer(many=True)
    course = CourseSerializer()
    class Meta:
        model = Lesson
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        data = validated_data.copy()
        user = User(**data)
        user.set_password(data['password'])
        user.save()

        return user

    class Meta:
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }
        model = User
        fields = ['last_name', 'first_name', 'email', 'username', 'password', 'avatar']