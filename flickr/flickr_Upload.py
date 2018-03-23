"""Tools for uploading photos"""
import os
import flickr
import xml.dom.minidom

UPLOAD_URL = 'https://up.flickr.com/services/upload'
LOGGER = flickr.get_logger('upload')


def upload_photos(photo_file_names, photoset_id=None, session=None):
    """Upload these photos. Optionally add them to the photoset using
    photoset_id"""
    for photo_file_name in photo_file_names:
        assert os.path.isfile(photo_file_name), (
            'No such file: '+photo_file_name
        )
    if not session:
        session = flickr.flickr_session()
    photo_ids = [
        xml.dom.minidom.parseString(
            upload_photo(photo_file_name, session).text
        ).getElementsByTagName('photoid')[0].childNodes[0].data
        for photo_file_name in photo_file_names
    ]
    if not photoset_id:
        return
    # Add photos to photo set
    for photo_id in photo_ids:
        LOGGER.info('Adding %s to photoset %s', photo_id, photoset_id)
        flickr.photosets_add_photo(photoset_id, photo_id, session)


def upload_photo(photo_file_name, session):
    """Upload a single photo. Called from upload_photos"""
    LOGGER.info('Uploading %s', photo_file_name)
    return session.post(
        UPLOAD_URL,
        files={'photo': open(photo_file_name, 'rb')}
    )
