"""Implement the flickr.photosets functions"""
import flickr
import xml.dom.minidom


def photsets_get_list(session=None):
    """Implements flickr.photosets.getList
    https://www.flickr.com/services/api/flickr.photosets.getList.html"""
    if not session:
        session = flickr.flickr_session()
    print(
        session.get(
            'https://api.flickr.com/services/rest',
            params={'method': 'flickr.photosets.getList'}
        ).text
    )
    return session


if __name__ == '__main__':
    photsets_get_list()
