from rest_framework.routers import DefaultRouter
from api.github.urls import router as repository_router

api_router = DefaultRouter()
api_router.registry.extend(repository_router.registry)
