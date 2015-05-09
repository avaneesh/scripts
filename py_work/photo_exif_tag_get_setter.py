#! /usr/bin/python2.7

from gi.repository import GExiv2


# https://wiki.gnome.org/Projects/gexiv2
# install GExiv2 manually from above link
# Also install:
# sudo apt-get install python-gobject
# sudo apt-get install gir1.2-gexiv2-0.10 (only if required)
# sudo apt-get install python-gi (only if required)

# Sample:
# https://wiki.gnome.org/Projects/gexiv2/PythonSupport

exif = GExiv2.Metadata('img.jpg')

p_comment = exif.get_comment()
print 'Comment is: ' + p_comment

# Add a new comment 
#exif.set_comment('new comment')

# Save the file if you make changes
#exif.save_file()
