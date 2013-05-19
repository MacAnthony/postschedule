from django.core.management.base import BaseCommand, CommandError
from sketchdailyschedule.settings import REDDIT_USER, REDDIT_PASSWD
from schedule.models import Post
import praw

from datetime import date

class Command(BaseCommand):
    help = 'Post the DailyTheme to SketchDaily'

    def handle(self, *args, **options):
        p = Post.objects.get(date=date.today())

        r = praw.Reddit(user_agent='Sketchdaily Schedule Bot 1.0 by /u/davidwinters github.com/davidwinters/postschedule')
        r.login(REDDIT_USER, REDDIT_PASSWD)
        r.submit('sketchdailyCANADA', p.title, text=p.text)

        self.stdout.write('Theme Posted by %s \n' % REDDIT_USER)