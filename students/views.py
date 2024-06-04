from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    faculty = request.GET.get('faculty')
    search_query = request.GET.get('search_query')
    students = Student.objects.all() 
    if faculty:
        students = students.filter(faculty=faculty)
    if search_query:
        students = students.filter(
            Q(first_name__icontains=search_query) |
            Q(last_name__icontains=search_query) |
            Q(email__icontains=search_query) |
            Q(faculty__icontains=search_query)
        )  
    faculties = Student.objects.values_list('faculty', flat=True).distinct()
    
    return render(request, 'index.html', {'students': students, 'faculties': faculties})


def view_student(request, id):
    student=Student.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'),{'student':student})

def add_student(request):
    if request.method=="POST":
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        faculty=request.POST.get('faculty')
        gpa=request.POST.get('gpa')
        std=Student.objects.create(first_name=first_name,last_name=last_name,email=email,faculty=faculty,gpa=gpa)
        if (first_name and last_name and email and faculty and gpa) is not None:
            std.save()
            return render(request,'add_student.html',{'success':True})  
    return render(request,'add_student.html',{})    

def update_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == "POST":
        student.first_name = request.POST['first_name']
        student.last_name = request.POST.get('last_name')
        student.email = request.POST.get('email')
        student.faculty = request.POST.get('faculty')
        student.gpa = request.POST.get('gpa')
        student.save()
        return render(request, 'update_student.html', {'success': True, 'student': student})
    return render(request, 'update_student.html', {'student': student, 'success': False})


def delete_student(request, id):
    student= get_object_or_404(Student, id=id)
    if request.method=="POST":
        student.delete()
    return HttpResponseRedirect(reverse('index'))
