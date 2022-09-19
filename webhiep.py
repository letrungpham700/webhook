from flask import Flask, request, abort
from datetime import datetime
from pathlib import Path
import requests
import os
import json


app = Flask(__name__)
TOKEN_GL = "9T53aaAU5Xvvu7VI7n8dxHvwAgpFXcsi20b4iNzqW9a"
TOKEN_TEST = "SvP2mdmsRNyaFd4b0GL3kGDDGwGZtay7cH5yD50srmC"
FILE = "/home/pthiep/log"
FILE1 = "/home/pthiep/ip-vpn"
URL = "https://notify-api.line.me/api/notify"


@app.route('/' + TOKEN_GL, methods=['POST'])
def webhook():
    if request.method == 'POST':
        writelog(request.json, "vpn")
        data = json.dumps(request.json)
        dataextra = json.loads(data)
        extrajson(dataextra)
        return 'success', 200
    else:
        abort(400)


@app.route('/' + TOKEN_TEST, methods=['POST'])
def webhook1():
    if request.method == 'POST':
        writelog(request.json, "test")
        data = json.dumps(request.json)
        dataextra = json.loads(data)
        extrajson(dataextra)
        return 'success', 200
    else:
        abort(400)


def extrajson(message):
    try:
        check = message["event_definition_title"]
        if(check == "VPN-SERVER"):
            dataiptruycap = message["event"]["group_by_fields"]["ip_truy_cap"]
            dataport = message["event"]["group_by_fields"]["port"]
            dataipuservpn = message["event"]["group_by_fields"]["ip_user_vpn"]
            writefile(dataipuservpn, dataiptruycap, dataport)
        elif(check == "VPN-GG-AUTHEN"):
            datauser = message["event"]["group_by_fields"]["USERNAME"]
            datasend = "\"[VPN-VDC-New]: User " + datauser + \
                " AUTH_FAILED, Google Authenticator is incorrect\""
            sendline(datasend, TOKEN_GL)
        elif(check == "VPN-WRONG-MAC"):
            datauser = message["event"]["group_by_fields"]["USERNAME"]
            datasend = "\"[VPN-VDC-New]: User " + datauser + \
                " AUTH_FAILED, Wrong MAC/UUID address hardware\""
            sendline(datasend, TOKEN_GL)
        else:
            datasend = "abc"
            sendline(datasend, TOKEN_TEST)
    except:
        print("ERROR")


def writelog(message, name):
    try:
        path = Path(FILE)
        if not path.is_dir():
            os.system("mkdir " + FILE)
        logfiledata = (datetime.now().strftime(name + '-%d-%m-%Y.log'))
        createfile = os.system("touch " + FILE + "/" + logfiledata)
        with open(FILE + "/" + logfiledata, 'a') as f:
            f.write(datetime.now().strftime('[%H:%M:%S] - '))
            json.dump(message, f)
            f.write('\n')
        f.close()
    except:
        print("writelog")


def writefile(ipvpn, ipvm, port):
    try:
        logfiledata = (datetime.now().strftime("vpn" + '-%d-%m-%Y.csv'))
        createfile = os.system("touch " + FILE1 + "/" + logfiledata)
        with open(FILE1 + "/" + logfiledata, 'a') as f:
            f.write(ipvpn + " " + ipvm + " " + port + "\n")
        f.close()
    except:
        print("writefile")


def sendline(message, token):
    payload = {"message": message}
    r = requests.post(URL, data=payload, headers={'Authorization': 'Bearer {}'.format(
        token), 'Content-Type': 'application/x-www-form-urlencoded'})


if __name__ == '__main__':
    app.run(host='172.16.61.118', port=8000, debug=True)