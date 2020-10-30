# Generated by Django 2.2.5 on 2019-10-10 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DeptTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deptName', models.CharField(max_length=50)),
                ('deptShortName', models.CharField(max_length=20)),
                ('deptCode', models.CharField(max_length=50)),
                ('creationDate', models.DateField()),
            ],
            options={
                'db_table': 'tbl_department',
            },
        ),
        migrations.CreateModel(
            name='EmployeeTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empcode', models.CharField(max_length=10)),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('birthdate', models.DateField()),
                ('gender', models.CharField(max_length=10)),
                ('deptname', models.CharField(max_length=50)),
                ('emailid', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=500)),
                ('city', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('epassword', models.CharField(max_length=20)),
                ('ecpassword', models.CharField(max_length=20)),
                ('mobile', models.CharField(max_length=20)),
                ('status', models.IntegerField()),
                ('regdate', models.DateTimeField()),
            ],
            options={
                'db_table': 'tbl_employee',
            },
        ),
        migrations.CreateModel(
            name='LeaveHistoryTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leaveType', models.CharField(max_length=100)),
                ('toDate', models.DateField()),
                ('fromDate', models.DateField()),
                ('description', models.CharField(max_length=500)),
                ('postingDate', models.DateTimeField()),
                ('adminRemark', models.CharField(max_length=500)),
                ('adminRemarkDate', models.DateTimeField()),
                ('leaveStatus', models.IntegerField()),
                ('IsRead', models.IntegerField()),
                ('empid', models.IntegerField()),
            ],
            options={
                'db_table': 'tbl_leavehistory',
            },
        ),
        migrations.CreateModel(
            name='LeaveTypeTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leaveType', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
                ('creationDate', models.DateTimeField()),
            ],
            options={
                'db_table': 'tbl_leavetypes',
            },
        ),
        migrations.CreateModel(
            name='UserTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('utype', models.CharField(max_length=50)),
                ('updationDate', models.DateField()),
            ],
            options={
                'db_table': 'tbl_user',
            },
        ),
    ]