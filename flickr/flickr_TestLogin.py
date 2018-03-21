"""Run the flickr.test.login method"""
import flickr


def test_login(session=None):
    """Run the flickr.test.login method"""
    if not session:
        session = flickr.flickr_session()
    print(
        session.get(
            'https://api.flickr.com/services/rest',
            params={'method': 'flickr.test.login'}
        ).content
    )
    return session
