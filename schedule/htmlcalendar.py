from calendar import HTMLCalendar
from itertools import groupby
from django.utils.html import conditional_escape as esc
from datetime import date

#this shit gets used in the view to make nice html calendar

class PostCalendar(HTMLCalendar):

    def __init__(self, posts):
        super(PostCalendar, self).__init__()
        self.posts = self.group_by_day(posts)
        self.setfirstweekday(6)

    def formatday(self, day, weekday):
        if day != 0:
            display_year = date(self.year, self.month, day).strftime("%Y")
            display_month = date(self.year, self.month, day).strftime("%m")
            display_day = date(self.year, self.month, day).strftime("%d")
	    displaydate = display_year + "-" + display_month + "-" + display_day
            cssclass = self.cssclasses[weekday]

            if date.today() == date(self.year, self.month, day):
                cssclass += ' today'
            if date.today() > date(self.year, self.month, day):
                cssclass += ' past'
            if (date.today() < date(self.year, self.month, day)) and (day not in self.posts):
                cssclass += ' empty'
                body = ['']
                body.append('<a class="btn btn-danger" href="/create/%s/%s/%s">Schedule Theme</a>' % (display_year, display_month, display_day))
                return self.day_cell(cssclass, '%d %s' % (day, ''.join(body)), displaydate)
            if day in self.posts:
                cssclass += ' filled'
                body = ['<ul>']
                for post in self.posts[day]:
                    body.append('<li data-id="%s">' % (post.id))
                    body.append(esc(post.title))
                    if date.today() > date(self.year, self.month, day):
                        buttonMessage = "View"
                    else:
                        buttonMessage = "Edit"
                    body.append('<br/><a class="btn btn-info btn-small" href="/update/%s/">%s</a>' % (post.id, buttonMessage))
                    body.append('</li>')
                body.append('</ul>')
                return self.day_cell(cssclass, '%d %s' % (day, ''.join(body)), displaydate)
            return self.day_cell(cssclass, day, displaydate)
        return self.day_cell('noday', '&nbsp;')

    def formatmonth(self, year, month):
        self.year, self.month = year, month
        return super(PostCalendar, self).formatmonth(year, month)

    def group_by_day(self, posts):
        field = lambda post: post.date.day
        return dict(
            [(day, list(items)) for day, items in groupby(posts, field)]
        )

    def day_cell(self, cssclass, body, displaydate=""):
        return '<td class="%s" data-date="%s">%s</td>' % (cssclass,displaydate, body)
