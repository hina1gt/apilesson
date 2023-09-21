from rest_framework import serializers
from app.models import *
from study.models import *

class CafeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cafe
        fields = '__all__'

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'

class StudyCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyCenter
        fields = '__all__'

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

class StudentrSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'