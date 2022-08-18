import git


remoteurl = "https://github.com/TomasSpusta/pokus_github.git"
localfolder = "/pokus_github"

try:
    myrepo = git.Repo.clone_from (remoteurl, localfolder)
except Exception as e:
    print (e)
    myrepo = git. Repo (localfolder)
    myrepo.remotes.origin.pull("master")
    