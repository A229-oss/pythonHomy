from django.shortcuts import render, redirect

from newapp.forms import LoginRegister, workregistForm, TimeForm
from newapp.models import workerregist, Schedule, Notification


def worker(request):
    return render(request,'workertemp/workerbase.html')

def working(request):
    return render(request,'workertemp/workerlanding.html')


def work(request):
    form1 = LoginRegister()
    form2 = workregistForm()

    if request.method == 'POST':
        form1 = LoginRegister(request.POST)
        form2 = workregistForm(request.POST, request.FILES)

        if form1.is_valid() and form2.is_valid():
            data = form1.save(commit=False)
            data.is_worker = True
            data.save()
            user1 = form2.save(commit=False)
            user1.user = data
            user1.save()
            return redirect("log")

    return render(request,"workertemp/worker.html", {"form1": form1, "form2": form2})


def timeshedule(request):
    form = TimeForm()
    if request.method == "POST":
        form = TimeForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.workers = workerregist.objects.get(user=request.user)
            form.save()
            return redirect('viewshedule')
    return render(request,'workertemp/timeshedule.html',{'form': form})


def viewshedule(request):

    data1 = workerregist.objects.get(user=request.user)

    data2 = Schedule.objects.filter(workers=data1)


    return render(request,"workertemp/viewshedule.html",{'data2': data2})

def Worker_notif(request):
    data = Notification.objects.all()

    return render(request, 'workertemp/workernoti.html', {"data": data})

