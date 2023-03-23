from django.contrib import messages
from django.shortcuts import render, redirect

from newapp.forms import WorkForm, workregistForm, FeedBack, NotificationForm, BillingForm
from newapp.models import work, workerregist, Feedback, Notification, Appointment, Bill


def corona(request):
    return render(request,'corona/corona.html')



def test(request):
    return render(request,'admin/test.html')

def add_work(request):
    form = WorkForm()
    print(form)
    print("ok")
    if request.method == 'POST':
        form = WorkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('views_work')
    return render(request, "admin/addwork.html", {'form': form})



def views_work(request):
    data = work.objects.all()
    return render(request, 'admin/worksview.html', {"data": data})


def delete(request,id):
    if request.method == 'POST':
        work.objects.get(id=id).delete()
        return redirect('views_work')

def views_workers(request):
    data = workerregist.objects.all()
    return render(request,'admin/workersview.html',{"data": data})



def dlte(request, id, user=None):
    if request.method == 'POST':
        user.objects.get(id=id).delete()
        return redirect('views_workers')

def update(request, id):
    data = workerregist.objects.get(id=id)
    form = workregistForm(instance=data)
    if request.method == 'POST':
        form = workregistForm(request.POST,request.FILES, instance=data)
        if form.is_valid():
            form.save()
            return redirect('views_workers')
    return render(request, "admin/workersupdate.html", {'form': form})



def Views_AdminFedback(request):
    data = Feedback.objects.all()
    return render(request,'admin/feedbackviews.html', {"data": data})

def ReplayFeedback(request,id):
    feedback = Feedback.objects.get(id=id)
    if request.method == 'POST':
        r = request.POST.get('replay')
        feedback.replay = r
        feedback.save()
        messages.info(request,"replay for messages")
        return redirect('Views_AdminFedback')
    return render(request,'admin/feedbackreplay.html', {"form": feedback})


def AddNotification(request):
    form = NotificationForm()

    if request.method == 'POST':
        form = NotificationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('adminviewnoti')

    return render(request,'admin/addnotification.html',{'form': form})

def adminviewnoti(request):
    data = Notification.objects.all()

    return render(request, 'admin/adminviewnoti.html', {"data": data})


def deletenotif(request,id):
    if request.method == 'POST':
        Notification.objects.get(id=id).delete()
        return redirect('adminviewnoti')

def View_Booking(request):
    data = Appointment.objects.all()
    return render(request,'admin/viewbookings.html' ,{"data": data})

def Booking_Accept(request,id):
    data = Appointment.objects.get(id=id)
    data.status = 1
    data.save()

    messages.info(request,'appointment accepted')

    return redirect('View_Booking')

def Booking_Reject(request,id):
    data = Appointment.objects.get(id=id)
    data.status = 2
    data.save()

    messages.info(request,"appointment rejected")

    return redirect('View_Booking')



def Bill_Settlememnt(request):
    form = BillingForm()

    if request.method == 'POST':
        form = BillingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('View_Booking')

    return render(request, 'admin/Billsetlememnt.html', {'form': form})

