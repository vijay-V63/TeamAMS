from django.db import models

class Realalumni(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(unique=True)
    mobileno=models.IntegerField()
    password=models.CharField(max_length=14)

    #checking if email is existing or not
    def isexist(self):
        if Realalumni.objects.filter(email=self.email):
            return True
        return False
    
    #to check login cred matching or not
    @staticmethod
    def getemail(email):
        try:
            return Realalumni.objects.get(email=email)
        except:
            return False