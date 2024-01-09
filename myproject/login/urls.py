from . import views
from django.urls import path

app_name = 'login'
urlpatterns = [
    path('',views.GetView.as_view(),name='getview'),
]