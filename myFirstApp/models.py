from django.db import models

class Users(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    fullname = models.CharField(max_length=200)
    email = models.CharField(max_length=200, default = '')
    def delete_account(self):
        self.delete

class Courses(models.Model):
    course_title = models.CharField(max_length=200)
    deskripsi = models.CharField(max_length=200)
    karakteristik_id = models.CharField(max_length=200, default='1,2')

    def set_karakteristik(self,karakteristik):
        self.karakteristik = ','.join(karakteristik)

    def get_karakteristik(self):
        return self.karakteristik_id.split(',')

class Karakteristik(models.Model):
    deskripsi = models.CharField(max_length=200)

class Feedback(models.Model):
    content = models.TextField()
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)

class Certificate(models.Model):
    user_id = models.CharField(max_length=200)
    course_id = models.CharField(max_length=200)
    status = models.CharField(max_length=200, default='Belum Selesai')




    


# Create your models here.
