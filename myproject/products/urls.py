from . import views
from django.urls import path

app_name = 'products'
urlpatterns = [
    path('',views.GetView.as_view(),name='getview'),
]