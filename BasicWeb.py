import os
import argparse
import pyautogui as gui
import time

class Operacje():
    def __init__(self,name, path):
        self.name = name
        self.path = path
    def goToPath(self):
        os.chdir(self.path)
    def createFolder(self):
        os.system("mkdir {}".format(self.name))
        os.chdir(self.name)
    def makro(self):
        gui.hotkey('ctrl', 'z')
        gui.press('enter')
    def createFiles(self):
        list = ["index.html","script.js","style.css"]
        for x in list:
            os.system("copy con {}".format(x))
            os.system("pause")
            time.sleep(1)
            self.makro()

    def check(self):
        os.system("tree")




parser = argparse.ArgumentParser(description="Creating basic web files (script.js, index.html, style.css)", prog="BIOS ACTIV")

parser.add_argument ("-n","--name",help="Name of the folder in which will be syntax",required=True,type=str)

parser.add_argument ("-p","--path",help="Path to location where will be created folder",required=True,type=str)

args = parser.parse_args()

obiekt = Operacje(args.name,args.path)

obiekt.goToPath()
obiekt.createFolder()
obiekt.createFiles()
# obiekt.check()
