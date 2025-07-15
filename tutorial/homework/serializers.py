from rest_framework import serializers

from .models import Student, Teacher

class StudentSerializer(serializers.ModelSerializer):
    teacher_name = serializers.CharField(source='teacher.name', read_only=True)
    teacher_subject = serializers.CharField(source='teacher.subject', read_only=True)

    class Meta:
        model = Student
        fields = ('id', 'name', 'teacher', 'teacher_name', 'teacher_subject')


class TeacherSerializer(serializers.ModelSerializer):
    # students = StudentSerializer(source='student_set', many=True, read_only=True)
    class Meta:
        model = Teacher
        fields = '__all__'