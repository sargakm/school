from django.shortcuts import render,redirect
from collegeapp.models import Department,User,Teacher,Student
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout


def dep_add(request):
    if request.method=="POST":
        d=request.POST["dep"]
        x=Department.objects.create(Dep_name=d)
        x.save()
        return HttpResponse("success")
    else:
        return render(request,'dep_add.html')
    
def mainhome(request):
    return render(request,'mainhome.html')    

def index(request):
    return render(request,'index.html')        

def adminhome(request):
    return render(request,'adminhome.html')

def reg_teacher(request):
    if request.method=="POST":
        d=request.POST['dep']
        f=request.POST['fname']
        l=request.POST['lname']
        e=request.POST['email']
        u=request.POST['username']
        p=request.POST['password']
        a=request.POST['age']
        ad=request.POST['address']
        q=request.POST['qual']
        x=User.objects.create_user(first_name=f,last_name=l,email=e,username=u,password=p,usertype='teacher')
        x.save()
        y=Teacher.objects.create(tid=x,depid_id=d,Age=a,Address=ad,Qualification=q)
        y.save()
        return HttpResponse("success")
    else:
        x=Department.objects.all()
        return render(request,'reg_teacher.html',{'x1':x})
    

def reg_student(request):
    if request.method=="POST":
        d=request.POST['dep']
        f=request.POST['fname']
        l=request.POST['lname']
        e=request.POST['email']
        u=request.POST['username']
        p=request.POST['password']
        a=request.POST['age']
        ad=request.POST['address']
        x=User.objects.create_user(first_name=f,last_name=l,email=e,username=u,password=p,usertype='student',is_active=False)
        x.save()
        y=Student.objects.create(depid_id=d,sid=x,Address=ad,Age=a)
        y.save()
        return HttpResponse("student registered")
    else:
        x=Department.objects.all()
        return render(request,'reg_student.html',{'x1':x})
    
def viewstudents(request):
    x=Student.objects.all()
    return render(request,'viewstudent.html',{'x1':x}) 

def deletestudents(request,uid):
    x=User.objects.get(id=uid)
    x.delete()
    return redirect(viewstudents)


def viewteacher(request):
    x=Teacher.objects.all()
    return render(request,'viewteacher.html',{'x1':x})

def deleteteacher(request,uid):
    x=User.objects.get(id=uid)
    x.delete()
    return redirect(viewteacher)

def approve(request,aid):
    st=Student.objects.get(id=aid)
    st.sid.is_active=True
    st.sid.save()
    return redirect(viewstudents)

def teacherhome(request): 
    return render(request,'teacherhome.html')   

def studenthome(request):
    return render(request,'studenthome.html') 


def logins(request):
    if request.method=="POST":
        u=request.POST['username']
        p=request.POST['password']
        User=authenticate(request,username=u,password=p)
        if User is not None and User.is_superuser==1:
            return redirect(adminhome)
        elif User is not None and User.usertype=="teacher":
            login(request,User)
            request.session['teach_id']=User.id
            return redirect(teacherhome)
        elif User is not None and User.usertype=="student" and User.is_active==1:
            login(request,User)
            request.session['stud_id']=User.id
            return redirect(studenthome)
        else:
            return HttpResponse("not valid")
        
    else:
        return render(request,'logins.html')


def approved_stview(request):
    x=User.objects.filter(is_active=1,usertype="student")
    return render(request,'approved_stview.html',{'x':x})

def updatest(request):
    stud=request.session.get('stud_id')
    student=Student.objects.get(sid_id=stud)
    user=User.objects.get(id=stud)
    return render(request,'updatest.html',{'view':student,'data':user})

def updatestudent(request,uid):
    if request.method=="POST":
        stud=Student.objects.get(id=uid)
        sid=stud.sid_id
        user=User.objects.get(id=sid)
        user.first_name=request.POST['fname']
        user.last_name=request.POST['lname']
        user.email=request.POST['email']
        user.username=request.POST['uname']
        user.save()
        stud.Age=request.POST['age']
        stud.Address=request.POST['address']
        stud.save()
        return HttpResponse("success")
    

def updateteach(request):
    teach=request.session.get('teach_id')
    teacher=Teacher.objects.get(tid_id=teach)
    user=User.objects.get(id=teach)
    return render(request,'updateteach.html',{'view':teacher,'data':user})

def updateteacher(request,uid):
    if request.method=="POST":
        teach=Teacher.objects.get(id=uid)
        tid=teach.tid_id
        user=User.objects.get(id=tid)
        user.first_name=request.POST['fname']
        user.last_name=request.POST['lname']
        user.email=request.POST['email']
        user.username=request.POST['uname']
        user.save()
        teach.Age=request.POST['age']
        teach.Address=request.POST['address']
        teach.Address=request.POST['qualification']
        teach.save()
        return HttpResponse("success")
    

def lgout(request):
    logout(request)
    return redirect(logins) 

def regi(request):
    return render(request, "regi.html")

def table(request):
     return render(request, "table.html")

def depbystudent(request):
    teacher=Teacher.objects.get(tid=request.user)
    department_student=Student.objects.filter(depid=teacher.depid)
    return render(request,'department_student.html',{'x1':department_student})

def depbyteacher(request):
    student=Student.objects.get(sid=request.user)
    department_teacher=Teacher.objects.filter(depid=student.depid)
    return render(request,'department_teacher copy.html',{'x1':department_teacher})
    










    
    







