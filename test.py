import ffmpeg
import os
from os import path
import shutil


def main():

    vidName = input("Enter the video's name here: ")
    filepath = input("Enter the filepath if not in current directory: ")
    
    def runstream(name):
        stream = ffmpeg.input(name)
        stream = ffmpeg.hflip(stream)
        stream = ffmpeg.output(stream, 'output.mp4')
        ffmpeg.run(stream)

    def checkvid(vidName, filepath):
        if path.exists(vidName) == True:
            print("File exists in current directory")
            runstream(vidName)
        else: 
            if os.path.exists(filepath):
                fullvidlink = os.path.realpath(filepath + "\\" + vidName)
                if os.path.exists(fullvidlink):
                    print("File exists")
                    runstream(fullvidlink)
                else:
                    print("File doesn't exist in this directory.")
            else:
                print("Sorry, not a valid directory.")
       
    checkvid(vidName, filepath)

   

if __name__ == "__main__":
    main()