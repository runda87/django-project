from django.urls import path
from .views import CreateAccountViews

app_name = 'users'

urlpatterns = [
    path('create-account/', CreateAccountViews.as_view(), name='createAccount')
]