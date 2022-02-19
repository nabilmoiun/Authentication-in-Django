from django.urls import path
from django.contrib.auth.views import (
    PasswordResetDoneView,
    PasswordResetCompleteView
)

from .views import (
    Home,
    Login,
    Logout,
    Registration,
    ChangePassword,
    SendEmailToResetPassword,
    ResetPasswordConfirm
)


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('registration/', Registration.as_view(), name='registration'),
    path('change_password/', ChangePassword.as_view(), name='change_password'),
    path('password_reset/', SendEmailToResetPassword.as_view(), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(template_name='account/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', ResetPasswordConfirm.as_view(), name='password_reset_confirm'),


]