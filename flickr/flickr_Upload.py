"""Tools for uploading photos"""
import os
import flickr
import xml.dom.minidom
import xml.parsers.expat
import time
import sys

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
    photo_ids = []
    for photo_file_name in photo_file_names:
        response = upload_and_get_response(photo_file_name, session)
        document = xml.dom.minidom.parseString(response)
        photo_ids.append(
            document.getElementsByTagName('photoid')[0].childNodes[0].data
        )
    if not photoset_id:
        return
    # Add photos to photo set
    for photo_id in photo_ids:
        LOGGER.info('Adding %s to photoset %s', photo_id, photoset_id)
        flickr.photosets_add_photo(photoset_id, photo_id, session)


def upload_and_get_response(photo_file_name, session):
    """Upload the photo and get the response. Try again if necessary."""
    for attempt in range(3):
        response = upload_photo(photo_file_name, session).text
        if '502 Bad Gateway' not in response:
            return response
        LOGGER.warning(
            'Received 502 Bad Gateway, '
            'trying again in three seconds ({}/3)...'.format(attempt+1)
        )
        if attempt == 2:
            LOGGER.critical('Could not connect')
            sys.exit(48)
        time.sleep(3)


def upload_photo(photo_file_name, session):
    """Upload a single photo. Called from upload_photos"""
    LOGGER.info('Uploading %s', photo_file_name)
    return session.post(
        UPLOAD_URL,
        files={'photo': open(photo_file_name, 'rb')}
    )
