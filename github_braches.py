import git


remoteurl = "https://github.com/TomasSpusta/pokus_github.git"
localfolder = "D:\PC\Tom\_Odrive\odrive\GD_Work\_WORK\_Bastl\PiPi_RFID ctecka ceitec nano\pokus_github"

myrepo = git.Repo.init (remoteurl, localfolder)
