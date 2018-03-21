import flickr
import os

APPLE_DIR = '/home/media/photos/FIS Phone/DCIM/100APPLE'
flickr.upload_photos(
    [os.path.join(APPLE_DIR, file_name) for file_name in os.listdir(APPLE_DIR)]
)
