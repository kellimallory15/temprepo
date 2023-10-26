from django.template.defaulttags import url
from django.urls import path, include, re_path
from django.views.i18n import JavaScriptCatalog
from django.views.static import serve
from django.contrib import admin

from . import views

urlpatterns = [path('admin/', admin.site.urls),
               path('', views.index, name='index'),
               path('senior_about/', views.senior_about, name='senior_about'),
               path('family_about/', views.family_about, name='family_about'),
               path('calendar/', views.calendar, name="calendar"),
               path('couples_enagagements_about', views.couples_engagements_about, name='couples_engagements_about'),
               path('calendar/<int:pk>', views.CalendarView.as_view(), name='couples_engagements_calendar'),
               path('cart/', views.view_cart, name='view_cart'),
               path('', include('payments.urls')),
               path('create_booking/', views.create_booking, name='create_booking'),
               path('input_order_information/', views.create_booking, name="input_order_information"),  # new
               ]

# If you already have a js_info_dict dictionary, just add
# 'recurrence' to the existing 'packages' tuple.
js_info_dict = {
    'packages': ('recurrence', ),
}

# jsi18n can be anything you like here
#urlpatterns += [
#    url(r'^jsi18n/$', JavaScriptCatalog.as_view(), js_info_dict),
#]

# Pages we need
# Index.html homepage with about us, our mission, and view package types (kelli)
# create a senior portraits page that links to the calendar page, available on nav bar (kelli)
# create a booking calendar page for the senior portraits avaialble dates (Alex)
# create a wedding portraits page that links to the calendar page, available on nav bar (kelli)
# create a booking calendar page for the wedding portraits avaialble dates (Alex)
# create a couples & engagements portraits page that links to the calendar page, available on nav bar (kelli)
# create a booking calendar page for the couples/engagements portraits avaialble dates (Alex)
# create a page that shows that you have a portrait package in your cart (Erik)
# create a page that allows you to input order information (Erik)
# create a page that shows that the booking was confirmed and that gives you a randomized confirmation number (Andrew)
