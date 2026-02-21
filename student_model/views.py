from django.shortcuts import render
from .import models
# Create your views here.
def home(request):
    students=models.Student.objects.all().order_by('roll')
    return render(request,'home.html',{'datas':students})