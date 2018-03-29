"""Flickr Python package"""

from .flickr_Logging import get_logger
from .flickr_Authenticate import flickr_session, REST_URL
from .flickr_Upload import upload_photos
from .flickr_Photosets import photsets_get_list, photosets_add_photo

__version__ = '1.1.2'
