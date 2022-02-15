from django.urls import path

from .views import (
    Home,
    Login,
    Logout
)


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),


]