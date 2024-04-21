from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin

from api.github.serilalizers import GithubRepositorySerializer, IssueSerializer
from github.models import Repository, Issue


class RepositoryViewSet(GenericViewSet, ListModelMixin):
    queryset = Repository.objects.all()
    serializer_class = GithubRepositorySerializer


class IssueViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
