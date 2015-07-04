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
project_dir = "{0}/ceweb/".format(home_dir)
os.chdir(project_dir)


def check_for_variable_vvv():
    if os.path.isfile("{0}/.vv-config".format(home_dir)):
        return 'true'
    else:
        return 'false'


def get_variable_vvv():
    print "Checking for Variable VVV"
    if not check_for_variable_vvv():
        print "Can't find a it."
        print "Installing Variable VVV"
        os.system("brew install bradp/vv/vv")
    else:
        print "Found it!"
        return


def get_vvv():
    print "Checking for VVV"
    vvv_path = "{0}/vagrant-local/".format(project_dir)
    if not os.path.isfile("{0}/Vagrantfile".format(vvv_path)):
        print "Can't find a it."
        print "Installing vagrant-hostsupdater plugin..."
        os.system("vagrant plugin install vagrant-hostsupdater")
        print "Cloning VVV..."
        os.system("git clone git://github.com/Varying-Vagrant-Vagrants/VVV.git vagrant-local")
        os.chdir(vvv_path)
        os.system("vagrant up")
    else:
        print "Found it!"
        os.chdir(vvv_path)


def check_for_local_website():
    pass


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
get_variable_vvv()
