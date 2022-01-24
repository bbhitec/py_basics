#
# [mst] file_io_basics.py 
# basic file operations
# based on the lynda.com 'Learning Python' course
#
# log:
# -opening and writing a file
# -reading a file line-wise or entirely
#

def main():
    
    fname = "textfile.txt"
    # Open a file for writing (the '+' will create it if it doesn't exist)
    # the files functionality is built into python (no special import)
    #f = open(fname,"w+")
    # [bp] using 'with' will close the file even if there is an exception
    #       before closing explicitly    
    with open(fname, 'w+') as f:
       
#     # Open the file for appending text to the end
#     f = open("textfile.txt","a+")
     
        # write some lines of data to the file
        for i in range(10):
            f.write("This is line %d\r\n" % (i+1))
       
    # close the file when done [bp] no need f using 'with'
    #f.close()
  
    # Open the file back up and read the contents
    f = open("textfile.txt","r")
    if f.mode == 'r': # check to make sure that the file was opened
        # use the read() function to read the entire file at once
        contents = f.read()
        print (contents)
    
    # sometime we need to read line by line (e.g. file is too big)
    fl = f.readlines() # readlines reads the individual lines into a list
    for x in fl:
        print (x)
    
if __name__ == "__main__":
    main()
