import os
import json
import requests
import simplejson
from datetime import datetime

# Version Manifest is used by Minecraft to store release/snapshot metadata
VERSION_MFST_URL = "https://launchermeta.mojang.com/mc/game/version_manifest.json"

# # Specific Manifest is the JSON that is given by the specific version's url
# SPECIFIC_MFST_URL = None

def log_write(log: dict) -> None:
    if not os.path.exists('logs/'):
        os.makedirs('logs/')
    with open(f"logs/{log['timestamp']}-log.txt", "w") as f:
        f.write(json.dumps(log, default=str))

def json_request_handler(url: str) -> dict:
    try:
        version_mfst_response = requests.get(url)
        if version_mfst_response.status_code == 200:
            version_mfst = version_mfst_response.json()
            return version_mfst
        else:
            log = {
                "timestamp": datetime.now(),
                "message": f"VERSION_MFST_URL response code is {version_mfst_response.status_code}",
                "url": url
            }
            log_write(log)
            return None
    except requests.HTTPError as e:
        log = {
                "timestamp": datetime.now(),
                "message": e,
                "url": url
            }
        log_write(log)
        return None
    except simplejson.errors.JSONDecodeError as e:
        log = {
                "timestamp": datetime.now(),
                "message": e,
                "url": url
            }
        log_write(log)
        return None

def fetch_version_manifest(manifest_url: str) -> dict:
    return json_request_handler(manifest_url)

def fetch_specific_manifest(version_mfst: str) -> dict:
    for version in version_mfst['versions']:
        if version['type'] == 'release':
            return version['url']
    return {}

def fetch_specific_jar_link(specific_manifest: str) -> str:
    pass

version_mfst = fetch_version_manifest(VERSION_MFST_URL)
if version_mfst is not None:
    specific_mfst = fetch_specific_manifest(version_mfst)
    if specific_mfst is not None:
        try:
            specific_mfst_jar_link = json_request_handler(specific_mfst)['downloads']['server']['url']
            print(specific_mfst_jar_link)
        except KeyError as e:
            log = {
                "timestamp": datetime.now(),
                "message": e,
                "url": VERSION_MFST_URL
            }
            log_write(log)
            exit()
        except TypeError as e:
            log = {
                "timestamp": datetime.now(),
                "message": e,
                "url": VERSION_MFST_URL
            }
            log_write(log)
            exit()
    else:
        log = {
            "timestamp": datetime.now(),
            "message": e,
            "url": VERSION_MFST_URL
        }
        log_write(log)
        exit()
else:
    log = {
        "timestamp": datetime.now(),
        "message": f"version_mfst is None.",
        "url": VERSION_MFST_URL
    }
    log_write(log)
    exit()