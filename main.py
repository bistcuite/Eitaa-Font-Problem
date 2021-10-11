from sys import argv
import os
from os.path import isdir
import shutil

if __name__ == "__main__" :
    if len(argv) == 1:
        pass
    elif len(argv) == 2 :
        if not isdir("~/.local/share/fonts"):
            os.mkdir("~/.local/share/fonts") # or : os.makedirs("~/.local/share/fonts")
        shutil.move(argv[1],"~/.local/share/fonts")
        font_name = argv[1].split(".")[0]
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
        with open("~/.local/share/EitaaDesktop/edata/fc-custom-1.conf","w") as file:
            file.write(content)