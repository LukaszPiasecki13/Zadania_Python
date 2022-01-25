import xml.sax

import xml.dom.minidom
from xml.etree.ElementTree import parse

# define a Custom ContentHandler class that extends ContenHandler
class CustomContentHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.postCount = 0
        self.entryCount = 0
        self.isInTitle = False

    # Handle startElement
    def startElement(self, tagName, attrs):
        if tagName == 'blogposts':
            print('Blogposts title: ' + attrs['title'])
        elif tagName == 'post':
            self.postCount += 1
        elif tagName == 'entry':
            self.entryCount += 1
        elif tagName == 'title':
            self.isInTitle = True






def Sax_example():
    # create a new content handler for the SAX parser
    handler = CustomContentHandler()

    # call the parse method on an XML file
    xml.sax.parse('xmldata.xml', handler)

    # when we're done, print out some interesting results
    print(f'There were {handler.postCount} post elements')
    print(f'There were {handler.entryCount} entry elements')





def Dom_example():
    file = r"xmldata.xml"
    doc = parse(file)
    domtree = xml.dom.minidom.parse('xmldata.xml')
    rootnode = domtree.documentElement

    # display some information about the content
    print(f'The root element is {rootnode.nodeName}')
    print(f'The Title is: {rootnode.getAttribute("title")}')
    entries = domtree.getElementsByTagName('entry')
    print(f'There are {entries.length} entry tags')

    newItem = domtree.createElement('entry')

    newItem.appendChild(domtree.createTextNode('NOWY WPROWADZONY TEKST'))

    firstPost = domtree.getElementsByTagName('post')[0]
    firstPost.appendChild(newItem)

    # Now count the entry tags again
    entries = domtree.getElementsByTagName('entry')
    print('Now there are {0} entry tags'.format(entries.length))

    # Print out the domtree as xml
    print(domtree.toxml())
    doc.write('xmldata1.xml', encoding="UTF-8", xml_declaration=True)


if __name__ == '__main__':
    print("Sax example below:")
    print("")
    Sax_example()
    print("")
    print("Dom example below:")
    print("")
    Dom_example()