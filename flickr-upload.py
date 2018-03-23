"""Tool for uploading files to flickr"""
import flickr
import argparse
import sys
import os
# /home/media/photos/FIS Phone/DCIM/100APPLE
# /home/media/photos/Wedding/Benny/HiRes
# /home/media/photos/2012-04
# /home/media/photos/2016
# /home/media/photos/Camera
# /home/media/photos/FisherPriceRafael

SUPPORTED_EXTENSIONS = ('.jpg', '.jpeg', '.mp4', '.3gp', '.gif')


def main():
    """Get the file names from the command line and upload them"""
    parser = get_parser()
    args = parser.parse_args()
    if args.version:
        print_version(parser)
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
        for supported_extension in SUPPORTED_EXTENSIONS:
            if lower.endswith(supported_extension):
                break
        else:
            print(
                '{}: Only these extensions are supported: {}'.format(
                    file_name, ' '.join(SUPPORTED_EXTENSIONS)
                )
            )
            return 41
    flickr.upload_photos(photo_file_names, args.photoset_id)


def print_version(parser):
    """Get all the versions and print them out"""
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


def get_parser():
    """Parse the command line arguments"""
    parser = argparse.ArgumentParser(description='Upload to Flickr.')
    parser.add_argument(
        'photo_file_names', nargs='*', help='list of files to upload'
    )
    parser.add_argument('--version', action='store_true')
    parser.add_argument('--photoset-id')
    return parser


sys.exit(main())
