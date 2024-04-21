from django.contrib import admin
from .models import Repository, GithubUser, Issue


@admin.register(Repository)
class RepositoryAdmin(admin.ModelAdmin):
    list_display = ("name", "github_user")


@admin.register(GithubUser)
class GithubUserAdmin(admin.ModelAdmin):
    list_display = ("username",)


@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    list_display = ("issue_id", "title", "state", "repository")

    readonly_fields = ("issue_id",)
