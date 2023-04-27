import json
from pprint import pprint

import requests
from combidata import Process
from combidata.classes.combination import Combination

from const import HOST, AGENT_ID


def export(combination: Combination):
    pprint(combination.formed_data)
    sent_request = json.dumps(combination.formed_data)
    received_json = requests.post(f"{HOST}send", headers={"agent": AGENT_ID}, data=sent_request).text
    combination.cache.update({"received_json": json.loads(received_json)})
    pprint(combination.cache["received_json"])
    return True


def ask(combination: Combination):
    sent_request = json.dumps(combination.cache["received_json"])
    received_json = requests.post(f"{HOST}receive", headers={"agent": AGENT_ID}, data=sent_request).text
    combination.cache.update({"saved_data": json.loads(received_json)})
    pprint(json.loads(received_json))
    return True


def compare(combination: Combination):
    del combination.cache["saved_data"]["TARGETID"]
    if combination.cache["saved_data"] != combination.formed_data:
        combination.cache.update({"result": False})
        return True
    combination.cache.update({"result": True})
    return True


def er_compare(combination: Combination):
    if combination.cache["received_json"] != combination.main_case.additional_fields["error"]:
        combination.cache.update({"result": False})
        return True
    combination.cache.update({"result": True})
    return True


EXPORT = Process("EXPORT", export)
ASK = Process("ASK", ask)
COMPARE = Process("COMPARE", compare)
ER_COMPARE = Process("ER_COMPARE", er_compare)