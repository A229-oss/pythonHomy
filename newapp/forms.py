

from django.core.validators import EmailValidator

from django import forms
from django.contrib.auth.forms import UserCreationForm

from newapp.models import work, workerregist, Login, regist, Schedule, Feedback, Notification, Appointment, Bill, \
    Creditcard


class WorkForm(forms.ModelForm):

    class Meta:
        model = work
        fields = ('__all__')

class registForm(forms.ModelForm):
    class Meta:
        model = regist
        fields = ('Name','address','phone','email')



class workregistForm(forms.ModelForm):

    class Meta:
        model = workerregist
        fields = ('WorkerName','address','phone','email','work','profile')

class LoginRegister(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label="password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="confirm password", widget=forms.PasswordInput)

    class Meta:
        model = Login
        fields = ('username','password1','password2')


class dateinput(forms.DateInput):
    input_type = 'date'


class timeinput(forms.TimeInput):
    input_type = 'time'



class TimeForm(forms.ModelForm):
    date = forms.DateField(widget=dateinput)
    start_time=forms.TimeField(widget=timeinput)
    end_time=forms.TimeField(widget=timeinput)

    class Meta:
        model = Schedule
        fields = ('date','start_time','end_time','Work')




class FeedBack(forms.ModelForm):


    class Meta:
        model = Feedback
        fields = ('message',)




class FeedBackreplay(forms.ModelForm):


    class Meta:
        model = Feedback
        fields = ('__all__')

class NotificationForm(forms.ModelForm):

    class Meta:
        model = Notification
        fields = ('notification',)

class AppointmentForm(forms.ModelForm):

    class Meta:
        model = Appointment
        fields = ('status',)

class BillingForm(forms.ModelForm):

     class Meta:
         model = Bill
         fields = ("name","amount",)
#
class CreditForm(forms.ModelForm):

    class Meta:
        model = Creditcard
        fields = ("__all__")
