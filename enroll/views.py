from django.shortcuts import render
from .forms import StudentRegistration
from .models import User
from django.http import HttpResponseRedirect

# Create your views here.
def add_show(request):
    if request.method == 'POST':
        fmData = StudentRegistration(request.POST)
        if fmData.is_valid():
            # fmData.save()
                    # OR
            name = fmData.cleaned_data.get('name')
            email = fmData.cleaned_data.get('email')
            pas = fmData.cleaned_data.get('password')
            u = User(name=name,email=email,password=pas)
            u.save()
            fmData = StudentRegistration()
    else:
        fmData = StudentRegistration()
    stud = User.objects.all()
    return render(request,'enroll/addandshow.html',{'form':fmData,'stu':stud})

# delete student
def delete_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
    
# update student
def update_student(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
    return render(request,'enroll/updatestudent.html',{'form':fm})