from django.urls import path
from . import views

from django.contrib import admin  # 追加
from django.views.generic import TemplateView  # 追加

app_name = 'lists'
urlpatterns = [
    path('', views.index, name='index'),
    path('daily_record', views.daily_record, name='daily_record'),
    path('reminder_record', views.reminder_record, name='reminder_record'),
    path('objective_record', views.objective_record, name='objective_record'),
    path('add_daily_record', views.add_daily_record, name='add_daily_record'),
    path('save_daily_record', views.save_daily_record, name='save_daily_record'),
    path('add_reminder_record', views.add_reminder_record,
         name='add_reminder_record'),
    path('save_reminder_record', views.save_reminder_record,
         name='save_reminder_record'),
    path('add_objective_record', views.add_objective_record,
         name='add_objective_record'),
    path('save_objective_record', views.save_objective_record,
         name='save_objective_record'),
]
