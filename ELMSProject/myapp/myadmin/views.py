from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render, redirect
from .models import UserTable, DeptTable, LeaveTypeTable, EmployeeTable, LeaveHistoryTable, Inpatient
from .forms import UserTableForm
from datetime import datetime
from django.contrib import auth, messages


# Create your views here.
def index(request):
    title = "ELMS Admin | Login Page"
    return render(request, "login.html", {"title": title})


def home(request):
    title = "ELMS Admin | Home Page"
    totlt = LeaveTypeTable.objects.count()
    totd = DeptTable.objects.count()
    return render(request, "home.html", {"title": title, "totalleavetype": totlt, "totaldept": totd})


def changepass(request):
    title = "ELMS Admin | Change Password"
    return render(request, "changepassword.html", {"title": title})


#-------------------Start Employee------------
def addemployee(request):
    title = "Admin | Add Employee"
    data = DeptTable.objects.all()
    return render(request, "addemployee.html", {"title": title, "items": data})


def addemp(request):
    form = EmployeeTable()
    form.empcode = request.POST["empcode"]
    form.fname = request.POST["efirstname"]
    form.lname = request.POST["elastname"]
    form.birthdate = request.POST["empdate"]
    form.gender = request.POST["empgender"]
    form.deptname = request.POST["deptname"]
    form.emailid = request.POST["empemail"]
    form.address = request.POST["empaddr"]
    form.city = request.POST["empcity"]
    form.country = request.POST["empcountry"]
    form.epassword = request.POST["emppassword"]
    if form.epassword == request.POST["empcpassword"]:
        form.ecpassword = request.POST["empcpassword"]
    else:
        error = "Your password and confirm password do not match."

    form.mobile = request.POST["empmobile"]
    myDate = datetime.now()
    form.regdate = myDate.strftime("%Y-%m-%d %H:%M:%S")
    form.status = 1
    form.save()
    return HttpResponseRedirect('/displayemp/')


def displayemp(request):
    title = "Admin | Employee"
    data = EmployeeTable.objects.all()
    return render(request, "employee.html", {"title": title, "data": data})

#----------------End Employeee--------------

def applyleave(request):
    title = "Employee | Apply Leave"
    data = LeaveTypeTable.objects.all()
    return render(request, "apply-leave.html", {"title": title, "items": data})


def addapplyleave(request):
    context = {}
    if request.method == "POST":
        form = LeaveHistoryTable()
        form.leaveType = request.POST["leavetypename"]
        form.toDate = request.POST["todate"]
        form.fromDate = request.POST["fromdate"]
        form.description = request.POST["ldescription"]
        myDate = datetime.now()
        form.adminRemark = ""
        form.adminRemarkDate = myDate.strftime("%Y-%m-%d %H:%M:%S")
        form.postingDate = myDate.strftime("%Y-%m-%d %H:%M:%S")
        form.leaveStatus = 1
        form.IsRead = 1
        form.empid = 1

        try:
            form.save()
            messages.success(request, 'Successfully Inserted Record..!')
            return redirect("applyleave")
        except:
            context['Error'] = "Not Insert Record Please Try Again..!"
            return render(request, "apply-leave.html", context)
    else:
        return render(request, "apply-leave.html")


def displaysignup(request):
    title = "Admin | Sign up"
    data = UserTable.objects.all()
    return render(request, "signup.html", {"title": title, "data": data})


def displeavehistory(request):
    title = "Admin | Leave History"
    return  render(request, "leavehistory.html", {"title": title})


def addsignup(request):
    form = UserTable()
    form.username = request.POST['username'].upper()
    form.password = request.POST['upassword']
    form.utype = request.POST['usertype']
    form.updationDate = request.POST['userdate']
    form.save()
    return render(request, "login.html")


#--------------Start Department---------------
def displaydept(request):
    title = "Admin | Department"
    data = DeptTable.objects.all()
    return render(request, "department.html", {"title": title, "data": data})


def adddept(request):
    title = "Admin | Department"
    return render(request, "adddepartment.html", {"title": title})


def adddepartment(request):
    context = {}
    if request.method == "POST":
        form = DeptTable()
        form.deptName = request.POST['departmentname']
        form.deptShortName = request.POST['deptshortname']
        form.deptCode = request.POST['deptcode']
        myDate = datetime.now()
        form.creationDate = myDate.strftime("%Y-%m-%d")
        try:
            form.save()
            messages.success(request, 'Successfully Inserted Record..!')
            return redirect("adddept")
        except:
            context['Error'] = "Not Insert Record Please Try Again..!"
            return render(request, "adddepartment.html", context)
    else:
        return render(request, "adddepartment.html")


def editdept(request, id):
    title = "Edit Department"
    form = DeptTable.objects.get(id=id)
    return render(request, "editdepartment.html", {"title": title, "form": form})


def updatedept(request, id):
    #title = "Edit Department"
    form = DeptTable.objects.get(id=id)
    form.deptName = request.POST['departmentname']
    form.deptShortName = request.POST['deptshortname']
    form.deptCode = request.POST['deptcode']
    myDate = datetime.now()
    form.creationDate = myDate.strftime("%Y-%m-%d")
    form.save()
    return HttpResponseRedirect('/displaydept/')


def deletedept(request, id):
    form = DeptTable.objects.get(id=id)
    form.delete()
    form = DeptTable.objects.all()
    return HttpResponseRedirect('/displaydept/')
#----------------End Department----------------------------------


#----------------Start Leave History--------------------------------
def displayleavehistory(request):
    title = "Admin | Leave Type"
    data = LeaveTypeTable.objects.all()
    return render(request, "leavehistory.html", {"title": title, "data": data})


#----------------Start Leave Type--------------------------------
def displayleavetype(request):
    title = "Admin | Leave Type"
    data = LeaveTypeTable.objects.all()
    return render(request, "leavetype.html", {"title": title, "data": data})


def addleavetype(request):
    title = "Admin | Add Leave Type"
    return render(request, "addleavetype.html", {"title": title})


def addtypeofleave(request):
    form = LeaveTypeTable()
    form.leaveType = request.POST["leavetypename"]
    form.description = request.POST["ldescription"]
    myDate = datetime.now()
    form.creationDate = myDate.strftime("%Y-%m-%d %H:%M:%S")
    form.save()
    return HttpResponseRedirect('/displayleavetype/')


def deleteleavetype(request, id):
    form = LeaveTypeTable.objects.get(id=id)
    form.delete()
    form = LeaveTypeTable.objects.all()
    return HttpResponseRedirect('/displayleavetype/')


def editleavetype(request, id):
    title = "Edit Leave Type"
    form = LeaveTypeTable.objects.get(id=id)
    return render(request, "editleavetype.html", {"title": title, "form": form})


def updateleavetype(request, id):
    form = LeaveTypeTable.objects.get(id=id)
    form.leaveType = request.POST["leavetypename"]
    form.description = request.POST["ldescription"]
    myDate = datetime.now()
    form.creationDate = myDate.strftime("%Y-%m-%d %H:%M:%S")
    form.save()
    return HttpResponseRedirect('/displayleavetype/')


#----------------End Leave Type--------------------------------
def logincheck(request):
    if request.method != 'POST':
        raise Http404('Only POSTs are allowed')
    try:
        u = UserTable.objects.get(username=request.POST['uname'])

        if u.username == request.POST['uname']:
            request.session['uname'] = u.username
            welcome_user = request.session.get('uname', 0)
            noti = "Ronak Panchal EMP001 applied for leave at 2019."
            return render(request, "changepassword.html", {"welcomeuser": welcome_user, "notification": noti})
    except UserTable.DoesNotExist:
        error = "Your username and password didn't match."
        return render(request, "login.html", {"error": error})


def loginempcheck(request):
    if request.method != 'POST':
        raise Http404('Only POSTs are allowed')
    try:
        u = EmployeeTable.objects.get(emailid=request.POST['uname'])

        if u.emailid == request.POST['uname']:
            request.session['uname'] = u.fname
            welcome_user = request.session.get('uname', 0)
            noti = "Ronak Panchal EMP001 applied for leave at 2019."
            return render(request, "emp-changepassword.html", {"welcomeuser": welcome_user, "notification": noti})
    except EmployeeTable.DoesNotExist:
        error = "Your username and password didn't match."
        return render(request, "login.html", {"error": error})
"""def logincheck(request):
    if request.session.has_key('username'):
        uname = request.session['username']
        return render(request, "changepassword.html", {'usrname': uname})

        context = {}
        if request.method == 'POST':
            U = request.POST['utype']
            if U == "admin":
                uname = request.POST['uname']
                upassword = request.POST['psw']
                try:
                    user = UserTable.objects.get(username = uname,password=upassword)
                except:
                    context['Error'] = "Invalid Email and password"
                    return render(request, "login.html", context)
                if user is not None:
                    request.session['username'] = user.uname
                    #if 'next' in request.POST:
                    #    return redirect(request.POST.get('next'))
                    #else:
                    return HttpResponseRedirect('/changepass/')
                else:
                    context['Error'] = "Invalid Email and password"
                    return render(request, "changepassword.html", context)
            else:
                uname = request.POST['uname']
                upassword = request.POST['psw']
                try:
                    user = UserTable.objects.get(username = uname,password=upassword)
                except:
                    context['Error'] = "Invalid Email and password"
                    return render(request, "login.html", context)
                if user is not None:
                    request.session['username'] = user.uname
                    return render(request, "emp-changepassword.html")
                else:
                    context['Error'] = "Invalid Email and password"
                    return render(request, "login.html", context)
        else:
            return render(request, "login.html")
"""


def changepwd(request):
    context = {}
    if request.session.has_key('username'):
        un = request.session['username']
        firstname = UserTable.objects.get(username=un)
        #photo = EmployeeTable.objects.get(email=email)
        if request.method == "POST":
            update = UserTable.objects.get(password=request.POST['currname'])
            new_pwd = request.POST['new_pwd']
            confirm_pwd = request.POST['confirm_pwd']
            if new_pwd == confirm_pwd:
                update.password = new_pwd
                try:
                    update.save()
                    messages.success(request, 'Successfully Change Password..!')
                    return render(request, "changepassword.html")
                except:
                    context['Error'] = "Not Change Password Please Try Again..!"
                    return render(request, "changepassword.html", context)
            else:
                context['Error'] = "Does't Match Password..!"
                return render(request, "changepassword.html", context)
        else:
            return render(request, "changepassword.html", {"welcomeuser": firstname})
    else:
        return render(request, "login.html")


def logout(request):
    from django.contrib import auth
    auth.logout(request)
    return HttpResponseRedirect('/login/')


def userlist(request):
    title = "User Detail"
    query_results = UserTable.objects.all()
    return render(request, "showuserlist.html", {"title": title, "data": query_results})


def signup(request):
    title = "ELMS Admin | Sign Up Page"
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UserTableForm(request.POST)
        # check whether it's valid:
        if form.is_valid():

            form.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/success/')
        #return redirect('success.html')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = UserTableForm(request.POST)
    return render(request, "login.html", {"title": title, "form": form})


def success(request):
    title = "ELMS Admin | Success Page"
    return render(request, "success.html", {"title": title})


def addpatients(request):
    title = "ELMS Admin | Patient Page"
    return render(request, "addpatientss.html", {"title": title})


def empchangepass(request):
    title = "ELMS Employee"
    return render(request, "emp-changepassword.html", {"title": title})


def empleavehistory(request):
    title = "ELMS Employee"
    return render(request, "emp-leavehistory.html", {"title": title})


def empprofile(request):
    title = "ELMS Employee"
    return render(request, "empprofile.html", {"title": title})


def addpatient(request):
    form = Inpatient()
    form.pid = request.POST["pid"]
    form.adm = request.POST["padm"]
    form.save()
    return HttpResponseRedirect('/displayleavetype/')


"""def login(request):
    if request.session.has_key('doctor_email'):
        email = request.session['doctor_email']
        return render(request, "Admin/doctor_dashboard.html", {'doctor_email': email})
    if request.session.has_key('user_email'):
        email = request.session['user_email']
        #--------------------------------------------------------------------------------
        return render(request, "Admin/doctor_dashboard.html", {'user_email': email})
        # --------------------------------------------------------------------------------
    context = {}
    if request.method == 'POST':
        U = request.POST['checkuser']
        if U == "Doctor":
            email = request.POST['email']
            password = request.POST['password']
            try:
                user = Doctor.objects.get(email = email,password=password)
            except:
                context['Error'] = "Invalid Email and password"
                return render(request, "User/login.html", context)
            if user is not None:
                request.session['doctor_email'] = user.email
                #if 'next' in request.POST:
                #    return redirect(request.POST.get('next'))
                #else:
                return HttpResponseRedirect('admin/doctor_dashboard')
            else:
                context['Error'] = "Invalid Email and password"
                return render(request, "User/login.html", context)
        elif U == "Patient":
            email = request.POST['email']
            password = request.POST['password']
            try:
                user = Patient.objects.get(email = email,password=password)
            except:
                context['Error'] = "Invalid Email and password"
                return render(request, "User/login.html", context)
            if user is not None:
                request.session['user_email'] = user.email
                return HttpResponseRedirect('admin/patient_dashboard')
            else:
                context['Error'] = "Invalid Email and password"
                return render(request, "User/login.html", context)
    else:
        return render(request, "User/login.html")
#-------------------------
#Convert into JSON format
#import django.core import serializers
#import django.http import HttpResponse
def list(request):
    queryset=UserTable.objects.all()
    queryset=serializars.serialize('json',queryset)
    return HttpResponse(queryset, content_type='application/json')
#-------------------------
"""

