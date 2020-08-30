from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profile_api import views

router = DefaultRouter()
router.register(r'hello-viewset', views.HelloViewSet, basename = 'hello-viewset')
router.register(r'profile', views.UserProfileViewSet)
router.register(r'feed', views.UserProfileFeedViewSet   )
urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view(), name = 'hello-view'),
    path('', include(router.urls)),
    path('login/', views.UserLoginApiView.as_view(), name = 'login'),
]
