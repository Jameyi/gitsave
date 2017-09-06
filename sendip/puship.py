#! usr/bin/env python
#! coding:utf-8

import os
import socket
import pycurl,json

def get_local_ip():
    
    cmdip = "ifconfig | grep 'inet addr:' | grep -v '127.0.0.1' | cut -d: -f2 | awk '{ print $1}'"
    ip = os.popen(cmdip).read()
    ip = str(ip).split('\n')[0]
    return(ip)

def get_essid():
    cmdssid = "iwconfig wlan0 | grep 'ESSID:' | cut -d: -f2"
    essid = os.popen(cmdssid).read()
    essid = str(essid).split(' ')[0]
    return(essid)

def post_ip(appID,appSecret,pushEvent,pushMessage):

    appID = appID
    appSecret = appSecret
    pushEvent = pushEvent
    pushMessage = pushMessage

    c = pycurl.Curl()
    c.setopt(c.URL,'https://api.instapush.im/v1/post')
    c.setopt(c.HTTPHEADER,['x-instapush-appid:' + appID,'x-instapush-appsecret:' + appSecret,'Content-Type: application/json'])

    json_fields = {}
    json_fields['event'] = pushEvent
    json_fields['trackers'] = {}
    json_fields['trackers']['message'] = pushMessage
    postfields = json.dumps(json_fields)

    c.setopt(c.POSTFIELDS,postfields)

    c.perform()
    c.close()

if __name__ == "__main__":
    ip = get_local_ip()
    essid = get_essid()
    appID = "597320e2a4c48a1455de80b2"
    appSecret = "6f1b417cb01195fe337710012e81004c"
    pushEvent = "IP"
    pushMessage = essid + ":" + ip
    post_ip(appID,appSecret,pushEvent,pushMessage)
    #print(essid + ":" + ip)

