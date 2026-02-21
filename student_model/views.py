from django.shortcuts import redirect, render
from .import models
# Create your views here.
def home(request):
    students=models.Student.objects.all().order_by('roll')
    return render(request,'home.html',{'datas':students})

def delete_student(request,roll):
    student=models.Student.objects.get(roll=roll)
    student.delete()
    # print(student)
    return redirect('home')
    