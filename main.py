from sys import argv
import os
import shutil

if len(argv) == 1:
    pass
elif len(argv) == 2 :
    if not os.isdir("~/.local/share/fonts"):
        os.mkdir("~/.local/share/fonts") # or : os.makedir("~/.local/share/fonts")
   shutil.move(argv[1],"~/.local/share/fonts")
   font_name = argv[1].split(".")[0]
   file = open("~/.local/share/EitaaDesktop/edata/fc-custom-1.conf","w")
   content = f"""<?xml version='1.0'?>
    <!DOCTYPE fontconfig SYSTEM 'fonts.dtd'>
    <fontconfig>

    <match>
    <edit mode="prepend" name="family">
    <string>{font_name}</string>
    </edit>
    </match>

    <dir>~/.local/share/fonts</dir>
    <dir>/usr/share/fonts/</dir>

    </fontconfig>
   """
   file.write(content)
   file.close()
