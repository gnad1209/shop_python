from views import GetView
from django.urls import path

urlpatterns = [
    path('',GetView.as_view(),name='getview'),
]