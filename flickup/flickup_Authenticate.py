"""Authenticate the application"""
import pickle
import requests_oauthlib
import os


REQUEST_TOKEN_URL = 'https://www.flickr.com/services/oauth/request_token'
KEY = '0bb57ec4e4e4287e4f10a8e6f4dd9ef2'
SECRET = '204a435d30fdd09e'
AUTH_BASE_URL = 'https://www.flickr.com/services/oauth/authorize'
ACCESS_TOKEN_URL = 'https://www.flickr.com/services/oauth/access_token'
FLICKUP_TOKEN_FILENAME = os.path.expanduser('~/.flickup')
UPLOAD_URL = 'https://up.flickr.com/services/upload'


def flickr_session():
    """Get a Flickr session, authenticating if necessary."""
    if os.path.isfile(FLICKUP_TOKEN_FILENAME):
        with open(FLICKUP_TOKEN_FILENAME, 'rb') as f_open:
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
        with open(FLICKUP_TOKEN_FILENAME, 'wb') as f_write:
            token = flickr.fetch_access_token(ACCESS_TOKEN_URL)
            print(token, type(token))
            pickle.dump(token, f_write)
        return flickr


def test_login(session=None):
    """Run the flickr.test.login method"""
    if not session:
        session = flickr_session()
    print(
        session.get(
            'https://api.flickr.com/services/rest',
            params={'method': 'flickr.test.login'}
        ).content
    )
    return session


def upload_photos(photo_file_names, session=None):
    for photo_file_name in photo_file_names:
        assert os.path.isfile(photo_file_name), (
            'No such file: '+photo_file_name
        )
    if not session:
        session = flickr_session()
    for photo_file_name in photo_file_names:
        upload_photo(photo_file_name, session)


def upload_photo(photo_file_name, session):
    """Upload a single photo. Called from upload_photos"""
    print(
        session.post(
            UPLOAD_URL,
            files={'photo': open(photo_file_name, 'rb')}
        ).content
    )
