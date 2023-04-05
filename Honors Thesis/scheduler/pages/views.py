from django.shortcuts import render
from django.http.response import JsonResponse
from django.http import HttpResponse
from pages.models import Prof, Course, Room
TIMES = [('MWF','08:00','10:30'), ('MWF','09:05','9:55'), ('MWF','10:10','11:00'), ('MWF','11:15','12:05'), ('MWF','12:20','1:10'), ('MWF','1:25','2:15'), ('MWF','2:30','3:20'), ('MWF','3:35','4:25'), ('MWF','4:40','5:30'), 
             ('TR','08:00','09:15'), ('TR','09:30','10:45'), ('TR','11:00','12:15'), ('TR','12:30','1:45'), ('TR','2:00','3:15'), ('TR','03:30','04:45'), 
             ('MW','07:35','08:50'), ('MW','04:40','5:55'), ('MW','07:35','8:50'), ('MF','04:40','5:55'), ('WF','07:35','8:50'), ('WF','04:40','5:55')]
    

#logic to connect user inputs to database

#dept, number, name, credits, dependencies
#make sure to know that in course.py in logic, dept+number = number

#del all course and prof entries and make sure to print everything out on a page to see it all
#create html pages, url pattern
def cleanTablesView(request):
    #remove all profs and courses
    Prof.objects.all().delete()
    Course.objects.all().delete()

def currDataView(request):
    profs = Prof.objects.all()
    courses= Course.objects.all()
    context = {"profs": profs, "courses": courses}
    return HttpResponse(render(request, 'curr_data.html', context=context))

def homePageView(request):
    return render(request, 'home.html')

#MAIN ALG
def outputPageView(request):
    #take prof and room info from database
    #run genetic alg
    #output the schedules
    return render(request, 'output.html')

def profOptionsView(request):
    return HttpResponse(render(request, 'professor_options.html'))

def addProfessorView(request):
    profs = Prof.objects.all()
    curr_courses = Course.objects.all()
    times = TIMES
    context = {"profs": profs, "courses": curr_courses, "times" : times}
    return HttpResponse(render(request, 'add_professor.html', context=context))

def addProfessorConfView(request):
    name=request.POST["name"]
    profID=request.POST["prof_id"]    
    course_keys = request.POST.getlist("courses")

    hard_times = request.POST.getlist("hard_prefs")
    soft_times = request.POST.getlist("soft_prefs")

    if Prof.objects.filter(name__iexact = name, profID__iexact=profID).exists():
        return HttpResponse(render(request, 'add_prof_error.html')) 

    p = Prof(name=name, profID=profID, hard_times=hard_times, soft_times=soft_times)
    p.save()
    for key in course_keys:
        c = Course.objects.get(id = key)
        p.courses.add(c)
    p.save()
    return HttpResponse(render(request, 'add_professor_conf.html')) 

def updateProfView(request):
    courses = Course.objects.all()
    context = {"courses": courses, "times": TIMES}
    return HttpResponse(render(request, 'update_prof.html', context))

def updateProfConfView(request):
    profID = request.POST["profID"]
    new_name = request.POST["name"]
    new_course_keys = request.POST["courses"]
    new_hard_times = request.POST["hard_prefs"]
    new_soft_times = request.POST["soft_prefs"]

    #should be single course
    p = Prof.objects.filter(profID = profID)
    p.name, p.course_keys, p.hard_times, p.soft_times = new_name, new_course_keys, new_hard_times, new_soft_times
    p.save()
    return HttpResponse(render(request, 'update_prof_conf.html'))

def directoryView(request):
    return HttpResponse(render(request, 'directory_manager.html'))

#test
def addRemoveDependencyView(request):
    return HttpResponse(render(request, 'add_remove_dependency.html'))

def addDependencyView(request):
    courses = Course.objects.all()
    context = {'courses': courses}
    return HttpResponse(render(request, 'add_dependency.html', context=context))

def removeDependencyView(request):
    courses = Course.objects.all()
    context = {'courses': courses}
    return HttpResponse(render(request, 'remove_dependency.html', context=context))

def removeDependencyConfView(request):
    #will do post stuff, query database for course, remove dependencies to course
    course_id = request.POST["course"] #will be course key 
    course = Course.objects.get(id=course_id)

    dependency_keys = request.POST.getlist("dependencies")

    for key in dependency_keys:        
        c = Course.objects.get(id = key)
        print(c.number)
        course.dependencies.remove(c)
    course.save()
    
    print(course.dependencies)  
    print("hi")      
    return HttpResponse(render(request, 'remove_dependency_conf.html'))

def addDependencyConfView(request):
    #will do post stuff, query database for course, add dependencies to course
    course_id = request.POST["course"] #will be course key 

    course = Course.objects.get(id=course_id)
    dependency_keys = request.POST.getlist("dependencies")

    for key in dependency_keys:
        print(key)
        c = Course.objects.get(id = key)
        course.dependencies.add(c)
    course.save()
    return HttpResponse(render(request, 'add_dependency_conf.html'))

def addCourseView(request):
    return HttpResponse(render(request, 'add_course.html'))

def addCourseConfView(request):
    dept = request.POST["dept"]
    number = request.POST["number"]
    name = request.POST["course_name"]
    credits = request.POST["credits"]
    if Course.objects.filter(dept__iexact = dept, number__iexact=number).exists():
        return HttpResponse(render(request, 'add_course_error.html'))
    c = Course(dept = dept, number = number, name = name, credits = credits)
    c.save()
    courses = Course.objects.all()
    context = {"courses": courses}
    return HttpResponse(render(request, 'add_course_conf.html', context=context))

def removeCourseView(request):
    courses = Course.objects.all()
    context = {"courses": courses}
    return HttpResponse(render(request, 'remove_course.html', context=context))

def removeCourseConfView(request):
    removing_courses = request.POST.getlist("courses") #course id

    for key in removing_courses:
        c = Course.objects.get(id = key)
        c.delete()
    return HttpResponse(render(request, 'remove_course_conf.html'))

#has survey
def updateCourseView(request):
    return HttpResponse(render(request, 'update_course.html'))

def updateCourseConfView(request):
    old_dept = request.POST["old_dept"]
    old_number = request.POST["old_number"]
    new_dept = request.POST["new_dept"]
    new_number = request.POST["new_number"]
    new_name = request.POST["new_course_name"]
    new_credits = request.POST["new_credits"]
    #print(old_dept, old_number, new_dept, new_number, new_name, new_credits)
    #should be single course
    c = Course.objects.filter(dept = old_dept, number = old_number)
    c.dept, c.number, c.name, c.credits  = new_dept, new_number, new_name, new_credits
    c.save()
    return HttpResponse(render(request, 'update_course_conf.html'))