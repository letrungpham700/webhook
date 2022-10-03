#!/bin/env python3
"""
Line Notify Gateway Application
License: MIT
"""

import logging
import requests
from datetime import datetime, timezone
import dateutil.parser
import pytz

from flask import Flask, render_template, request, jsonify

import manage_logs

LOG_PATH = '/opt/webhook/logs/line-notify-gateway.log'
LINE_NOTIFY_URL = 'https://notify-api.line.me/api/notify'
app = Flask(__name__)


def reformat_datetime(alerttime):
    """
    Reformat of datetime to humand readable.
    """
    time_tam = dateutil.parser.parse(alerttime)
    data_time = time_tam.strftime('%Y-%m-%d %H:%M:%S')
    datatime = datetime.strptime(data_time, '%Y-%m-%d %H:%M:%S')
    utc = pytz.timezone('UTC')
    localtz = pytz.timezone('Asia/Ho_Chi_Minh')
    utctime = utc.localize(datatime)
    data = localtz.normalize(utctime.astimezone(localtz))
    timedate = data.strftime('%Y-%m-%d %H:%M:%S')
    return timedate


def firing_alert(request):
    """
    Firing alert to line notification with message payload.
    """
    if request.json['status'] == 'firing':
        status = "Alert"
        time = reformat_datetime(request.json['alerts'][0]['startsAt'])
    else:
        status = "Resolved"
        time = str(datetime.now().date()) + ' ' + str(datetime.now().time().strftime('%H:%M:%S'))
    header = {'Authorization':request.headers['AUTHORIZATION']}
    for alert in request.json['alerts']:
        msg = "\n[Q9-" + status +"] " + alert['annotations']['description'] + "\nTime: " + time 
        msg = {'message': msg}
        response = requests.post(LINE_NOTIFY_URL, headers=header, data=msg)


@app.route('/')
def index():
    """
    Show summary information on web browser.
    """
    logging.basicConfig(filename=LOG_PATH, level=logging.DEBUG)
    return render_template('index.html', name='index')


@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    """
    Firing message to Line notify API when it's triggered.
    """
    logging.basicConfig(filename=LOG_PATH, level=logging.DEBUG)
    logging.debug(str(request))
    if request.method == 'GET':
        return jsonify({'status':'success'}), 200
    if request.method == 'POST':
        try:
            firing_alert(request)
            return jsonify({'status':'success'}), 200
        except:
            return jsonify({'status':'bad request'}), 400


@app.route('/logs')
def logs():
    """
    Display logs on web browser.
    """
    file = open(LOG_PATH, 'r+')
    content = file.read()
    return render_template('logs.html', text=content, name='logs')


@app.route('/metrics')
def metrics():
    """
    Expose metrics for monitoring tools.
    """

if __name__ == "__main__":
    manage_logs.init_log(LOG_PATH)
    app.run(host='0.0.0.0')
