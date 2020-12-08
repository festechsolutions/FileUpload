from django.shortcuts import render,redirect
# from django.contrib.auth.models import User
# from django.contrib import auth
from .models import Vacancie,Candidate

# Create your views here.


def home(request):
    a = vacancie.objects.all()
    return render(request,'home.html',{'data' : a})


# def signup(request):
#     if request.method=="POST":
#         if request.POST['password']==request.POST['conpassword']:
#             try:
#                 user=User.objects.get(username=request.POST['username'])
#                 return render(request,'register.html',{'error':'Username has already been taken'})
#             except User.DoesNotExist:
#                 user=User.objects.create_user(username=request.POST['username'],password=request.POST['password'])
#                 return redirect(home)
#         else:
#             return render(request,'register.html',{'error':'password does not matched'})
#     else:
#         return render(request,'register.html')



# def login(request):
#     if request.method == 'POST':
#         user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
#         if user is not None:
#             auth.login(request, user)
#             return redirect(home)
#         else:
#             return render(request, 'login.html',{'error':'username or password is incorrect.'})
#     else:
#         return render(request, 'login.html')




# def logout(request):
#     auth.logout(request)
#     return redirect(home)

def userJobForm(Request):
    a = Request.POST['ate']
    b = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    return render(Request,'userJobForm.html',{'data': a,'data1':b})



def userdata(request):
    if request.method == "POST":
        fn = request.POST["na"]
        ln = request.POST["la"]
        d = request.POST["dt"]
        p = request.POST["ph"]
        e = request.POST["em"]
        j = request.POST["jds"]
        w = request.POST["we"]
        file3 = request.FILES['fl']
        document = Candidate.objects.create(First_name=fn,Last_name=ln,DOB=d,phonenumber=p,mail_ID=e,experience=w,Position=j,resume=file3)
        document.save()
        return redirect(home)
