from xml.etree.ElementTree import Comment
from flask import Flask, request, jsonify
import re
import requests
import json

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        probe = request.form['probe']
        device = request.form['device']
        name = request.form['name']
        status = request.form['status']
        down = request.form['down']
        link = request.form['linksensor']
        comment = request.form['comment']
        commentarray = comment.split('\\')
        print(commentarray)
        prov = re.sub(r'[^\w .,:]', "", commentarray[1])
#        prov = " ".join(prov)
        phone = re.sub(r'[^\w .,:]', "", commentarray[2])
        addres = re.sub(r'[^\w .,:]', "", commentarray[3])
        dog = re.sub(r'[^\w .,:]', "", commentarray[4])
        ip = re.sub(r'[^\w .,:]', "", commentarray[6])
        mask = re.sub(r'[^\w .,:]', "", commentarray[7])
        gw =re.sub(r'[^\w .,:]', "", commentarray[8])
        dns = re.sub(r'[^\w .,:]', "", commentarray[9])
	
    if status == 'Up':
        color = "#99ff99"
    else:
        color = "#ff0000"

    URL = ''
    headers = {
        'content-type': 'application/json',
        'X-Auth-Token': '',
        'X-User-Id': ''
    }
    data = '''{
   "message": {
      "rid": "bcatjSZsF5phRDpHZ",
      "attachments": [{
            "color": "'''+ color +'''",
            "text": "PRTG",
            "fields": [{
              "short": true,
              "title": "БЮ",
              "value": "'''+ probe +'''"
            },{
              "short": true,
              "title": "Канал",
              "value": "'''+ device +'''"
            },{
              "short": true,
              "title": "Сенсор",
              "value": "'''+ name +'''"
            },{
              "short": true,
              "title": "Статус",
              "value": "'''+ status +'''"
            },{
              "short": true,
              "title": "Сообщение",
              "value": "'''+ down +'''"
            },{
              "short": true,
              "title": "",
              "value": ""
            },{
              "short": false,
              "title": "Информация для звонка",
              "value": "'''+ prov +'''\\n'''+ phone +'''\\n'''+ addres +'''\\n'''+ dog +'''\\n'''+ ip +'''\\n'''+ mask +'''\\n'''+ gw +'''\\n'''+ dns +'''"
            },{
              "short": false,
              "title": "Ссылка",
              "value": "'''+ link +'''"
            }]
      }]
  }
}'''
    print(data)
    r = requests.post(url = URL,  headers= headers, data = data.encode('utf-8') )
    return 'web'
app.run(host='0.0.0.0', port=8001)
