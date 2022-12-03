import os
import sys

# Get a list of all files in the directory
current_path = os.getcwd()
list_of_files = []

for root, dirs, files in os.walk(current_path):
    for file in files:
        if not file in ['slideshow.xml', 'gen.py']:
            list_of_files.append(os.path.join(root,file))

# If slideshow.xml already exists it will be replaced with new content
with open('slideshow.xml', 'w') as file:
    file.write('<?xml version="1.0" ?>\n')
    file.write('<background>\n')
    for x in range(0, len(list_of_files)):
        file.write('  <static>\n')
        file.write('    <duration>'+sys.argv[2]+'</duration>\n')
        file.write('    <file>'+list_of_files[x] + '</file>\n')
        file.write('  </static>\n')

        file.write('  <transition>\n')
        file.write('    <duration>'+sys.argv[3]+'</duration>\n')
        file.write('    <from>'+list_of_files[x]+'</from>\n')
        if x != len(list_of_files)-1:
            file.write('    <to>'+list_of_files[x+1]+'</to>\n')
        else:
            file.write('    <to>'+list_of_files[0]+'</to>\n')
        file.write('  </transition>\n')
    file.write('</background>\n')

# Creating config.xml file in directory ~/.local/share/gnome-background-properties
config_xml_path = os.path.expanduser('~') + r'/.local/share/gnome-background-properties/config.xml'
with open(config_xml_path, 'w') as file:
    file.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    file.write('<!DOCTYPE wallpapers SYSTEM "gnome-wp-list.dtd">\n')
    file.write('<wallpapers>\n')
    file.write('  <wallpaper>\n')
    file.write('    <name>'+sys.argv[1]+'</name>\n')
    file.write('    <filename>'+current_path+'/slideshow.xml</filename>\n')
    file.write('    <options>zoom</options>\n')
    file.write('    <pcolor>#2c001e</pcolor>\n')
    file.write('    <scolor>#2c001e</scolor>\n')
    file.write('    <shade_type>solid</shade_type>\n')
    file.write('  </wallpaper>\n')
    file.write('</wallpapers>\n')

