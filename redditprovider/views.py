import requests
import praw, json, inspect

from allauth.socialaccount.providers.oauth2.views import (OAuth2Adapter, OAuth2LoginView, OAuth2CallbackView, OAuth2View)
from allauth.socialaccount.providers.oauth2.client import (OAuth2Client,
                                                           OAuth2Error)
from allauth.socialaccount.models import SocialAccount, SocialLogin, SocialToken
from allauth.socialaccount.adapter import get_adapter
from allauth.socialaccount.helpers import render_authentication_error
from allauth.socialaccount.helpers import complete_social_login
from django.http import HttpResponseRedirect
import logging
from django.core import serializers

from .provider import RedditProvider

class RedditOAuth2Adapter(OAuth2Adapter):
    provider_id = RedditProvider.id
    access_token_url = 'https://ssl.reddit.com/api/v1/access_token'
    authorize_url = 'https://ssl.reddit.com/api/v1/authorize'
    profile_url = 'https://oauth.reddit.com/api/v1/me.json'

    def complete_login(self, request, app, token, **kwargs):
        userob = kwargs["user"]
        extra = kwargs["extra"]
        extra_info = []
        for item in extra:

            item_serial = item.__dict__['display_name']
            extra_info.append(item_serial)
        #extra = serializers.serialize("json", extra)
        logging.debug(extra_info)
        #extra = json.dumps(extra)
        # auth = ('bearer', token.token)
        # resp = requests.get(self.profile_url,
        #                     params={ 'oauth_token': token.token })
        #extra_data = resp.json()
        # uid = str(extra_data['id'])
        user = get_adapter() \
            .populate_new_user(name=userob.name,
                               username=userob.name,
                               email=userob.name)
        account = SocialAccount(user=user,
                                uid=userob.id,
                                extra_data=extra_info,
                                provider=self.provider_id)
        return SocialLogin(account)

class RedditOAuth2LoginView(OAuth2LoginView):
    def dispatch(self, request):
        app = self.adapter.get_provider().get_app(self.request)
        client = self.get_client(request, app)
        client.state = SocialLogin.marshall_state(request)
        try:
            return HttpResponseRedirect(client.get_redirect_url())
        except OAuth2Error:
            return render_authentication_error(request)

class RedditOAuth2CallbackView(OAuth2CallbackView):
    def dispatch(self, request):
        if 'error' in request.GET or not 'code' in request.GET:
            # TODO: Distinguish cancel from error
            return render_authentication_error(request)
        app = self.adapter.get_provider().get_app(self.request)
        client = self.get_client(request, app)
        try:
            r = praw.Reddit('OAuth Sketchdaily Schedule  by u/davidwinters ver 0.1.')
            r.set_oauth_app_info(client.consumer_key, client.consumer_secret, 'http://themes.sketchdaily.net/accounts/redditprovider/login/callback/')
            access_token = r.get_access_information(request.GET['code'])
            user = r.get_me()
            extra = r.get_my_moderation()
            # access_token = client.get_access_token(request.GET['code'])
            token = SocialToken(token=access_token)
            #token = self.adapter.parse_token(access_token)
            token.app = app
            login = self.adapter.complete_login(request,
                                                app,
                                                token,
                                                response=access_token, user=user, extra=extra)
            token.account = login.account
            login.token = token
            login.state = SocialLogin.unmarshall_state(request.REQUEST
                                                       .get('uniqueKey'))
            return complete_social_login(request, login)
        except OAuth2Error:
            return render_authentication_error(request)


oauth2_login = RedditOAuth2LoginView.adapter_view(RedditOAuth2Adapter)
oauth2_callback = RedditOAuth2CallbackView.adapter_view(RedditOAuth2Adapter)
# oauth2_login = OAuth2LoginView.adapter_view(RedditOAuth2Adapter)
# oauth2_callback = OAuth2CallbackView.adapter_view(RedditOAuth2Adapter)
