import sys
from pathlib import Path
from os import path, mkdir
import shutil


def get_target_dir_from_args():
    if len(sys.argv) > 1:
        dest_path = sys.argv[2] if len(sys.argv) == 3 else 'c:\\temp\\dest'
        src_path = sys.argv[1]
        if path.isdir(src_path):
            return src_path, dest_path
        else:
            print("Specified path is not exist or is not a directory: " + src_path)
            exit(-2)
    else:
        print("Please specify a target path: python recursion.py <src path> <dest path(default: dest)>")
        exit(-1)


def copy_files(src, dest):
    if src.is_dir():
        dir_content = src.iterdir()
        for item in dir_content:
            copy_files(item, dest)
    else:
        sub_dir_name = src.name.split(".")[-1]
        path_dest_dir = path.join(dest, sub_dir_name)
        try:
            if not path.exists(path_dest_dir):
                mkdir(path_dest_dir)
            shutil.copy2(src.absolute(), path_dest_dir + '\\' + src.name)
        except:
            print("Something went wrong with copying file " + sub_dir_name + " to " + path_dest_dir)


def main():
    src, dest = get_target_dir_from_args()
    print("copying from " + src + " to " + dest)
    copy_files(Path(src), Path(dest))


if __name__ == '__main__':
    main()
