from django.views.generic import CreateView, UpdateView
from schedule.models import Post
from schedule.htmlcalendar import PostCalendar
#calendar shit
from datetime import date
from dateutil.relativedelta import relativedelta

from django.shortcuts import render_to_response
from django.utils.safestring import mark_safe

# Create your views here.

class CreatePost(CreateView):
    template_name = "forms/form_create.html"
    context_object_name = "post"
    model = Post
    success_url = "/cal/"

    def get_initial(self):
        self.year = int(self.kwargs["year"])
        self.month = int(self.kwargs["month"])
        self.day = int(self.kwargs["day"])
        return { 'date': date(self.year, self.month, self.day) }

    def get_context_data(self, **kwargs):
        context = super(CreatePost, self).get_context_data(**kwargs)
        context['date_for_link'] = date(self.year,self.month,self.day)
        return context

class EditPost(UpdateView):
    template_name = "forms/form_edit.html"
    context_object_name = "post"
    model = Post
    success_url = "/cal/"
    def get_object(self, queryset=None):
        obj = Post.objects.get(id=self.kwargs['id'])
        return obj

# Calendar View
def calendar(request, year=date.today().strftime("%Y"), month=date.today().strftime("%m")):
  post_schedule = Post.objects.order_by('date').filter(
    date__year=int(year), date__month=int(month)
  )
  prev = date(int(year), int(month), 1) - relativedelta(months=1)
  next = date(int(year), int(month), 1) + relativedelta(months=1)

  cal = PostCalendar(post_schedule).formatmonth(int(year), int(month))
  return render_to_response('calendar/calendar.html', {'calendar': mark_safe(cal),'prev': prev, 'next': next})