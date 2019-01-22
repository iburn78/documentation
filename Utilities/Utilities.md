---
title: Utilities commands
author: Andy Kim
geometry: margin=2cm
---

# GIT

* git clone https://github.com/iburn78/documentation
* git init
* git add \<file name\>
* git commit \<file name\>
* git status
* git push
* git pull (once git is cloned, pull checks updates)
* git config credential.helper store \# enables to save id/pwd in local git
* git rm -r \<directory\> to remove all its contents and directory (then commit has to be executed)

# Docker

* docker pull \<image name\> (from Docker Image Repository or Docker hub)
* docker images
* docker ps -a
* docker start \<container id\>
* docker attach \<container id\>
* ctrl+p q: escape from the container
* (once escaped) enter with $docker attach \<container id\> 
* docker run -i -t \<image name\> /bin/bash \# e.g., $ docker run -i -t continuumio/miniconda3 /bin/bash
* To save a image:
    * $ docker ps -a
    * $ docker commit \<container id\> \<new image name\>:\<tag\> \# e.g., $ docker commit \<container id\> mlearn:init
    * $ docker run -i -t mlearn:init /bin/bash /# "/bin/bash" might be skipped
* To mount a folder (e.g., home)
    * $ docker run -i -t -v /c/Users/andy.kim/docker_home:/docker_home_in_image mlearn:init /bin/bash

# Tmux 

* ctrl+b, c: create window
* ctrl+b, w: list windows
* ctrl+b, n p: next / previous window
* ctrl+b, &: kill window
* ctrl+b, , f: name / find window
* ctrl+b, % ": vertical / horizontal split
* ctrl+b, o: switch pane
* ctrl+b, \<space\>: toggle between layouts
