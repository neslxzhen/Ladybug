import pwd
from requests_oauthlib import OAuth1Session
from models.api.api import API


class Twitter(API):
    def __init__(self):
        super().__init__()
        tokens=self.get_tokens()
        print('Please go here and authorize,', f"https://api.twitter.com/oauth/authorize?oauth_token={tokens.get('oauth_token')}")
        self.oauth = OAuth1Session(pwd.TWITTER_KEY,
                                   client_secret=pwd.TWITTER_SECRET,
                                   resource_owner_key=tokens.get("oauth_token"),
                                   resource_owner_secret=tokens.get("oauth_token_secret"),
                                   verifier=super().get_code())
        tokens=self.oauth.fetch_access_token("https://api.twitter.com/oauth/access_token")

        r = self.oauth.get("https://api.twitter.com/1.1/statuses/home_timeline.json").content
        print(r)

    def get_tokens(self):
        return OAuth1Session(pwd.TWITTER_KEY, client_secret=pwd.TWITTER_SECRET).fetch_request_token("https://api.twitter.com/oauth/request_token")

