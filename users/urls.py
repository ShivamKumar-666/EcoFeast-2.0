from django.urls import path
from .views import (
    RegisterUserView, landing_view, login_view,
    register_view, logout_view, UserProfileUpdateView
)

urlpatterns = [
    # API ENDPOINT (For the Register Form to talk to)
    path('api/register/', RegisterUserView.as_view(), name='register-api'),

    # FRONTEND PAGES (For Humans)
    path('', landing_view, name='landing'),
    path('login/', login_view, name='login-ui'),
    path('signup/', register_view, name='register-ui'),
    path('logout/', logout_view, name='logout-ui'),
    path('profile/update/', UserProfileUpdateView.as_view(), name='profile-update'),
]