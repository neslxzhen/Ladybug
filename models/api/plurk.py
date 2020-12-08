import pwd
from requests_oauthlib import OAuth1Session

oauth_tokens = OAuth1Session(pwd.PLURK_KEY,client_secret=pwd.PLURK_SECRET).fetch_request_token("https://www.plurk.com/OAuth/request_token")
print('Please go here and authorize,', f"https://www.plurk.com/OAuth/authorize?oauth_token={oauth_tokens.get('oauth_token')}")
code = input('Paste the authentication Code here:')

oauth = OAuth1Session(pwd.PLURK_KEY,
                          client_secret=pwd.PLURK_SECRET,
                          resource_owner_key=oauth_tokens.get("oauth_token"),
                          resource_owner_secret=oauth_tokens.get("oauth_token_secret"),
                          verifier=code)
oauth_tokens=oauth.fetch_access_token("https://www.plurk.com/OAuth/access_token")

r = oauth.get("https://www.plurk.com/APP/Users/me").content
print(r)
