from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^listings/', views.search, name='search'),
    url(r'^forms/plot/', views.plot_form),
    url(r'^forms/booking/', views.booking_form),
    url(r'^forms/applicant/', views.applicant_form),
    url(r'^plot/(?P<pk>[\w-]+)/$', views.plot_detail, name='plotdetail'),
    url(r'^plot/(?P<pk>[\w-]+)/edit/$', views.plot_update, name='plotupdate'),
    url(r'^plot/(?P<pk>[\w-]+)/delete/$', views.plot_delete, name='plotdelete'),
    url(r'^booking/(?P<pk>[\w-]+)/$', views.booking_detail, name='bookingdetail'),
    url(r'^booking/(?P<pk>[\w-]+)/edit/$', views.booking_update, name='bookingupdate'),
    url(r'^booking/(?P<pk>[\w-]+)/delete/$', views.booking_delete, name='bookingdelete'),
    url(r'^applicant/(?P<pk>[\w-]+)/$', views.applicant_detail, name='applicantsdetail'),
    url(r'^applicant/(?P<pk>[\w-]+)/edit/$', views.applicant_update, name='applicantupdate'),
    url(r'^applicant/(?P<pk>[\w-]+)/delete/$', views.applicant_delete, name='applicantdelete'),
    url(r'^account/(?P<pk>[\w-]+)/$', views.profile, name='profile'),
]
