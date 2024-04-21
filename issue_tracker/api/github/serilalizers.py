from rest_framework import serializers
from github.models import Repository, Issue, GithubUser


class GithubUserSerializer(serializers.RelatedField):
    def to_representation(self, value: GithubUser):
        return value.username


class IssueHistoricalRecordField(serializers.ListField):
    child = serializers.DictField()

    def to_representation(self, data):
        return super().to_representation(data.values())


class IssueSerializer(serializers.ModelSerializer):
    history = IssueHistoricalRecordField(read_only=True)

    class Meta:
        model = Issue
        fields = ("issue_id", "title", "state", "created_at", "updated_at", "history")


class GithubRepositorySerializer(serializers.ModelSerializer):
    github_user = GithubUserSerializer(read_only=True)
    issues = IssueSerializer(many=True)

    class Meta:
        model = Repository
        fields = ("name", "github_user", "issues")
