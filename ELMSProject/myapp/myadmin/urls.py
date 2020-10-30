from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('home/', views.home, name="home"),
    path('login/', views.index, name="index"),
    path('myadmin/', views.changepass, name="changepass"),
    path('signup/', views.signup, name="signup"),
    path('displaysignup/', views.displaysignup, name="displaysignup"),
    path('showsignuplist/', views.userlist, name="userlist"),
    path('success/', views.success, name="success"),
    path('logincheck/', views.logincheck, name="logincheck"),
    path('loginempcheck/', views.loginempcheck, name="loginempcheck"),
    path('changepwd/', views.changepass, name="changepwd"),
    path('empchangepwd/', views.empchangepass, name="empchangepass"),
    path('logout/', views.logout, name="logout"),
    path('addsignup/', views.addsignup, name="addsignup"),
    #path('myadmin/', views.home, name="home"),
    #path('', include('myadmin.urls'))
    #-----start department--------
    path('department/', views.displaydept, name="displaydept"),
    path('add_department/', views.adddept, name="adddept"),
    path('adddepartment/', views.adddepartment, name="adddepartment"),
    path('displaydept/', views.displaydept, name="displaydept"),
    path('edit/<int:id>', views.editdept, name="editdept"),
    path('updatedept/<int:id>', views.updatedept, name="updatedept"),
    path('deletedepartment/<int:id>', views.deletedept, name="deletedept"),
    #-----end department--------
    #----------start leave type--------
    path('addleavetype/', views.addleavetype, name="addleavetype"),
    path('addtypeofleave/', views.addtypeofleave, name="addtypeofleave"),
    path('displayleavetype/', views.displayleavetype, name="displayleavetype"),
    path('editleavetype/<int:id>', views.editleavetype, name="editleavetype"),
    path('updateleavetype/<int:id>', views.updateleavetype, name="updateleavetype"),
    path('deleteleavetype/<int:id>', views.deleteleavetype, name="deleteleavetype"),
    #------------------end leave type---------------
    path('displayemp/', views.displayemp, name="displayemp"),
    path('addemployee/', views.addemployee, name="addemployee"),
    path('addemp/', views.addemp, name="addemp"),
    path('myadmin/leave-history/', views.displeavehistory, name="displeavehistory"),
    path('applyleave/', views.applyleave, name="applyleave"),
    path('addapplyleave/', views.addapplyleave, name="addapplyleave"),
    path('addpatients/', views.addpatients, name="addpatients"),
    path('addpatient/', views.addpatient, name="addpatient"),
    path('empchangepassword/', views.empchangepass, name="empchangepass"),
    path('empleavehistory/', views.empleavehistory, name="empleavehistory"),
    path('empprofile/', views.empprofile, name="empprofile"),
]