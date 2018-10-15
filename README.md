## Alpine-lua image

Image alpine-lua is a small alpine image with LUA installed.

This image is primarily used as a small runtime environment for dynamically/"mostly statically" linked go.
This image does not come with luarocks and is not specifically built for LUA development.

This image installs LUA to environmental variable "LUA_DIR".

A simple use case may be:
```Dockerfile
ARG REPO
FROM $REPO/alpine-lua:alpine3.8-lua5.3.4

RUN env CGO_CFLAGS="-I/${LUA_DIR}/lib" go build -o /app
CMD ["/app"]
```

## Build args
Required inputs:
* ALPINE_VERSION:   
  alpine tag to pull for base image
* LUA_VERSION:   
  desired version of lua to install
* LUA_SHA1:  
  SHA1 of the lua tarball  
  Find sha's at "https://www.lua.org/ftp/"
  
Don't pass in other arguments. They may be removed without warning.

## multidimension script
The helper script multidimension.py simplifies creating an include matrix for the inputs to a build tool.
