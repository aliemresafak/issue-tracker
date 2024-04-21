from django.test import TestCase
from github.models import Repository, GithubUser, Issue
from datetime import datetime
import pytest
from rest_framework import status
from django.utils import timezone


@pytest.mark.django_db
class TestIssuesEndpoint(TestCase):
    def setUp(self):
        github_user = GithubUser.objects.create(username="test")
        self.repository = Repository.objects.create(
            name="test_repository",
            github_user=github_user
        )
        self.issue = Issue.objects.create(
            issue_id="1",
            title="test",
            state="Open",
            repository=self.repository,
            created_at=timezone.now(),
            updated_at=timezone.now()
        )

    def tearDown(self):
        self.repository.delete()
        self.issue.delete()

    def test_retrieve(self):
        response = self.client.get(f"/api/issues/{self.issue.pk}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.issue.title)

    def test_list(self):
        response = self.client.get("/api/issues/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
