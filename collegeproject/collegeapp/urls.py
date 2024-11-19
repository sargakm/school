from django.contrib import admin
from django.urls import path,include
from collegeapp import views

urlpatterns =[
    path('dep_add',views.dep_add,name='dep_add'),
    path('',views.index,name='index'),
    path('adminhome',views.adminhome,name='adminhome'),
    path('mainhome',views.mainhome,name='mainhome'),
    path('reg_teacher',views.reg_teacher,name='reg_teacher'),
    path('reg_student',views.reg_student,name='reg_student'),  
    path('viewstudents',views.viewstudents ,name='viewstudents'),
    path('approve/<int:aid>',views.approve,name='approve'),
    path('logins',views.logins,name='logins'), 
    path('teacherhome',views.teacherhome,name='techerhome'), 
    path('studenthome',views.studenthome,name='studenthome'), 
    path('approved_stview',views.approved_stview,name='approved_stview'), 
    path('updatest',views.updatest,name='updatest'),
    path('updatestudent/<int:uid>',views.updatestudent,name='updatestudent'),
    path('lgout',views.lgout,name='lgout'),
    path('updateteacher',views.updateteacher,name='updateteacher'), 
    path('updateach',views.updateteach,name='updateteach'),
    path('viewtecher',views.viewteacher,name='viewteacher'),
    path('deleteteacher/<int:uid>',views.deleteteacher,name='deleteteacher'),
    path('deletestudents/<int:uid>',views.deletestudents,name='deletestudents'),
    path('depbystudent',views.depbystudent,name='depbystudent'),
    path('depbyteacher',views.depbyteacher,name='depbyteacher'),
   


    

]
