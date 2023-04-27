import requests

from const import AGENT_ID, HOST


def main():
    print(requests.get(HOST + "fix", headers={"agent": AGENT_ID, "field": "ID_CARD"}).text)

if __name__ == '__main__':
    main()