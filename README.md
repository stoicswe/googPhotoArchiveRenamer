# Goog Photo Archive Renamer
Downloading Google Photo archives is annoying, since all the image file names do not have the date and time for when they were created. This python script will help with changing that.

# How to use
First, download your Google Photos archives. They can be found here: https://myaccount.google.com/dashboard. just scroll down to the `Photos` section and click download. This may take some time depending on how many photos you have uploaded. Once downloaded, unzip the folders out of the files you downloaded into a new folder. Second, in order to use this script, you will need to download and install [python3+](https://www.python.org/downloads/). Once installed, you can run the script using the following command, replacing the `<YOUR_FOLDER_NAME>` with the folder where you put all the photos from Google Photos:
```
python3 ./readGooglePhotoArchives.py -f <YOUR_FOLDER_NAME>
```
The script will then do the rest. This script will parse over subfolders as well (not fully tested btw)! All images in the sub-folders will be renamed to be: `YYY-MM-DD HH:MM:SSZ` with the correct image extension.

# Acknowledgement
_Original Author_: [Nathaniel Bunch](https://github.com/nathanielbunch)
