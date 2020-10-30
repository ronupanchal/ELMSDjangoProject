from django.db import models


# Create your models here.
class UserTable(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    utype = models.CharField(max_length=50)
    updationDate = models.DateField()

    class Meta:
        db_table = "tbl_user"


class DeptTable(models.Model):
    deptName = models.CharField(max_length=50)
    deptShortName = models.CharField(max_length=20)
    deptCode = models.CharField(max_length=50)
    creationDate = models.DateField()

    class Meta:
        db_table = "tbl_department"


class LeaveTypeTable(models.Model):
    leaveType = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    creationDate = models.DateTimeField()

    class Meta:
        db_table = "tbl_leavetypes"


class EmployeeTable(models.Model):
    empcode = models.CharField(max_length=10)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    birthdate = models.DateField()
    gender = models.CharField(max_length=10)
    deptname = models.CharField(max_length=50)
    emailid = models.CharField(max_length=50)
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    epassword = models.CharField(max_length=20)
    ecpassword = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    status = models.IntegerField()
    regdate = models.DateTimeField()

    class Meta:
        db_table = "tbl_employee"


class LeaveHistoryTable(models.Model):
    leaveType = models.CharField(max_length=100)
    toDate = models.DateField()
    fromDate = models.DateField()
    description = models.CharField(max_length=500)
    postingDate = models.DateTimeField()
    adminRemark = models.CharField(max_length=500)
    adminRemarkDate = models.DateTimeField()
    leaveStatus = models.IntegerField()
    IsRead = models.IntegerField()
    empid = models.IntegerField()

    class Meta:
        db_table = "tbl_leavehistory"


class Inpatient(models.Model):
    pid = models.CharField(max_length=10)
    adm  = models.DateTimeField()

    class Meta:
        db_table = "tbl_inpatient"