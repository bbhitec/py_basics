#
# [mst] file_io_path_utils.py
# file properties and details operations
# based on the lynda.com 'Learning Python' course (chapter 4)
#
# log:
# -file existence and creation times, modification timedeltas
# -path sting manipulations
# -shell utils: file manipulations
#

import os
from os import path
import datetime
#from datetime import date, time, timedelta
import time
#from calendar import mdays
import shutil       # copy, copystat, rename...
from zipfile import ZipFile

def main():

    # print the name of the OS
    print ("os.name: " + os.name)
    init_fname = "textfile.txt"

    # [demo] Filename manipulations
    # file existence and path manipulations
    if path.exists(init_fname):
        src = path.realpath(init_fname)
        (dirname, filename) = path.split(src)  # will split by the '/' token, into a list
        print (path.split(dirname))

    # Check for item type
    # str() will convert a boolean to readable string
    print (" is a file: " + str(path.isfile(filename)))
    print ("Item is a directory: " + str(path.isdir("textfile.txt")))


    # Get the modification time, different formats
    t = time.ctime(path.getmtime(filename))
    print (t)
    print (datetime.datetime.fromtimestamp(path.getmtime(filename)))

    # Calculate how long ago the item was modified
    td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))
    print ("It has been " + str(td) + "The file was modified") # (will result in a 'timedelta' object)
    print ("Or, " + str(td.total_seconds()) + " seconds")

    # [demo] Shell utilities

    # make a duplicate(backup) of an existing file
    if path.exists(init_fname):
        # let's make a backup copy by appending "bak" to the name (full path)
        dst = src + ".bak"

        # now use the shell to make a copy of the file
        shutil.copy(src,dst)
        print (datetime.datetime.fromtimestamp(path.getmtime(dst)))

        # we can copy a file's permissions and modification dates
        shutil.copystat(src, dst)
        print (datetime.datetime.fromtimestamp(path.getmtime(dst)))

        # renaming files using the os module (will not overwrite, can use shutil.move for that)
        dst_rename = dst + "2"
        if not path.exists(dst_rename):
            os.rename(dst, dst_rename)


        # [demo] Archiving and zipping
        # simple-archiving a dir
        shutil.make_archive("arch", "zip", dirname)

        # advanced archiving
        # 'with' will open a local scope for the given instruction/object
        with ZipFile("betterzip.zip","w") as newzip:
            #here we can fine-pick files to add to the archive
            newzip.write(dst_rename)    # using an absolute path will create sub-dirs in the zip file
            newzip.write(filename)


if __name__ == "__main__":
    main()
