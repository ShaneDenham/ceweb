#!/usr/bin/python
import os

home_dir = os.environ['HOME']
project_dir = "{0}/ceweb".format(home_dir)
vvv_path = "{0}/vagrant-local".format(home_dir)
os.chdir(home_dir)


def get_vvv():
    print "Checking for VVV..."
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


def get_variable_vvv():
    print "Checking for Variable VVV..."
    if not os.path.isfile("{0}/.vv-config".format(home_dir)):
        print "Can't find a it."
        print "Installing Variable VVV"
        os.system("brew install bradp/vv/vv")
    else:
        print "Found it!"


def check_for_local_website():
    if os.path.isdir("{0}/www/covenanteyes/htdocs/lemonade".format(vvv_path)):
        return True
    else:
        return False


def clone_lemonade():
    print "Checking for lemonade2 repo..."
    if not os.path.isdir("{0}/www/covenanteyes/htdocs/lemonade/".format(vvv_path)):
        print "Can't find a it."
        print "Cloning lemonade2 repo..."
        os.system("git clone https://github.com/CovenantEyes/lemonade2.git {0}/www/covenanteyes/htdocs".format(vvv_path))
    else:
        print "Found it!"


def clone_royrogers():
    print "Checking for RoyRogers repo..."
    royrogers_dir = "{0}/www/covenanteyes/htdocs/lemonade/wp-content/themes/roy-rogers".format(vvv_path)
    if not os.path.isdir("{0}".format(royrogers_dir)):
        print "Can't find a it."
        print "Cloning RoyRogers repo..."
        os.system("git clone https://github.com/CovenantEyes/RoyRogers.git {0}".format(royrogers_dir))
        print "Renaming scripts.php.example to scripts.php"
        os.rename("{0}/inc/scripts.php.example".format(royrogers_dir), "{0}/inc/scripts.php".format(royrogers_dir))
    else:
        print "Found it!"


def clone_icetea():
    print "Checking for ice-tea repo..."
    if not os.path.isdir("{0}/www/covenanteyes/htdocs/lemonade/wp-content/plugins/ice-tea".format(vvv_path)):
        print "Can't find a it."
        print "Cloning ice-tea repo..."
        os.system("git clone https://github.com/CovenantEyes/ice-tea.git {0}/www/covenanteyes/htdocs/lemonade/wp-content/plugins/ice-tea".format(vvv_path))
    else:
        print "Found it!"


def clone_posttype():
    print "Checking for ce-custom-post-types-plugin repo..."
    if not os.path.isdir("{0}/www/covenanteyes/htdocs/lemonade/wp-content/plugins/ce-custom-post-types-plugin".format(vvv_path)):
        print "Can't find a it."
        print "Cloning ce-custom-post-types-plugin repo..."
        os.system("git clone https://github.com/CovenantEyes/ce-custom-post-types-plugin.git {0}/www/covenanteyes/htdocs/lemonade/wp-content/plugins/ce-custom-post-types-plugin".format(vvv_path))
    else:
        print "Found it!"


def clone_supportpress():
    print "Checking for SupportPress repo..."
    if not os.path.isdir("{0}/www/covenanteyes/htdocs/lemonade/wp-content/plugins/SupportPress".format(vvv_path)):
        print "Can't find a it."
        print "Cloning SupportPress repo..."
        os.system("git clone https://github.com/CovenantEyes/SupportPress.git {0}/www/covenanteyes/htdocs/lemonade/wp-content/plugins/SupportPress".format(vvv_path))
    else:
        print "Found it!"


def clone_repos():
    print "Cloning repos.."
    clone_lemonade()
    clone_royrogers()
    clone_icetea()
    clone_posttype()
    clone_supportpress()


def setup_local_website():
    if not os.path.isdir("{0}/www/covenanteyes".format(vvv_path)):
        print "Creating local website at covenanteyes.dev..."
        db_file = "{0}/db_staging_ramp.sql".format(project_dir)
        if os.path.isfile(db_file):
            os.rename("{0}".format(db_file), "{0}/wp_2014_covenanteyes.sql".format(vvv_path), )
            os.system("vv create -d covenanteyes.dev -n covenanteyes --blank-with-db -db {0}/db_staging_ramp.sql".format(vvv_path))
        else:
            os.system("vv create -d covenanteyes.dev -n covenanteyes --blank")
    clone_repos()
    os.chdir(vvv_path)
    os.system("vagrant reload --provision")


def create_repo_branches(branch):
    print "Creating repo branches..."

    repo_paths = {'lemonade2': '{0}/www/covenanteyes/htdocs'.format(vvv_path),
                  'roy-rogers': '{0}/www/covenanteyes/htdocs/lemonade/wp-content/themes/roy-rogers'.format(vvv_path),
                  'ice-tea': '{0}/www/covenanteyes/htdocs/lemonade/wp-content/plugins/ice-tea'.format(vvv_path),
                  'ce-custom-post-types-plugin': '{0}/www/covenanteyes/htdocs/lemonade/wp-content/plugins/ce-custom-post-types-plugin'.format(vvv_path),
                  'SupportPress': '{0}/www/covenanteyes/htdocs/lemonade/wp-content/plugins/SupportPress'.format(vvv_path)}

    for repo, repo_path in repo_paths.items():

        print "cheking for %r" % repo
        if os.path.isdir(repo_path):
            os.chdir(repo_path)
            print "pulling down master"
            os.system("git checkout master")
            os.system("git pull -f")
            print "creating the %r branch" % branch
            os.system("git push origin master:refs/heads/{0}".format(branch))


def build_local_website():
    get_vvv()
    get_variable_vvv()
    setup_local_website()


def ce_website_project():
    print "Checking for a local copy of the website..."
    if not check_for_local_website():
        print "Can't find a it."
        build_local_website()
    else:
        print "Found it!"
        print "New branch name:"
        branch = raw_input()
        print "Creating new project: %r" % branch
        create_repo_branches(branch)


ce_website_project()
