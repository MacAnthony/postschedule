import praw
from sketchdailyschedule.settings import CLIENT_ID, CLIENT_SECRET, REDIRECT_URL
from django.shortcuts import render_to_response



def reddit_auth(request):
    r = praw.Reddit('OAuth Sketchdaily Scheduler u/davidwinters ver 0.1. See '
                'https://praw.readthedocs.org/en/latest/'
                'pages/oauth.html for more info.')
    r.set_oauth_app_info(CLIENT_ID, CLIENT_SECRET, REDIRECT_URL)
    link_no_refresh = r.get_authorize_url('UniqueKey')

    return render_to_response('forms/login.html', {'link': link_no_refresh})

def reddit_finish(request, **kwargs):
    state = kwargs['state']
    code = kwargs['code']
    info = r.get_access_information(code)
    user = r.get_me()

    return render_to_response('base.html', {'user': user})