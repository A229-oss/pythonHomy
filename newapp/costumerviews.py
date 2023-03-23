from django.contrib import messages
from django.shortcuts import render, redirect

from newapp.forms import workregistForm, registForm, LoginRegister, FeedBack, AppointmentForm, CreditForm, BillingForm
from newapp.models import Feedback, workerregist, regist, Notification, Schedule, Appointment, Bill, Creditcard


def costumerbase(request):
    return render(request, 'costumer/costumerbase.html.html')


def customer(request):
    return render(request, 'costumer/customerlanding.html')


def costumerreg(request):
    form1 = LoginRegister()
    form2 = registForm()

    if request.method == 'POST':
        form1 = LoginRegister(request.POST)
        form2 = registForm(request.POST)

        if form1.is_valid() and form2.is_valid():
            data = form1.save(commit=False)
            data.is_customer = True
            data.save()
            user1 = form2.save(commit=False)
            user1.user = data
            user1.save()
            return redirect("log")

    return render(request, "costumer/customer.html", {"form1": form1, "form2": form2})


def Fedback_customer(request):
    form = FeedBack()

    if request.method == 'POST':
        form = FeedBack(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.customer = regist.objects.get(user=request.user)
            form.save()
            messages.info(request, "feedback added succesfully")
            return redirect("Feedback_View")
    return render(request, 'costumer/feedback.html', {'form': form})


def Feedback_View(request):
    data1 = regist.objects.get(user=request.user)
    data2 = Feedback.objects.filter(customer=data1)

    return render(request, 'costumer/feedbackviewscustomer.html', {"data2": data2})


def Customer_Notif(request):
    data = Notification.objects.all()

    return render(request, 'costumer/customernoti.html', {"data": data})


def Appoint_submit(request):
    data2 = Schedule.objects.all()

    return render(request, 'costumer/appointment.html', {"data2": data2})


def Booking(request, id):
    s = Schedule.objects.get(id=id)
    print(s)
    c = regist.objects.get(user=request.user)
    print(c)

    appointment = Appointment.objects.filter(user=c, schedule=s)
    if appointment.exists():
        messages.info(request, "you have already requested appointment")
        return redirect("Appoint_submit")
    else:
        if request.method == 'POST':
            obj = Appointment()
            obj.user = c
            obj.schedule = s
            obj.save()
            messages.info(request, "appointment booked successfully")
    return render(request, "costumer/booking.html", {'schedule': s})


def Booking_Accepted(request, id):
    data = Appointment.objects.get(id=id)
    data.status = 1
    data.save()

    messages.info(request, 'appointment accepted')


def Booking_Rejected(request, id):
    data = Appointment.objects.get(id=id)
    data.status = 1
    data.save()

    messages.info(request, 'appointment rejected')
    return redirect(request, '')


def Status_Appoint(request):
    c = regist.objects.get(user=request.user)
    a = Appointment.objects.filter(user=c)

    return render(request, "costumer/statusappoint.html", {"appointment": a})


def Custom_Billing(request):
    data = Bill.objects.all()

    return render(request, "costumer/customerbillview.html", {"data": data})


def Billing_Section(request):
    data = Bill.objects.all()
    return render(request,"costumer/billingsection.html",{"data": data})


def Payin_Direct(request,id):
    data = Bill.objects.get(id=id)
    data.status = 2
    data.save()
    messages.info(request, "choose to pay fee directly")

    return redirect('Custom_Billing')


def CreditCard_Add(request,id):
    data = Bill.objects.get(id=id)
    form = CreditForm()

    if request.method == 'POST':
        b = request.POST.get('card')
        c = request.POST.get('cvv')
        d = request.POST.get('exp')
        Creditcard(card_no=b,card_cvv=c,expiry_date=d).save
        data.status = 1
        data.save()
        messages.info(request,"bill paid successfully")
        return redirect("Billing_Section")

    return render(request,"costumer/creditcardadd.html",{"form": form})


def CredtCard_view(request):

    data =Creditcard.objects.all()


    return render(request,"costumer/viewcreditcard.html",{"data" :data})
