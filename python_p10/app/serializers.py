import uuid

from django.db import transaction
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from python_p10.app.models import Contributor, Project, Issue, Comment


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

    @transaction.atomic
    def create(self, validated_data):
        project = super().create(validated_data)
        contributor = Contributor()
        contributor.author = project.author
        contributor.user = project.author
        contributor.project = project
        contributor.save()
        return project


class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    uuid = serializers.CharField(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'

    def create(self, validated_data):
        validated_data['uuid'] = str(uuid.uuid4())
        return super().create(validated_data)


class ContributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributor
        fields = '__all__'
        validators = [
            UniqueTogetherValidator(
                queryset=Contributor.objects.all(),
                fields=['user', 'project']
            )
        ]
