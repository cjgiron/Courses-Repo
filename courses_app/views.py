from django.shortcuts import render, redirect
from .models import Course
from django.contrib import messages



def index(request):
    context = {
        'all_courses': Course.objects.all(),
    }
    return render(request, "index.html", context)


def process_course(request):
    print(request.POST)

    errors = Course.objects.basic_validator(request.POST)
        
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        Course.objects.create(
            name = request.POST['course_name'],
            description = request.POST['course_description']
        )

    return redirect('/')


def destroy_page(request, course_id):
    this_course = Course.objects.get(id=course_id)

    context = {
        'course': this_course,
    }
    
    return render(request, "destroy_page.html", context)


def destroy(request, course_id):
    this_course = Course.objects.get(id=course_id)
    this_course.delete()

    return redirect('/')