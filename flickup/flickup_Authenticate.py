"""Authenticate the application"""
import requests_oauthlib


REQUEST_TOKEN_URL = 'https://www.flickr.com/services/oauth/request_token'
KEY = '0bb57ec4e4e4287e4f10a8e6f4dd9ef2'
SECRET = '204a435d30fdd09e'
AUTH_BASE_URL = 'https://www.flickr.com/services/oauth/authorize'
ACCESS_TOKEN_URL = 'https://www.flickr.com/services/oauth/access_token'


def authenticate():
    """Authenticate the Flickr session"""
    flickr = requests_oauthlib.OAuth1Session(
        KEY, client_secret=SECRET, callback_uri='http://127.0.0.1/cb',
    )
    print(flickr.fetch_request_token(REQUEST_TOKEN_URL))
    authorization_url = flickr.authorization_url(AUTH_BASE_URL)
    print('Please go here and authorize,', authorization_url)
    redirect_response = input('Paste the full redirect URL here: ')
    flickr.parse_authorization_response(redirect_response)
    print(flickr.fetch_access_token(ACCESS_TOKEN_URL))
    print(flickr.get('https://api.flickr.com/services/rest', params={'method': 'flickr.test.login'}).content)