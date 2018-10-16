ARG ALPINE_VERSION
FROM alpine:${ALPINE_VERSION}

# LUA CONFIG
ARG LUA_VERSION
# Find LUA sha's here:
# https://www.lua.org/ftp/
ARG LUA_SHA1

ARG LUA_NAMED_VERSION="lua-${LUA_VERSION}"
ARG LUA_FILENAME="${LUA_NAMED_VERSION}.tar.gz"

ENV LUA_DIR=/.lua

RUN set -eu; \
	apk add --no-cache --virtual .lua-deps \
	    build-base=0.5-r1 \
	    linux-headers=4.4.6-r2 \
	    readline-dev=7.0.003-r0 \
		curl=7.61.1-r \
		make=4.2.1-r2 \
		gcc=6.4.0-r9 \
		; \
    mkdir -p /tmp/lua/ ; \
    cd /tmp/lua/ ; \
    curl -L -o "${LUA_FILENAME}" https://www.lua.org/ftp/${LUA_FILENAME} ; \
    test "$(sha1sum ${LUA_FILENAME} | awk '{print $1;}')" == "$LUA_SHA1" ; \
    tar xzf "/tmp/lua/${LUA_FILENAME}"  -C /tmp/lua/ ; \
    cd "${LUA_NAMED_VERSION}" ; \
    mkdir -p $LUA_DIR; \
    make linux install INSTALL_TOP="$LUA_DIR" ; \
    apk del .lua-deps ; \
    rm -rf /tmp/lua/
