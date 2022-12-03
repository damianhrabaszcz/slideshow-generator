# slideshow-generator
Tested on Ubuntu 20.04.05 LTS

Place the `gen.py` file inside your images directory, and then execute it with python with this paremeter list:
1) name of the slideshow (eg. "My slide show")
2) show time of each image (in seconds, eg. 60.0)
3) transition duration (in seconds, eg. 0.5)

Example:
```bash
python3 gen.py "My slide show" 60.0 0.5
```

This script run will create 2 files:
1) `slideshow.xml` Inside your images directory  
with links to all the images inside your images directory 
2) `config.xml` inside `~/.local/share/gnome-background-properties/`  
with link to slideshow.xml

Each run will overwrite the files.

Now you should be able to see the slideshow in Background Settings.
