"""Authenticate the application"""
import pickle
import requests_oauthlib
import os


REQUEST_TOKEN_URL = 'https://www.flickr.com/services/oauth/request_token'
KEY = '0bb57ec4e4e4287e4f10a8e6f4dd9ef2'
SECRET = '204a435d30fdd09e'
AUTH_BASE_URL = 'https://www.flickr.com/services/oauth/authorize'
ACCESS_TOKEN_URL = 'https://www.flickr.com/services/oauth/access_token'
FLICKR_TOKEN_FILENAME = os.path.expanduser('~/.flickr')


def flickr_session():
    """Get a Flickr session, authenticating if necessary."""
    if os.path.isfile(FLICKR_TOKEN_FILENAME):
        with open(FLICKR_TOKEN_FILENAME, 'rb') as f_open:
            access_token = pickle.load(f_open)
            return requests_oauthlib.OAuth1Session(
                client_key=KEY, client_secret=SECRET,
                resource_owner_key=access_token['oauth_token'],
                resource_owner_secret=access_token['oauth_token_secret']
            )
    else:
        flickr = requests_oauthlib.OAuth1Session(
            client_key=KEY, client_secret=SECRET,
            callback_uri='http://127.0.0.1/cb',
        )
        flickr.fetch_request_token(REQUEST_TOKEN_URL)
        authorization_url = flickr.authorization_url(AUTH_BASE_URL)
        print('Please go here and authorize,', authorization_url)
        flickr.parse_authorization_response(
            input('Paste the full redirect URL here: ')
        )
        with open(FLICKR_TOKEN_FILENAME, 'wb') as f_write:
            token = flickr.fetch_access_token(ACCESS_TOKEN_URL)
            print(token, type(token))
            pickle.dump(token, f_write)
        return flickr
