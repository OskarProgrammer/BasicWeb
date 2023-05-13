from os import system,chdir
import argparse
import sys


parser = argparse.ArgumentParser(description="Creating basic web files")

parser.add_argument("-n","--name",help="Name of the project",required=True,type=str)

parser.add_argument("-p","--path",help="Path to the place of the project",required=True,type=str)

args = parser.parse_args()

class CreateBasic(object):

    def __init__(self,name,path):
        self._name = name
        self._path = path
        self.all()

    def goToPath(self):
        chdir(self._path)

    def createFolder(self):
        system("mkdir {}".format(self._name))
        chdir(self._name)

    def createFiles(self):
        list = "index.html script.js style.css".split(" ")
        try:
            for x in list:
                with open(x,"a")as file:
                    if x == list[0]:
                        file.write("\"\"\" That's your html file where you can write html marks\"\"\"")
                    elif x==list[1]:
                        file.write(f"//That's your javascript file")
                    else:
                        file.write(f"// Here you can add style to components")
                    
        except Exception as e:
            print(f"Error: {e}")
            system("pause")

    def all(self):
        self.goToPath()
        self.createFolder()
        self.createFiles()
        
obiekt = CreateBasic(args.name,args.path)
