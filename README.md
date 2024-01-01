# NGL.link checker

# Files

- [IGfollowconvert.py](https://github.com/Ucodedev/NGL-checker/blob/main/IGfollowconvert.py "IGfollowconvert.py") This file is used to convert a .csv file from the [IGfollow](https://chromewebstore.google.com/detail/ig-export-follower-tool/pkafmmmfdgphkffldekomeaofhgickcg) extension to a .csv list that the main program can use. (Please name the input file : _igfile.csv_ and place them in the same folder as the other NGL checker files.)

-  [main-NGL-checker.py](https://github.com/Ucodedev/NGL-checker/blob/main/main-NGL-checker.py "main-NGL-checker.py") This is the main file that is used to check if usernames on the provided list have an NGL.link account. This program creates a _yes.csv_ file with all the usernames that have an NGL account. (The input file with usernames must be called _usernames.csv_ and must be located in the same folder as the other NGL checker files.)
## Requirements

This program needs these libraries :
- requests
- beautifulsoup4

You can install them with these commands :

    pip install requests
    pip install beautifulsoup4


## Manually create the usernames.csv list

You can manually create the _usernames.csv_ list using this data format:
![usernames.csv format](https://i.ibb.co/DVYt14W/image-2024-01-01-145106683.png)
