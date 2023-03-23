from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from newapp.forms import workregistForm, registForm, LoginRegister


# Create your views here.
#### landing page#########
def hom(request):
    return render(request,'homy.html')

####loging page############

def log(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        print(username)
        password = request.POST.get('pass')
        print(password)
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request,user)

            if user.is_staff:
                return redirect('corona')
            elif user.is_worker:
                return redirect('working')
            elif user.is_customer:
                return redirect('customer')

            else:
                messages.info(request,'Invalid Credentials')

    return render(request,'login.html')


#####register home######
def reg(request):
    form1 = LoginRegister()
    form2 = workregistForm()

    if request.method == 'POST':
        form1 = registForm(request.POST)
        form2 = LoginRegister(request.POST)

        if form1.is_valid() and form2.is_valid():
            data = form1.save(commit=False)
            data.is_worker = True
            data.save()
            user1 = form2.save(commit=False)
            user1.user = data
            return redirect("log")

    return render(request,"register/registerbase.html",{"form1" : form1 ,"form2" : form2})



