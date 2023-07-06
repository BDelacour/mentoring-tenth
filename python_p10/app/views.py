from rest_framework import viewsets, permissions

from python_p10.app.models import Contributor, Project, Issue, Comment
from python_p10.app.permissions import IsContributorOfProject, IsAuthor
from python_p10.app.serializers import ContributorSerializer, ProjectSerializer, IssueSerializer, CommentSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all().order_by('-created_time')
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_permissions(self):
        _permissions = super().get_permissions()
        if self.action in ["update", "partial_update", "destroy"]:
            _permissions.append(IsAuthor())
        return _permissions

    def create(self, request, *args, **kwargs):
        request.data['author'] = request.user.id
        return super().create(request, *args, **kwargs)


class ContributorViewSet(viewsets.ModelViewSet):
    queryset = Contributor.objects.all().order_by('-created_time')
    serializer_class = ContributorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_permissions(self):
        _permissions = super().get_permissions()
        if self.action in ["update", "partial_update", "destroy"]:
            _permissions.append(IsAuthor())
        return _permissions

    def create(self, request, *args, **kwargs):
        request.data['author'] = request.user.id
        return super().create(request, *args, **kwargs)


class IssueViewSet(viewsets.ModelViewSet):
    queryset = Issue.objects.all().order_by('-created_time')
    serializer_class = IssueSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_permissions(self):
        _permissions = super().get_permissions()
        if self.action in ["update", "partial_update", "destroy"]:
            _permissions.append(IsAuthor())
        elif self.action in ["create"]:
            _permissions.append(IsContributorOfProject())
        return _permissions

    def get_queryset(self):
        user_projects = [c.project for c in Contributor.objects.filter(user=self.request.user.id)]
        return Issue.objects.filter(project__in=user_projects)

    def create(self, request, *args, **kwargs):
        request.data['author'] = request.user.id
        return super().create(request, *args, **kwargs)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_time')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_permissions(self):
        _permissions = super().get_permissions()
        if self.action in ["update", "partial_update", "destroy"]:
            _permissions.append(IsAuthor())
        elif self.action in ["create"]:
            _permissions.append(IsContributorOfProject())
        return _permissions

    def get_queryset(self):
        user_projects = [c.project for c in Contributor.objects.filter(user=self.request.user.id)]
        return Comment.objects.select_related('issue').filter(issue__project__in=user_projects)

    def create(self, request, *args, **kwargs):
        request.data['author'] = request.user.id
        return super().create(request, *args, **kwargs)
