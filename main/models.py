from django.db import models

# Patient Model
class Patient(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    fname = models.CharField(max_length=40)
    sname = models.CharField(max_length=20)
    gender = models.CharField(max_length=6)
    address = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=12, null=True, blank=True)
    email = models.CharField(max_length=40, null=True, blank=True)
    contact_person = models.CharField(max_length=40, null=True, blank=True)
    contact_person_phone = models.CharField(max_length=30, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

# Course Category Model
# class CourseCategory(models.Model):
#     title = models.CharField(max_length=150)
#     description = models.TextField()

# Course Model
# class Course(models.Model):
    # category = models.ForeignKey(CourseCategory, on_delete=models.CASCADE)
    # teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    # title = models.CharField(max_length=150)
    # description = models.TextField()

# Student Model
# class Student(models.Model):
#     full_name = models.CharField(max_length=100)
#     email = models.CharField(max_length=100)
#     password = models.CharField(max_length=100)
#     qualification = models.CharField(max_length=200)
#     mobile_no = models.CharField(max_length=12)
#     address = models.TextField()
#     interested_categories = models.TextField()