#!/usr/bin/env python3

import os
import subprocess
import shutil

# --------------------------------------------------------
reorg_dir = "/Untitled Folder"
exclude = () 
remove_emptyfolders = True
# ---------------------------------------------------------

for root, dirs, files in os.walk(reorg_dir):
    for name in files:
        subject = root+"/"+name
        if name.startswith("."):
            extension = ".hidden_files"
        elif not "." in name:
            extension = ".without_extension"
        else:
            extension = name[name.rfind("."):]
        if not extension in exclude:
            if extension==".jpeg" or extension==".jpg" or extension==".JPG" or extension==".png" or extension==".PNG":
                new_dir = reorg_dir+"/Pictures"
            elif extension==".docx" or extension==".doc" or extension==".pdf" or extension==".xlsx" or extension==".ppt" or extension==".pptx":
                new_dir = reorg_dir+"/Documents"
            elif extension==".mp3" or extension==".MP3":
                new_dir = reorg_dir+"/Songs"
            elif extension==".mp4" or extension==".MP4" or extension==".avi" or extension==".AVI":
                new_dir = reorg_dir+"/Videos"
            elif extension==".db" or extension==".DB":
                new_dir = reorg_dir+"/Databases"
            elif extension=="*.*":
                new_dir = reorg_dir+"/Others"

        if not os.path.exists(new_dir):
                os.mkdir(new_dir)
            n = 1; name_orig = name
            while os.path.exists(new_dir+"/"+name):
                name = name_orig
                n = n+1
            newfile = new_dir+"/"+name
            shutil.move(subject, newfile)

def cleanup():
    filelist = []
    for root, dirs, files in os.walk(reorg_dir):
        for name in files:
            filelist.append(root+"/"+name)
    directories = [item[0] for item in os.walk(reorg_dir)]
    for dr in directories:
        matches = [item for item in filelist if dr in item]
        if len(matches) == 0:
            try:
                shutil.rmtree(dr)
            except FileNotFoundError:
                pass

if remove_emptyfolders == True:
    cleanup()