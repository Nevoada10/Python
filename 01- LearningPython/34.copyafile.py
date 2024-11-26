import shutil

# copyfile() = copies the content of a file.
# copy() = copyfile + permissions mode + destination can be a directory.
# copy2() = copy() + copies metadata (file's creation and modification times).

# shutil.copyfile(name, name2) if they are in the Pycharm's Project Folder,
# or if the copy destination is the same, you don't need to add the path.

shutil.copyfile("/Users/urielnevessilva/Desktop/Programing/Python/a.txt"  # - source
                , "/Users/urielnevessilva/Desktop/Programing/Python/34copyfiletest/a34copyafile.txt")  # - destination.
# args = (source, destination).
