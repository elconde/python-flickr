"""Tools for uploading photos"""
import os
import flickr

UPLOAD_URL = 'https://up.flickr.com/services/upload'
LOGGER = flickr.get_logger('upload')


def upload_photos(photo_file_names, session=None):
    for photo_file_name in photo_file_names:
        assert os.path.isfile(photo_file_name), (
            'No such file: '+photo_file_name
        )
    if not session:
        session = flickr.flickr_session()
    for photo_file_name in photo_file_names:
        upload_photo(photo_file_name, session)


def upload_photo(photo_file_name, session):
    """Upload a single photo. Called from upload_photos"""
    LOGGER.info('Uploading %s', photo_file_name)
    session.post(
        UPLOAD_URL,
        files={'photo': open(photo_file_name, 'rb')}
    )
