#-*-coding:utf-8-*-
import requests
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

base_url = 'https://api.qschou.com/v4/projects/love'
load = { "category_id": 3353, "total_amount": 300, "purpose": "test",
         "title": "lovetestssssssss测试", "raise_days": 10, "description": "fly away！sssssssfdsf s111",
         "privacy": False,
         "cover": [ { "image": "http://thumb.qschou.com/temp/2016/08/11/0126132072f8b24344785c5e5cad75bb8b0080edh5.jpg@!thumb.png" } ] }
headers = {'Platform':'qsc_ios/1.0.0/v1','Accept':'application/json','DeviceId':'cxzcxzcxzcxz','Content-Type':'application/json;utf-8','Authorization':'aakpsh5zdnwaof3istzxfoht34umqvrogzbh59ve'}
r = requests.post(base_url,data = json.dumps(load),headers=headers)
code = r.status_code
text = json.loads(r.text)
print text
# print text['error']
# print text['setting_info']['address']['recipient']
# for key in text:
#     print '%s : %s' % (key,text[key])
    # if isinstance(text[key], dict):
    #     text = text[key]
    #     for key in text:
    #         print '%s : %s' % (key, text[key])