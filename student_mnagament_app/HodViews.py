from datetime import datetime

from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from student_mnagament_app.models import CustomerUser, Courses, Subjects, Staffs


def admin_home(request):
    return render(request,"hod_template/home_content.html")

def add_staff(request):
    return render(request,"hod_template/add_staff_template.html")

def add_staff_save(request):
    if request.method!="POST":
        return HttpResponse('Methode Not Allowed !')
    else:
        first_name=request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        address = request.POST.get("address")
        try:
            user=CustomerUser.objects.create_user(username=username,password=password,email=email
                                                  ,last_name=last_name,first_name=first_name,user_type=2)
            user.staffs.address=address
            user.save()
            messages.success(request,"Successfully Added Staff")
            return HttpResponseRedirect("/add_staff")
        except:
            messages.error(request,"Failed to Add Staff")
            return HttpResponseRedirect("/add_staff")

def add_course(request):
    return render(request, "hod_template/add_course_template.html")


def add_course_save(request):
    if request.method!="POST":
        return HttpResponse('Methode Not Allowed !')
    else:
        course=request.POST.get("course")
        try:
            course_model=Courses(course_name=course)
            course_model.save()
            messages.success(request, "Successfully Added Course")
            return HttpResponseRedirect("/add_course")
        except:
            messages.error(request, "Failed to Add Course")
            return HttpResponseRedirect("/add_course")

def add_student(request):
    courses=Courses.objects.all()
    return render(request, "hod_template/add_student_template.html",{"courses":courses})

def add_student_save(request):
    if request.method != "POST":
        return HttpResponse('Methode Not Allowed !')
    else:
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        address = request.POST.get("address")
        course_id=request.POST.get("course")
        gender = request.POST.get("gender")
        session_start = request.POST.get("session_start")
        session_end = request.POST.get("session_end")
        try:
            user = CustomerUser.objects.create_user(username=username, password=password, email=email
                                                        , last_name=last_name, first_name=first_name, user_type=3)
            user.students.address = address
            course_obj=Courses.objects.get(id=course_id)
            user.students.course_id=course_obj
            user.students.session_start_year=session_start
            user.students.session_end_year=session_end
            user.students.gender=gender
            user.students.profile_pic=""
            user.save()
            messages.success(request, "Successfully Added Student")
            return HttpResponseRedirect("/add_student")
        except:
            messages.error(request, "Failed to Add Student")
            return HttpResponseRedirect("/add_student")

def add_subject(request):
    courses = Courses.objects.all()
    staffs = CustomerUser.objects.filter(user_type=2)
    return render(request, "hod_template/add_subject_template.html",{"courses":courses,"staffs":staffs})


def add_subject_save(request):
    if request.method!="POST":
        return HttpResponse('Methode Not Allowed !')
    else:
        subject_name=request.POST.get("subject_name")
        course_id = request.POST.get("course")
        course=Courses.objects.get(id=course_id)
        staff_id = request.POST.get("staff")
        staff=CustomerUser.objects.get(id=staff_id)
        try:
            subject=Subjects(subject_name=subject_name,course_id=course,staffs_id=staff)
            subject.save()
            messages.success(request, "Successfully Added Subject")
            return HttpResponseRedirect("/add_subject")
        except:
            messages.error(request, "Failed to Add Subject")
            return HttpResponseRedirect("/add_subject")


