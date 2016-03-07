# ceweb

This is a script to initiate a new project for the Covenant Eyes main website.

## Dependancies

- Virtual Box: [https://www.virtualbox.org/](https://www.virtualbox.org/)
- Vagrant: [https://www.vagrantup.com/](https://www.vagrantup.com/)

## Usage

Download the script and run "python ceweb.py"

It will first look for a local copy of the WordPress website in a vagrant-local directory.

### Local Website Set-up

If no local copy of the website is found when running "python ceweb.py", the website set-up is initiated.

Steps include:
1. Check for and download Varying Vagrant Vagrants
2. Check for and download Variable VVV
3. Run Variable VVV command to create a new WordPress site at covenanteyes.dev
4. Clone the necessary repos into the new covenanteyes.dev site

### New Project

If a local copy of the website is found when running "python ceweb.py", a new project is initiated.

- It will ask you for a "New branch name:" and create a tmp dir.

- Then for each repo it will:
    1. Clone the repo in the tmp dir
    2. Create a the new branch push to origin

- Finally, it will delete the tmp dir.