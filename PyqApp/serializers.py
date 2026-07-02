from rest_framework import serializers
from .models import PYQ, Subject

class PaperSerializer(serializers.ModelSerializer):
    subject_id = serializers.IntegerField(source="subject.id")
    title = serializers.CharField(source="subject.title")
    semester = serializers.IntegerField(source="subject.semester")
    branch = serializers.CharField(source="subject.branch")
    code = serializers.CharField(source="subject.code")

    class Meta:
        model = PYQ
        fields = [
            "id",
            "subject_id",
            "title",
            "semester",
            "branch",
            "year",
            "code",
            "drive_link",
        ]

class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model=Subject
        fields=[
            "id",
            "title",
            "code"
        ]