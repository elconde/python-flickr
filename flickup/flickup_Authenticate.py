"""Authenticate the application"""
import requests_oauthlib


REQUEST_TOKEN_URL = 'https://www.flickr.com/services/oauth/request_token'
KEY = '0bb57ec4e4e4287e4f10a8e6f4dd9ef2'
SECRET = '204a435d30fdd09e'


def authenticate():
    """Authenticate the Flickr session"""
    flickr = requests_oauthlib.OAuth1Session(
        KEY, client_secret=SECRET, callback_uri='http://www.nytimes.com'
    )
    print(flickr.fetch_request_token(REQUEST_TOKEN_URL))
    # authorization_url = flickr.authorization_url(authorization_base_url)
    # print('Please go here and authorize,', authorization_url)
