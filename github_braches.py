import git


remoteurl = "https://github.com/TomasSpusta/pokus_github.git"
localfolder = "/pokus_github"

myrepo = git.Repo.init (remoteurl, localfolder)
