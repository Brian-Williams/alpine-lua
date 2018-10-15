#!/usr/bin/env python3

# Travis-likes aren't conducive to DRY; this script simplifies matrix creation
# python ^3.6

from collections import namedtuple
import itertools
import requests
from pkg_resources import parse_version

# All versions of lua with their tarball SHA1 to be included in the matrix
lua_include = [
    ("5.3.4", "79790cfd40e09ba796b01a571d4d63b52b1cd950"),
    ("5.2.4", "ef15259421197e3d85b7d6e4871b8c26fd82c1cf"),
]

# Lowest version to include in alpine tag searching
alpine_include_vfloor = "3.7"


BUILD_LUA_VERSION = "LUA_VERSION"
BUILD_LUA_SHA1 = "LUA_SHA1"
BUILD_ALPINE_VERSION = "ALPINE_VERSION"
BUILD_TAG = "TAG"

Lua = namedtuple("Lua", ["version", "sha1"])
luas = [Lua(version, sha1) for version, sha1 in lua_include]


def get_tags(repo_name):
    """Get all tag names for a given repository"""
    # We can use something more lengthy if need be in the future
    # https://github.com/moby/moby/issues/17238#issuecomment-374930433
    url = f"https://registry.hub.docker.com/v1/repositories/{repo_name}/tags"
    r = requests.get(url)
    return [tag_data['name'] for tag_data in r.json()]


# @ commit time versions are: ["3.7", "3.8"]
# This will also filter non-versioned tags like 'latest', 'edge', 'dev' etc.
alpines = [tag for tag in get_tags('alpine') if parse_version(tag) >= parse_version(alpine_include_vfloor)]


matrix = ["matrix:",
          "  include:"]

for l, a in itertools.product(luas, alpines):
    tag = f"alpine{a}-lua{l.version}"
    matrix.append(f"  - name: {tag}")
    matrix.append(f"    env: {BUILD_LUA_VERSION}={l.version} {BUILD_LUA_SHA1}={l.sha1} {BUILD_ALPINE_VERSION}={a} "
                  f"{BUILD_TAG}={tag}")

if (len(matrix) - 2) > 200:
    print("Can't have 201+ jobs per repo, you either need an exclude matrix or to shrink the include matrix.")

build_matrix = '\n'.join(matrix)
print(build_matrix)
