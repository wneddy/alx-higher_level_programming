#!/usr/bin/python3
"""
module to add agrs passed in the command line
and saves the list to a file
"""
import sys


save_to_json_file = __import__('5-save_to_json_file.py').save_to_json_file
load_from_json_file = \
    __import__('6-load_from_json_file.py').load_from_json_file


def main():
    """main function"""
    try:
        args = load_from_json_file("add_item.json")
    except FileNotFoundError:
        args = []
    args.extend(sys.argv[1:])
    save_to_json_file(args, "add_item.json")
    print(f"Added {sys.argv[1:]} to add_item.json")


if __name__ == "__main__":
    main()
