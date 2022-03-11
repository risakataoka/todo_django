from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse, HttpRequest
from .models import daily, reminder, objective, done
from django.views.generic import ListView
import datetime


class IndexView(ListView):
    template_name = 'lists/index.html'
    context_object_name = 'daily_list'
    model = daily

    def get_context_data(self, **kwargs):
        # 本日の日付を文字列で取得
        today_date = datetime.date.today()
        yyyymmdd = today_date.strftime('%Y%m%d')

        # doneリストの数を確認
        done_lists = done.objects.filter(date_str=yyyymmdd)
        done_lists_count = done_lists.count()
        if done_lists_count >= 5:
            is_achived_done = True
        else:
            is_achived_done = False

        context = super(IndexView, self).get_context_data(**kwargs)
        context.update({
            'reminder_list': reminder.objects.all(),
            'objective_list': objective.objects.all(),
            'done_list': done_lists,
            'achivement_done': is_achived_done,
        })
        return context

    def get_queryset(self):
        return daily.objects.all()


index = IndexView.as_view()


def daily_record(request):
    if request.method == 'POST':
        if 'delete' in request.POST:
            deleteID = request.POST.get('delete')
            record = daily.objects.get(id=deleteID)
            record.delete()
        elif 'done' in request.POST:
            today_date = datetime.date.today()
            yyyymmdd = today_date.strftime('%Y%m%d')

            deleteID = request.POST.get('done')
            daily_object = daily.objects.get(id=deleteID)
            daily_content = daily_object.content
            done.objects.create(content=daily_content, date_str=yyyymmdd)

            record = daily.objects.get(id=deleteID)
            record.delete()

    return redirect('/lists/')


def reminder_record(request):
    if request.method == 'POST':
        if 'delete' in request.POST:
            deleteID = request.POST.get('delete')
            record = reminder.objects.get(id=deleteID)
            record.delete()

    return redirect('/lists/')


def objective_record(request):
    if request.method == 'POST':
        if 'delete' in request.POST:
            deleteID = request.POST.get('delete')
            record = objective.objects.get(id=deleteID)
            record.delete()

    return redirect('/lists/')


def add_daily_record(request):
    return render(request, 'lists/add_daily_record.html')


def save_daily_record(request):
    form_content = request.POST.get('content')
    daily.objects.create(content=form_content)
    return redirect('/lists/')


def add_reminder_record(request):
    return render(request, 'lists/add_reminder_record.html')


def save_reminder_record(request):
    form_content = request.POST.get('content')
    reminder.objects.create(content=form_content)
    return redirect('/lists/')


def add_objective_record(request):
    return render(request, 'lists/add_objective_record.html')


def save_objective_record(request):
    form_content = request.POST.get('content')
    objective.objects.create(content=form_content)
    return redirect('/lists/')
