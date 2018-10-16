## LUA image

Image 'lua' is a small image with LUA installed.

This image is primarily used as a small runtime environment for dynamically/"mostly statically" linked go.
This image does not come with luarocks and is not specifically built for LUA development.

This image installs LUA to environmental variable "LUA_DIR".

A simple use case may be:
```Dockerfile
ARG REPO
FROM $REPO/lua:alpine3.8-lua5.3.4

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

## multidimension.py script
The helper script multidimension.py simplifies creating an include matrix for the inputs to a build tool.

## Rebuild instructions

#### LUA version update
Open `multidimension.py` and add the new lua versions and sha1's to the lua_include list.
Then follow the steps in [Alpine version update](README.md#Alpine version update).

#### Alpine version update
Recreate the matrix of environmental variables with `python3 multidimension.py`.

Then use that matrix to create one or all of the images with those inputs.
