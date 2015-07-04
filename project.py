#!/usr/bin/python
import os
import shutil

'''
    This is a script to initiate a new project for the Covenant Eyes main website.
    Download the script and run "python ceweb.py"

    It will ask you for a "New branch name:" and create a tmp dir.

    Then for each repo it will:
        1. Clone the repo in the tmp dir
        2. Create a the new branch push to origin

    Finally, it will delete the tmp dir.
'''

home_dir = os.environ['HOME']


def get_variable_vvv():
    pass


def get_vvv():
    print "Checking for VVV"
    vvv_path = "{0}/vagrant-local/".format(home_dir)
    if not os.path.exists(vvv_path):
        print "Can't find a vagrant-local dir"
        print "Installing vagrant-hostsupdater plugin..."
        os.system("vagrant plugin install vagrant-hostsupdater")
        print "Cloning VVV..."
        os.system("git clone git://github.com/Varying-Vagrant-Vagrants/VVV.git vagrant-local")
        os.chdir(vvv_path)
        os.system("vagrant up")
    else:
        print "Found it!"
        os.chdir(vvv_path)


# print "New branch name:"
# branch = raw_input()

home_dir = os.environ['HOME']
tmp_dir = "{0}/tmp/".format(home_dir)

# print "Creating new project: %r" % branch


def make_tmp_dir():
    print "Setting up tmp dir..."
    if not os.path.exists(tmp_dir):
        os.makedirs(tmp_dir)
    else:
        print "tmp is already there"


def rm_tmp_dir():
    print "Removing tmp dir..."
    if os.path.exists(tmp_dir):
        shutil.rmtree(tmp_dir)
    print "Done."


def clone_repos(branch):
    print "Cloning repos..."

    repos = {'lemonade2': 'https://github.com/CovenantEyes/lemonade2.git',
             'ice-tea': 'https://github.com/CovenantEyes/ice-tea.git',
             'ce-custom-post-types-plugin': 'https://github.com/CovenantEyes/ce-custom-post-types-plugin.git'}

    for repo, url in repos.items():
        repopath = "{0}/{1}".format(tmp_dir, repo)
        os.chdir(tmp_dir)

        print "cheking for %r" % repo
        if not os.path.exists(repopath):
            print "clone this one: %r from: %r" % (repo, url)
            os.system("git clone {0}".format(url))
        else:
            print "already got it"

        os.chdir(repopath)
        print "pulling down master"
        os.system("git checkout master")
        os.system("git pull -f")
        print "creating the %r branch" % branch
        os.system("git push origin master:refs/heads/{0}".format(branch))

# make_tmp_dir()
# clone_repos(branch)
# rm_tmp_dir()
get_vvv()
