import ujson
import os
import time
import glob
import hashlib
import sys


manifest_file = "C:/Program Files (x86)/Steam/steamapps/common/Half-Life/wizardwars_beta.sourcehub.json"

def write_manifest(data):
    with open(manifest_file, "w+") as f:
        ujson.dump(data, f, indent=4)

try:
    with open(manifest_file, "r") as f:
        manifest = ujson.load(f)
except Exception:
    manifest = {"files": {},
                "name": "Error",
                "type": "error",
                "dir": ".",
                "version": "0"}
    
    write_manifest(manifest)

    # probably want to exit instead of continuing
    sys.exit("Error: manifest file not found")

moddir = os.path.join(os.path.dirname(manifest_file), manifest.get("dir", ""))

# get all files in directory recursively
files = glob.glob(moddir + "/**/*", recursive=True)

# for each file, compute the hash and add it to the manifest
for file in files:
    if os.path.isdir(file):
        continue

    with open(file, "rb") as f:
        hash = hashlib.sha256(f.read()).hexdigest()

    # get relative path to manifest file
    relative_path = os.path.relpath(file, moddir)

    # add to manifest
    manifest['files'][relative_path] = {
        "hash": hash,
        "size": os.path.getsize(file)
    }

manifest['timestamp'] = int(time.time())

write_manifest(manifest)
