"""Implement the flickr.photosets functions"""
import flickr


def photsets_get_list(session=None):
    """Implements flickr.photosets.getList
    https://www.flickr.com/services/api/flickr.photosets.getList.html"""
    if not session:
        session = flickr.flickr_session()
    print(
        session.get(
            flickr.REST_URL, params={'method': 'flickr.photosets.getList'}
        ).text
    )
    return session


def photosets_add_photo(photoset_id, photo_id, session=None):
    """Implements flickr.photosets.addPhoto
    https://www.flickr.com/services/api/flickr.photosets.addPhoto.html"""
    if not session:
        session = flickr.flickr_session()
    session.post(
        flickr.REST_URL, data={
            'photoset_id': photoset_id, 'photo_id': photo_id,
            'method': 'flickr.photosets.addPhoto'
        }
    )


if __name__ == '__main__':
    photsets_get_list()
