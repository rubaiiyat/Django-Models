from django.shortcuts import redirect, render
from .import models
from .import forms
# Create your views here.
def home(request):
    if request.method=='POST':
        form=forms.StudentForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            return redirect('home')
    else:
        form=forms.StudentForm
    students=models.Student.objects.all().order_by('roll')
    return render(request,'home.html',{'datas':students,'form':form})

def delete_student(request,roll):
    student=models.Student.objects.get(roll=roll)
    student.delete()
    # print(student)
    return redirect('home')
    