from main import *
import argparse



parser = argparse.ArgumentParser(description='Simple image metadata editor')
group = parser.add_mutually_exclusive_group(required=True)
parser.add_argument('filepath', type=str, help='File path')
group.add_argument(
        "-d", "--delete",
        action="store_true",  
        help="Delete all EXIF metadata"
    )
group.add_argument(
        "-c","--change", 
        action="store_true",  
        help="Change EXIF metadata"
    )
parser.add_argument(
        "-a","--all", 
        action="store_true",  
        help="Display all EXIF metadata"
    )

args = parser.parse_args()


img =jpg_to_exif(args.filepath)
if args.all:
    print("Выполняется команда для флага -a")
    list_all_exif(img)
if args.delete:
    print("Выполняется команда для флага -d")
    clear_all_exif(img)
elif args.change:
    print("Выполняется команда для флага -c")
    change_exif(img)
