import os
import json
import argparse
from datetime import datetime, timezone

# Name: Google Photo Archives
# Description: A smol project for converting
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--folder", help = "Folder where the Google Photo archive is.")
#parser.add_argument("", "--verbose", help = "Verbose mode.")
args = parser.parse_args()
###########################
# Helper funcitons
def navFolder(folder):
    list_of_folders = filter( lambda x: os.path.isdir(os.path.join(folder, x)), os.listdir(folder) )
    for fldr in list_of_folders:
        navFolder(folder + "/" + fldr)
    list_of_files = filter( lambda x: os.path.isfile(os.path.join(folder, x)), os.listdir(folder) )
    files = {}
    for f in list_of_files:
        fn = f.split('.')[0]
        if fn in files:
            files[fn] += [f]
        else:
            files[fn] = [f]
    print("Currently in {}".format(folder))
    print("Found {} files.".format(len(files)))
    for f in files:
        if len(files[f]) == 2:
            if files[f][0].endswith(".json"):
                try:
                    jf = open(folder + "/" + files[f][0], 'r', encoding="utf-8")
                    ext = os.path.splitext(files[f][1])[1]
                    data = json.load(jf)
                    print("File: {}".format(files[f][1]))
                    print("Ext: {}".format(ext))
                    ct = datetime.fromtimestamp(int(data["photoTakenTime"]["timestamp"]), timezone.utc)
                    print("Creation time: {}".format(ct))
                    nfn = ct.strftime('%Y-%m-%d %H.%M.%S') + "Z"
                    print("New filename: {}".format(nfn))
                    print()
                    os.rename(r'{}'.format(folder+"/"+files[f][1]), r'{}'.format(folder+"/"+nfn+ext))
                except UnicodeDecodeError:
                    print("File: {} not changed. UnicodeDecodeError.".format(files[f][1]))
            else:
                try:
                    jf = open(folder + "/" + files[f][1], 'r', encoding="utf-8")
                    ext = os.path.splitext(files[f][0])[1]
                    data = json.load(jf)
                    print("File: {}".format(files[f][0]))
                    print("Ext: {}".format(ext))
                    ct = datetime.fromtimestamp(int(data["photoTakenTime"]["timestamp"]), timezone.utc)
                    print("Creation time: {}".format(ct))
                    nfn = ct.strftime('%Y-%m-%d %H.%M.%S') + "Z"
                    print("New filename: {}".format(nfn))
                    print()
                    os.rename(r'{}'.format(folder+"/"+files[f][0]), r'{}'.format(folder+"/"+nfn+ext))
                except UnicodeDecodeError:
                    print("File: {} not changed. UnicodeDecodeError.".format(files[f][0]))

# Do not do anything if the folder arg is missing
if args.folder:
    workDir = args.folder
    # call and navigate recursively
    navFolder(workDir)
