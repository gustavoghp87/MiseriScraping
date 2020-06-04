from django.conf.urls import url

from . import views

from django.conf.urls import include                 #viewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, 'hello-viewset')    # allows href to /api/hello-viewset/

router.register('profile', views.UserProfileViewSet)     # django doesn't need a second parameter

router.register('login', views.LoginViewSet, 'login')

router.register('feed', views.UserProfileFeedViewSet)

urlpatterns = [
	url(r'^hello-view/', views.HelloApiView.as_view()),
	url(r'', include(router.urls))                            # viewset
]


