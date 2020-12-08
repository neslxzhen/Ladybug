from requests_oauthlib import OAuth2Session
from requests_oauthlib.compliance_fixes import facebook_compliance_fix
import pwd
from models.api.api import API


class Facebook(API):
    def __init__(self):
        super().__init__()
        redirect_uri = 'https://localhost:3000/'
        facebook = facebook_compliance_fix(OAuth2Session(pwd.FB_ID, redirect_uri=redirect_uri))
        authorization_url, state = facebook.authorization_url('https://www.facebook.com/dialog/oauth')
        print('Please go here and authorize,', authorization_url)
        redirect_response = input('Paste the full redirect URL here:')

        facebook.fetch_token('https://graph.facebook.com/oauth/access_token', client_secret=pwd.FB_SECRET,
                             authorization_response=redirect_response)

        r = facebook.get('https://graph.facebook.com/me?').content
        print(r)

    def get_tokens(self):
        return OAuth1Session(pwd.TWITTER_KEY, client_secret=pwd.TWITTER_SECRET).fetch_request_token("https://api.twitter.com/oauth/request_token")

