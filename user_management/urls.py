from django.urls import path, include
from user_management.views import UserCaptchaView, LoginView, UserMeView
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register('token',UserView)

urlpatterns = [
   path('get_captcha/', UserCaptchaView.as_view(),name="captcha"),
   path('web3_login/', LoginView.as_view(),name="login_view"),
   path('me/', UserMeView.as_view(),name="me_view"),   
   path('',include(router.urls)),
   path('link/<int:pk>/<str:username>/', TokenView.as_view(), name = 'click_link'),

]