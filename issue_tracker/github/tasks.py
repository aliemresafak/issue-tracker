from .models import Repository, Issue
from celery import shared_task
import httpx
import os
from django.core.mail import send_mail
def test_send_email(issue: Issue):
    send_mail(
        f"[{issue.issue_id}] {issue.title}",
        f"{issue.title} named issue changed",
        "info@issuetracker.com",
        ["test@gmail.com"]
    )
def pull_issues_for_repo(repo: Repository):
    url = f"https://api.github.com/repos/{repo.github_user}/{repo.name}/issues"
    headers = {}
    if os.environ.get("GITHUB_TOKEN"):
        headers = {
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {os.environ.get('GITHUB_TOKEN')}",
            "X-GitHub-Api-Version": "2022-11-28"
        }
    response = httpx.get(url=url, headers=headers)
    if response.status_code == 200:
        for github_issue in response.json():
            issue = Issue.objects.filter(issue_id=github_issue["id"]).first()
            if issue:
                if issue.updated_at.strftime("%Y-%m-%dT%H:%M:%SZ") != github_issue["updated_at"]:
                    issue.update(
                        title=github_issue["title"],
                        state=github_issue["state"],
                        created_at=github_issue["created_at"],
                        updated_at=github_issue["updated_at"]
                    )
                    issue.save()
                    test_send_email(issue)
                else:
                    print(f"[{issue}] issue'da herhangi bir degisiklik olmadi")
            else:
                issue = Issue.objects.create(
                    issue_id=github_issue["id"],
                    title=github_issue["title"],
                    state=github_issue["state"],
                    created_at=github_issue["created_at"],
                    updated_at=github_issue["updated_at"],
                    repository=repo
                )
                issue.save()
                test_send_email(issue)
    else:
        print("A error = ", response.text)


@shared_task
def get_issues():
    repositories = Repository.objects.all()
    for repository in repositories:
        pull_issues_for_repo(repository)