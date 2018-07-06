# -*- coding: utf-8 -*-
from views import *
from datetime import datetime, timedelta, tzinfo
import pytz
import json
from django.http.response import JsonResponse


def index(request):
    return render(request, "time/index.html")


def set_time(request):
    data = {}
    data['all'] = []
    country_list = {'英国格林尼治时间': 'UTC',
                    '新加坡': 'Asia/Singapore',
                    '达拉斯': 'America/Chicago',
                    '洛杉矶': 'America/Los_Angeles',
                    '纽约': 'America/New_York',
                    '法兰克福': 'Europe/Berlin',
                    '日本': 'Japan',
                    '首尔': 'Asia/Seoul',
                    '北京/香港': 'Asia/Shanghai'
                    }
    for i in sorted(country_list.keys()):
        tz = pytz.timezone(country_list[i])
        timenow = datetime.now(tz)
        # data['all'][i] = timenow
        data['all'].append({'name': i, 'time': str(timenow)[0:19]})
    data['all'] = write_html(data)
    return JsonResponse(data)


def write_html(data):
    result = "<table class='table table-bordered' id='table'>"
    for each in data['all']:
        r = '''
    <tr style=\"height: 10px\">
        <td style=\"font-size: 30px\">%s</td>
        <td style=\"font-size: 30px\">%s</td>
    </tr>
    ''' % (each["name"], each["time"])
        result += r
    result += '</div>'
    return result