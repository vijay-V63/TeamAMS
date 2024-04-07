from django.db import models

class Alumni(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    mobileno=models.IntegerField()
    password=models.CharField(max_length=14)

    #checking if email is existing or not
    def isexist(self):
        if Alumni.objects.filter(email=self.email):
            return True
        return False
    
    