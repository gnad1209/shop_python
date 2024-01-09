from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
# Create your views here.

class GetView(View):
    def get(self, req):
        return render(req,'home/index.html')
