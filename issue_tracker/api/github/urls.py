from rest_framework.routers import SimpleRouter
from api.github.views import RepositoryViewSet, IssueViewSet

router = SimpleRouter()
router.register("repositories", RepositoryViewSet, basename="repository")
router.register("issues", IssueViewSet, basename="issue")
