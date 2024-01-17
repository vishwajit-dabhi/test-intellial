from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class user(models.Model):
    email = models.EmailField(null = False , blank = False)
    password = models.CharField( max_length=50)
    firstname = models.CharField( max_length=50)
    lastname = models.CharField( max_length=50)

    def user_details(self):
        return {
            "id":self.id,
            "email":self.email,
            "password":self.password,
            "firstname":self.firstname,
            "lastname":self.lastname
        }
    
# class userdata(models.Model):
#     email = models.EmailField(null = False , blank = False)
#     firstname = models.CharField( max_length=50)
#     lastname = models.CharField( max_length=50)

#     def user_data(self):
#         return {
#             "id":self.id,
#             "email":self.email,
#             "firstname":self.firstname,
#             "lastname":self.lastname
#         }