from django.core.management.base import BaseCommand, CommandError
from sketchdailyschedule.settings import REDDIT_USER, REDDIT_PASSWD
from schedule.models import Post
import praw

from datetime import date, timedelta

class Command(BaseCommand):
    help = 'Post the DailyTheme to SketchDaily'

    def handle(self, *args, **options):
        p = Post.objects.filter(date=date.today())

        if not p:
            thetitle = 'Your Mods Have Failed You'
            thetext = 'You Should Draw the Mods or post pics of yourself for others to draw'
        else:
            thetitle = p[0].title
            thetext = p[0].text + "\n ***** \n Theme  posted by " + p[0].user

        r = praw.Reddit(user_agent='Sketchdaily Schedule Bot 1.0 by /u/davidwinters github.com/davidwinters/postschedule')
        r.login(REDDIT_USER, REDDIT_PASSWD)
        r.submit('sketchdaily', thetitle, thetext)


        today = date.today() + timedelta(days=1)
        np = Post.objects.filter(date=today)

        if not np:
            r.send_message('/r/sketchdaily', 'no theme scheduled for tomorrow', 'please schedule a theme for tomorrow at http://themes.sketchdaily.net')

