from django.db import models

from python_p10.authentication.models import User


class Project(models.Model):
    BACK_END = "BE"
    FRONT_END = "FE"
    IOS = "IOS"
    ANDROID = "AD"
    _type_choices = [
        (BACK_END, "Back-End"),
        (FRONT_END, "Front-End"),
        (IOS, "IOS"),
        (ANDROID, "Android"),
    ]

    created_time = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(to=User, related_name="project_author", on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True, default="")
    type = models.CharField(max_length=16, choices=_type_choices)


class Issue(models.Model):
    PRIORITY_LOW = "LOW"
    PRIORITY_MEDIUM = "MEDIUM"
    PRIORITY_HIGH = "HIGH"
    _priority_choices = [
        (PRIORITY_LOW, "Low"),
        (PRIORITY_MEDIUM, "Medium"),
        (PRIORITY_HIGH, "High"),
    ]

    TYPE_BUG = "BUG"
    TYPE_FEATURE = "FEATURE"
    TYPE_TASK = "TASK"
    _type_choices = [
        (TYPE_BUG, "Bug"),
        (TYPE_FEATURE, "Feature"),
        (TYPE_TASK, "Task"),
    ]

    STATUS_TODO = "TODO"
    STATUS_PROGRESS = "PROGRESS"
    STATUS_FINISHED = "FINISHED"
    _status_choices = [
        (STATUS_TODO, "To Do"),
        (STATUS_PROGRESS, "In Progress"),
        (STATUS_FINISHED, "Finished"),
    ]
    created_time = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(to=User, related_name="issue_author", on_delete=models.CASCADE)
    project = models.ForeignKey(to=Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True, default="")
    assignee = models.ForeignKey(to=User, null=True, on_delete=models.SET_NULL, default=None)
    priority = models.CharField(max_length=16, choices=_priority_choices)
    type = models.CharField(max_length=16, choices=_type_choices)
    status = models.CharField(max_length=16, choices=_status_choices, default=STATUS_TODO)


class Comment(models.Model):
    created_time = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(to=User, related_name="comment_author", on_delete=models.CASCADE)
    issue = models.ForeignKey(to=Issue, on_delete=models.CASCADE)
    uuid = models.CharField(max_length=36)
    description = models.TextField(blank=True, default="")


class Contributor(models.Model):
    created_time = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(to=User, related_name="contributor_author", on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    project = models.ForeignKey(to=Project, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'project'], name='unique')
        ]
