from django.shortcuts import get_object_or_404
from rest_framework import permissions

from python_p10.app.models import Issue, Comment, Contributor


class IsAuthor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.author


class IsContributorOfProject(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action not in ["create"]:
            return False
        _project = None
        if 'project' in request.data:
            _project = request.data['project']
        if 'issue' in request.data:
            issue = get_object_or_404(Issue, pk=request.data['issue'])
            _project = issue.project.id
        if _project is None:
            return True  # Body is malformed
        return Contributor.objects.filter(user=request.user.id, project=_project).exists()

    def has_object_permission(self, request, view, obj):
        _obj = obj
        if isinstance(_obj, Comment):
            _obj = obj.issue
        if isinstance(_obj, Issue):
            project = _obj.project
            return Contributor.objects.filter(user=request.user.id, project=project.id).exists()
        return False
