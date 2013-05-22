from allauth.socialaccount import providers
from allauth.socialaccount.providers.base import ProviderAccount
from allauth.socialaccount.providers.oauth2.provider import OAuth2Provider 

class RedditAccount(ProviderAccount):
    def get_profile_url(self):
        return self.account.extra_data.get('permalink_url')

    def get_avatar_url(self):
        return self.account.extra_data.get('avatar_url')

    def to_str(self):
        dflt = super(RedditAccount, self).to_str()
        full_name = self.account.extra_data.get('full_name')
        username = self.account.extra_data.get('username')
        return full_name or username or dflt

class RedditProvider(OAuth2Provider):
    id = 'redditprovider'
    name = 'Reddit'
    package = 'redditprovider'
    account_class = RedditAccount

    def get_default_scope(self):
        scope = []
        scope.append('identity')
        return scope

    def get_auth_params(self):
        settings = self.get_settings()
        return settings.get('AUTH_PARAMS', {'state': 'uniqueKey'})

        
providers.registry.register(RedditProvider)