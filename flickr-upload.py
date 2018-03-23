"""Tool for uploading files to flickr"""
import flickr
import argparse
import sys
import os
# PHOTOS_DIR = '/home/media/photos/FIS Phone/DCIM/100APPLE'
# PHOTOS_DIR = '/home/media/photos/Wedding/Benny/HiRes'


def main():
    """Get the file names from the command line and upload them"""
    parser = get_parser()
    args = parser.parse_args()
    if args.version:
        for module_name in (
            'certifi', 'chardet', 'idna', 'oauthlib', 'requests',
            'requests_oauthlib', 'urllib3'
        ):
            print(
                '{} {}'.format(
                    module_name, __import__(module_name).__version__
                )
            )
        print('{} {}'.format(parser.prog, flickr.__version__))
        return 0
    photo_file_names = args.photo_file_names
    if not photo_file_names:
        print('{}: list of files is missing!'.format(parser.prog))
        return 26
    for file_name in photo_file_names:
        if not os.path.isfile(file_name):
            print('{}: No such file!'.format(file_name))
            return 29
        lower = file_name.lower()
        if not lower.endswith('jpg') or lower.endswith('jpeg'):
            print(
                '{}: Only files that end with jpg or jpeg are '
                'supported!'.format(file_name)
            )
    flickr.upload_photos(photo_file_names)


def get_parser():
    """Parse the command line arguments"""
    parser = argparse.ArgumentParser(description='Upload to Flickr.')
    parser.add_argument(
        'photo_file_names', nargs='*', help='list of files to upload'
    )
    parser.add_argument('--version', action='store_true')
    return parser


sys.exit(main())