# gsdjango

## This is an experimental project to explore Django
> on VPS Ubuntu 16.04 using Python3, Pip3 & Django 2.0

## Steps to get going

**1. Log in to your ubuntu os.**

**2. Install Python3 if not installed**
   * $ sudo apt-get update
   * $ sudo apt-get -y upgrade
   * $ sudo apt-get install python3
  
  *Check the installation*
  
  * $ python3 -V
      > Output  -  Python 3.5.2
     
**3. Install pip3 if not installed** 
  * $ sudo apt-get install -y python3-pip
  
  *Check the installation*
  
  * $ pip3 -V
    > Output  -  pip 8.1.1 from /usr/lib/python3/dist-packages (python 3.5)

**4. Install Django 2.0 if not installed**
   * $ sudo pip3 install Django==2.0
   
   *Check the installation*
   
   * $ django-admin --version
     > OUtput  - 2.0

**5. Install git if not installed**
   * $ sudo apt-get install git
   
   *Check the installation*
   
   * $ git --version
     > Output  - git version 2.7.4

**6. Initialize and Configure git**
   * $ git init
   * $ git config --global user.name "Your Name"
   * $ git config --global user.email "youremail@domain.com"
   
   *Check the configuration*
   
   * $ git config --list
     > Output  - user.name=Your Name
               > user.email=youremail@domain.com

**7. Clone the remote repository**
   * $ git clone https://github.com/ghanshyamdhiman/gsdjango.gitb
   
   *Install tree if not installed*
   * $ sudo apt install tree
  
  *Check the installation*
  
   * $ tree --version
     > Output - tree v1.7.0 (c) 1996 - 2014
   
   *Check the clone*
    $ tree

**8. Move to the installation directory gsdjango**
   - $ cd gsdjango
   
**9. Run the server**
   * $ python3 manage.py runserver 0:80
   > Output  - ....Control-C

**10. Open the browser and see the application running by going to the ip address of the ubuntu server or localhost**


@ghanshyamdhiman :+1: Go it....Get it! :shipit:
   
  ###### Further Reading
[Writing your first Django app](https://docs.djangoproject.com/en/2.0/intro/tutorial01/).
     


