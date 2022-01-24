#
# [mst] parsing_html_xml.py 
# doodling built in html and xml parsers
# based on the lynda.com 'Learning Python' course (chapter 5)
#
# log:
# - 2021.01 initial
# - html parsing
# - xml parsing
#

import re   # some regex matching
from html.parser import HTMLParser  # we derive from the built in parser
import xml.dom.minidom  # built-in xml parser

# we will count xml meta tags globally 
metacount = 0;

# we inherit and override handling methods from the built in parser
class MyHTMLParser(HTMLParser):
    
    # handler functions are triggered at certain parts of the html file
    # this handler will be called when the closing ">" of the tag is reached
    # lets report the different elements met in throughout the parsing
    def handle_starttag(self, tag, attrs):
        global metacount
        
        pos = self.getpos() # returns a tuple indication line and character        
        print ("Encountered a start tag: ", tag, " At line: ", pos[0], " position ", pos[1])
        if tag == "meta":
            metacount += 1
            
        if attrs.__len__() > 0:
            attributes = "\tAttributes: "
            for a in attrs:
                attributes += "\t" + str(a[0]) + "=" + str(a[1])
            print (attributes)
            
            
    # [mst] just combined functionality for elements printing
    def handle_common(self, element_name, data):
        pos = self.getpos()
        print ("Encountered ", element_name, ": ", data, " At line: ", pos[0], " position ", pos[1])
        
     
    # function to handle the ending tag
    def handle_endtag(self, tag):
        self.handle_common("an end tag", tag)  
        
        
    # function to handle character and text data (tag contents)
    def handle_data(self, data):
        # [demo] we want to disregard white spaces and new lines as data
        # lets use regular expressions for an elegant fit
        pattern = re.compile("[\n ]+")
        
        if not  pattern.search(data):
        #if not data == '\r' and not data == '\n' and not data == "\n  ":
            self.handle_common("some data", data)
            

    # function to handle the processing of HTML comments
    def handle_comment(self, data):
        self.handle_common("a comment", data)
        

def listTag(doc, tagName):
    elements = doc.getElementsByTagName(tagName)
    print ("%d tags of " % elements.length, tagName)
    for element in elements:
        print (element.getAttribute("name"))


def main():       
    #######
    # parsing html - 
    print ("HTML parsing ...")
    parser = MyHTMLParser()
    
    # read-open the sample file and feed it to the parser
    f = open("samplehtml.html")
    if f.mode == "r":
        contents = f.read() # read the entire file
        parser.feed(contents)
    
    print ("%d meta tags encountered" % metacount)
    

  
    #######
    # parsing xml
    # use the parse() function to load and parse an XML file
    doc = xml.dom.minidom.parse("samplexml.xml");
    
    # print out the document node and the name of the first child tag
    print ("\n\nXML parsing...")
    print ("nodeName: ", doc.nodeName)
    print ("firstChild: ", doc.firstChild.tagName)
    
    
    # the parser allow us rto operate on tags as objects
    # we can list tags...
    listTag(doc, "skill")    
        
    # ... and add tags: create a new XML tag and add it into the document
    print("\nadding skill jQuiery...\n")
    newSkill = doc.createElement("skill")
    newSkill.setAttribute("name", "jQuery")
    doc.firstChild.appendChild(newSkill)
    
    listTag(doc, "skill")
    

if __name__ == "__main__":
    main()