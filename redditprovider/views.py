import requests
import praw

from allauth.socialaccount.providers.oauth2.views import (OAuth2Adapter, OAuth2LoginView, OAuth2CallbackView, OAuth2View)
from allauth.socialaccount.providers.oauth2.client import (OAuth2Client,
                                                           OAuth2Error)
from allauth.socialaccount.models import SocialAccount, SocialLogin
from allauth.socialaccount.adapter import get_adapter
from allauth.socialaccount.helpers import render_authentication_error
from allauth.socialaccount.helpers import complete_social_login


from .provider import RedditProvider

class RedditOAuth2Adapter(OAuth2Adapter):
    provider_id = RedditProvider.id
    access_token_url = 'https://ssl.reddit.com/api/v1/access_token'
    authorize_url = 'https://ssl.reddit.com/api/v1/authorize'
    profile_url = 'https://oauth.reddit.com/api/v1/me.json'

    def complete_login(self, request, app, token, **kwargs):
        auth = ('bearer', token.token)
        resp = requests.get(self.profile_url,
                            params={ 'oauth_token': token.token })
        extra_data = resp.json()
        uid = str(extra_data['id'])
        user = get_adapter() \
            .populate_new_user(name=extra_data.get('full_name'),
                               username=extra_data.get('username'),
                               email=extra_data.get('email'))
        account = SocialAccount(user=user,
                                uid=uid,
                                extra_data=extra_data,
                                provider=self.provider_id)
        return SocialLogin(account)

oauth2_login = OAuth2LoginView.adapter_view(RedditOAuth2Adapter)
oauth2_callback = OAuth2CallbackView.adapter_view(RedditOAuth2Adapter)