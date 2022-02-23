import json
import requests

info = json.loads(requests.get("https://api.whatexploitsare.online/status").text)

def get_status(exploit):
    if exploit == "synapse":
        return info[0]["Synapse"]["updated"]
    elif exploit == "scriptware":
        return info[1]["Script-Ware"]["updated"]
    elif exploit == "krnl":
        return info[2]["KRNL"]["updated"]
    elif exploit == "temple":
        return info[3]["Temple"]["updated"]
    elif exploit == "electron":
        return info[6]["Electron"]["updated"]
    elif exploit == "wearedevs":
        return info[8]["WeAreDevs API"]["updated"]
    elif exploit == "oxygenu":
        return info[9]["Oxygen"]["updated"]
    elif exploit == "fluxus":
        return info[10]["Fluxus"]["updated"]
    elif exploit == "celery":
        return info[11]["Celery"]["updated"]
    elif exploit == "roware":
        return info[12]["Ro-Ware"]["updated"]
    elif exploit == "westeria":
        return info[4]["Westeria"]["updated"]
    elif exploit == "dx9ware":
        return info[5]["DX9WARE"]["updated"]
    elif exploit == "atlas":
        return info[7]["Atlas"]["updated"]
    else:
        return "Error : exploit not found"
