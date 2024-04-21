from django.db import models
from simple_history.models import HistoricalRecords


class BaseDatetime(models.Model):
    timestamp_created = models.DateTimeField(
        auto_now_add=True,
        help_text="This field stores the time when the record was created.",
        db_comment="This field stores the time when the record was created."
    )
    timestamp_updated = models.DateTimeField(
        auto_now=True,
        help_text="This field stores the time when the record was last updated.",
        db_comment="This field stores the time when the record was last updated."
    )

    class Meta:
        abstract = True


class GithubUser(BaseDatetime):
    username = models.CharField(max_length=255)

    def __str__(self):
        return self.username


class Repository(BaseDatetime):
    name = models.CharField(max_length=255)
    github_user = models.ForeignKey(GithubUser, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Repositories"

    def __str__(self):
        return f"{self.github_user} / {self.name}"


class Issue(BaseDatetime):
    issue_id = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    repository = models.ForeignKey(Repository, on_delete=models.CASCADE, related_name="issues")
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history = HistoricalRecords()

    def update(self, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)
        return self.save()

    def __str__(self):
        return self.title
