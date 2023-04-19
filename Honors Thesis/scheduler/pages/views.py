import random
from random import sample
from django.shortcuts import render
from django.http.response import JsonResponse
from django.http import HttpResponse
from pages.models import Prof, Course, Room
TIMES = [('MWF', '08:00', '10:30'), ('MWF', '09:05', '9:55'), ('MWF', '10:10', '11:00'), ('MWF', '11:15', '12:05'), ('MWF', '12:20', '1:10'), ('MWF', '1:25', '2:15'), ('MWF', '2:30', '3:20'), ('MWF', '3:35', '4:25'), ('MWF', '4:40', '5:30'),
             ('TR', '08:00', '09:15'), ('TR', '09:30', '10:45'), ('TR', '11:00', '12:15'), (
                 'TR', '12:30', '1:45'), ('TR', '2:00', '3:15'), ('TR', '03:30', '04:45'),
             ('MW', '07:35', '08:50'), ('MW', '04:40', '5:55'), ('MW', '07:35', '8:50'), ('MF', '04:40', '5:55'), ('WF', '07:35', '8:50'), ('WF', '04:40', '5:55')]

# to run alg, change schedule class in thesis to take in data inputs from thesis
# make instances of course, dept, instructor, and c

# make all the profs for the database

def generateProfsView(request): # ABOUT 34 NUMBER OF PROFS
    # for i in range(34):
    #     # Define the percentage range to randomly select from (50 to 80%)
    #     lower_percentage = 50
    #     upper_percentage = 80
    #     # Calculate the number of items to select within the percentage range
    #     num_times = int(len(TIMES) * random.uniform(lower_percentage/100, upper_percentage/100))
    #     # Randomly select items from the list using a slice operation
    #     ht = random.sample(TIMES, num_times)
    #     st = random.sample(ht, len(ht)//2)

    #     p = Prof(name="PROF"+str(i+1), profID=i+1, hard_times=ht, soft_times=st)
    #     p.save()
        
    #     r = random.randint(5, 10)
    #     for i in range(r):
    #         random_courses = Course.objects.all().order_by('?')
    #         selected_courses = random_courses[:r]

    #         for c in selected_courses:
    #             p.courses.add(c)
    #     p.save()
    return HttpResponse(render(request, 'generate_profs.html'))

def currDataView(request):
    profs = Prof.objects.all()
    #imma just del half of the prefs with this
    # for prof in profs:
    #     course_prefs = list(prof.courses.all())

    #     # get the number of course preferences
    #     num_course_prefs = len(course_prefs)

    #     # calculate the number of course preferences to delete
    #     num_to_delete = num_course_prefs // 2

    #     # randomly select which course preferences to delete
    #     to_delete = sample(range(num_course_prefs), num_to_delete)

    #     # delete the selected course preferences
    #     for index in sorted(to_delete, reverse=True):
    #         del course_prefs[index]

    #     # set the new course preferences for the professor
    #     prof.courses.set(course_prefs)

    for p in profs:
        p.hard_times = [p.hard_times]
        p.soft_times = [p.soft_times]

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
    print(course)
    print(course.dependencies.all())
    dependency_keys = request.POST.getlist("dependencies")

    for key in dependency_keys:
        print(key)
        c = Course.objects.get(id = key)
        print(c)
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