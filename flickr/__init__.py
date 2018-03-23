"""Flickr Python package"""

from .flickr_Logging import get_logger
from .flickr_Authenticate import flickr_session
from .flickr_Upload import upload_photos
from .flickr_Photosets import photsets_get_list

__version__ = '0.0.1'