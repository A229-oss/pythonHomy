from django.urls import path

from newapp import views, workerviews, adminviews, costumerviews

urlpatterns = [
   path('',views.hom,name='hom'),
   path('log',views.log,name='log'),
   path('reg', views.reg, name='reg'),





   ##### admin  ###########
   path('corona',adminviews.corona,name='corona'),

   path('add_work', adminviews.add_work, name='add_work'),
   path("test",adminviews.test,name="test"),
   path('views_work',adminviews.views_work,name='views_work'),
   path('delete/<int:id>',adminviews.delete,name='delete'),
   path('views_workers', adminviews.views_workers, name='views_workers'),
   path('delete/<int:id>',adminviews.delete,name='delete'),
   path('update/<int:id>', adminviews.update, name='update'),
   path('Views_AdminFedback', adminviews.Views_AdminFedback, name='Views_AdminFedback'),
   path('ReplayFeedback/<int:id>',adminviews.ReplayFeedback,name='ReplayFeedback'),
   path('AddNotification',adminviews.AddNotification,name='AddNotification'),
   path('adminviewnoti',adminviews.adminviewnoti,name='adminviewnoti'),
   path('deletenotif/<int:id>',adminviews.deletenotif,name='deletenotif'),
   path('View_Booking', adminviews.View_Booking, name='View_Booking'),
   path('Booking_Accept/<int:id>',adminviews.Booking_Accept,name='Booking_Accept'),
   path('Booking_Reject/<int:id>',adminviews.Booking_Reject,name='Booking_Reject'),
   path("Bill_Settlememnt",adminviews.Bill_Settlememnt,name="Bill_Settlememnt"),






   ##### cotumer #########

   path('customer',costumerviews.customer,name='customer'),
   path('costumerreg',costumerviews.costumerreg,name='costumerreg'),
   path('costumerbase',costumerviews.costumerbase,name='costumerbase'),
   path('Fedback_customer',costumerviews.Fedback_customer,name='Fedback_customer'),
   path('Feedback_View',costumerviews.Feedback_View,name='Feedback_View'),
   path('Customer_Notif',costumerviews.Customer_Notif,name='Customer_Notif'),
   path('Appoint_submit',costumerviews.Appoint_submit,name='Appoint_submit'),
   path('Booking/<int:id>',costumerviews.Booking,name="Booking"),
   path('Status_Appoint',costumerviews.Status_Appoint,name="Status_Appoint"),
   path('Custom_Billing',costumerviews.Custom_Billing,name="Custom_Billing"),
   path('Payin_Direct/<int:id>',costumerviews.Payin_Direct,name='Payin_Direct'),
   path('Credit_Card/<int:id>',costumerviews.CredtCard_view,name="Credit_Card"),
   path('CreditCard_Add/<int:id>',costumerviews.CreditCard_Add,name='CreditCard_Add'),
   path("CredtCard_view",costumerviews.CredtCard_view,name='CredtCard_view'),
   path("Billing_Section",costumerviews.Billing_Section, name="Billing_Section"),






   ########worker########

   path('workerlanding',workerviews.working,name='working'),
   path('work',workerviews.work,name='work'),
   path('worker',workerviews.worker,name='worker'),
   path('timeshedule',workerviews.timeshedule,name='timeshedule'),
   path('viewshedule', workerviews.viewshedule, name='viewshedule'),
   path('Worker_notif',workerviews.Worker_notif,name='Worker_notif'),









]
