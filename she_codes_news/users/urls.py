from django.urls import path
from .views import CreateAccountViews, ProfileView

app_name = 'users'

urlpatterns = [
    path('create-account/', CreateAccountViews.as_view(), name='createAccount'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
]