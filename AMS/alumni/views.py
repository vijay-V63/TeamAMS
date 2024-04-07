from django.shortcuts import render,redirect
from django.http import HttpResponse
from .st import St
from .category import Category
from .alumni import Alumni
from .realalumni import Realalumni
from .studentreg import Studentreg
from django.contrib.auth.hashers import make_password,check_password
from http.client import responses

# Create your views here.
def home(request):
    return render(request,'dem1/index.html')
    #stus=St.objects.all()
    #return render(request,'dem1/indexstu.html',{'stud':stus})

#alumni
#for index2.html
def alumnisignup(request):
    if request.method=="GET":
        return render(request,"dem1/signup.html")
    else:
        name=request.POST['name']
        email=request.POST['email']
        mobileno=request.POST['mobileno']
        password=request.POST['password']
        password=make_password(password)
        userdata=[name,email,mobileno,password]
        print(userdata)

        #storing object
        realalumnidata=Realalumni(name=name,email=email,mobileno=mobileno,password=password)

        #validation
        error_msg=None
        success_msg=None
        if(not name):
            error_msg="Name not Found"
        elif(not email):
            error_msg="email not Found"
        elif(not mobileno):
            error_msg="mobile no. not Found"
        elif(not password):
            error_msg="Password field should not be empty"
        elif(realalumnidata.isexist()):
            error_msg="Email Already Exists"
        if(not error_msg):
            success_msg="Account Created Successfully"
            realalumnidata.save()
            msg={'success':success_msg}
            return render(request,'dem1/signup.html',msg)
        else:
            msg={'error':error_msg,'value':userdata}
            return render(request,"dem1/signup.html",msg)
        
    """
        #storing object
        alumnidata=Alumni(name=name,email=email,mobileno=mobileno,password=password)
        #email-validation
        error_msg=None
        success_msg=None
        if(alumnidata.isexist()):
            error_msg="E-mail Already Exists do login"
        if(not error_msg):
            success_msg="Account Created Successfully"
            alumnidata.save()
        msg={'error':error_msg,'success':success_msg}
        return render(request,"dem1/index3.html",msg)"""


#for index3.html
def alumnilogin(request):
    if request.method=='GET':
        return render(request,"dem1/allogin.html")
    else:
        email=request.POST['email']
        password=request.POST['password']
        #to check login cred
        users=Realalumni.getemail(email)
        if users:
            #if email found check password
            check=check_password(password,users.password)
            #if password found
            if check:
                return render(request,"dem1/index1.html")
            else:
                error_msg="Invalid Password"
                msg={'error':error_msg}
                return render(request,'dem1/allogin.html',msg)
        else:
            error_msg="Invalid ID"
            msg={'error':error_msg}
            return render(request,'dem1/allogin.html')


#for index1.html/
def alumnimain(request):
    return render(request,"dem1/index1.html")

#student
#for index5.html/studentsup
def studentsignup(request):
    if request.method=="GET":
        return render(request,"dem1/studentsup.html")
    else:
        name=request.POST['name']
        email=request.POST['email']
        dept=request.POST['dept']
        mobileno=request.POST['mobileno']
        regdno=request.POST['regdno']
        password=request.POST['password']
        password=make_password(password)
        userdata=[name,email,dept,mobileno,regdno,password]
        print(userdata)

        #storing object
        studentregdata=Studentreg(name=name,email=email,dept=dept,mobileno=mobileno,regdno=regdno,password=password)

        #validation
        error_msg=None
        success_msg=None
        if(not name):
            error_msg="Name not Found"
        elif(not email):
            error_msg="email not Found"
        elif(not mobileno):
            error_msg="mobile no. not Found"
        elif(not password):
            error_msg="Password field should not be empty"
        elif(studentregdata.isexist()):
            error_msg="Email Already Exists"
        if(not error_msg):
            success_msg="Account Created Successfully"
            studentregdata.save()
            msg={'success':success_msg}
            return render(request,'dem1/studentsup.html',msg)
        else:
            msg={'error':error_msg,'value':userdata}
            return render(request,"dem1/studentsup.html",msg)




#for index6.html
def studentlogin(request):
    if request.method=='GET':
        return render(request,"dem1/stulogin.html")
    else:
        email=request.POST['email']
        password=request.POST['password']
        #to check login cred
        users=Studentreg.getemail(email)
        if users:
            #if email found check password
            check=check_password(password,users.password)
            #if password found
            if check:
                return render(request,"dem1/index4.html")
            else:
                error_msg="Invalid Password"
                msg={'error':error_msg}
                return render(request,'dem1/stulogin.html',msg)
        else:
            error_msg="Invalid ID"
            msg={'error':error_msg}
            return render(request,'dem1/stulogin.html')


#for index4.html
def studentmain(request):
    return render(request,"dem1/index4.html")

#for adminpanel
def adminpanel(request):
    return render(request,"dem1/index8.html")

def adminpage(request):
    return render(request,'dem1/index9.html')