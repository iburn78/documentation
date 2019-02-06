#!/usr/bin/env python3
print("Content-Type: text/html; charset=utf-8")

# The first two lines above has to be included
# $ python3 -m http.server --cgi 8080
# this command should be executed in directory that contains /cgi-bin

# In case docker, run the docker command: 
# docker run -it -v $HOME:$HOME -p 8080:8080 <imagename>:<tag>
# files have to be executable (e.g., using chmod +x <file>)

print("")
print("<h1>Hello World...!</h1>")

