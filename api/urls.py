from django.urls import path
from rest_framework.routers import DefaultRouter
from data.views import BlogsLevelOneViewSet, BlogsLevelThreeViewSet, BlogsMaxClearanceViewSet

router = DefaultRouter()
router.register('blogs_one', BlogsLevelOneViewSet)
router.register('blogs_three', BlogsLevelThreeViewSet)
router.register('blogs_secret', BlogsMaxClearanceViewSet)

urlpatterns = router.urls
