# -*- coding: utf-8 -*-
# from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.
# from datetime import datetime
# import pytz
# tz = pytz.timezone('UTC')
# print datetime.datetime.now(tz=tz)
# tz1 = pytz.timezone('Asia/Shanghai')
# print datetime.datetime.now(tz=tz1)

# result = {}
# real_country_name = ['英国格林尼治时间', '香港']
# country_list = ['UTC', 'Asia/Shanghai']
# for i in range(len(country_list)):
#     tz = pytz.timezone(country_list[i])
#     result[real_country_name[i]] = datetime.datetime.now(tz=tz)
# for k, v in result.iteritems():
#     print k, v

#
# class uzi(object):
#     def __init__(self, data):
#         self.name = data['site']
#         self.time = data['time']
#
#
# result = {}
# data = {}
# data['c'] = []
# time_now = []
# real_country_name = ['英国格林尼治时间', '香港']
# country_list = ['UTC', 'Asia/Shanghai']
# for i in range(len(country_list)):
#     tz = pytz.timezone(country_list[i])
#     result[real_country_name[i]] = datetime.now(tz=tz)
#     time_now.append(datetime.now(tz=tz))
#     # data = {'site': real_country_name, 'time': time_now}
#     ob = {'site': real_country_name[i], 'time': datetime.now(tz=tz)}
#     data['c'].append(uzi(ob))
# for i in data['c']:
#     print i.name
#     print i.time
# print data

# print pytz.all_timezones

data = {'all': [{'name': '\xe8\xbe\xbe\xe6\x8b\x89\xe6\x96\xaf', 'time': '2018-04-03 04:57:12'}, {'name': '\xe9\xa6\x96\xe5\xb0\x94', 'time': '2018-04-03 18:57:12'}, {'name': '\xe6\xb4\x9b\xe6\x9d\x89\xe7\x9f\xb6', 'time': '2018-04-03 02:57:12'}, {'name': '\xe6\x97\xa5\xe6\x9c\xac', 'time': '2018-04-03 18:57:12'}, {'name': '\xe6\xb3\x95\xe5\x85\xb0\xe5\x85\x8b\xe7\xa6\x8f', 'time': '2018-04-03 11:57:12'}, {'name': '\xe6\x96\xb0\xe5\x8a\xa0\xe5\x9d\xa1', 'time': '2018-04-03 17:57:12'}, {'name': '\xe7\xba\xbd\xe7\xba\xa6', 'time': '2018-04-03 05:57:12'}, {'name': '\xe9\xa6\x99\xe6\xb8\xaf', 'time': '2018-04-03 17:57:12'}, {'name': '\xe8\x8b\xb1\xe5\x9b\xbd\xe6\xa0\xbc\xe6\x9e\x97\xe5\xb0\xbc\xe6\xb2\xbb\xe6\x97\xb6\xe9\x97\xb4', 'time': '2018-04-03 09:57:12'}]}


def write_html(data):
    result = ''
    for each in data['all']:
        r = '''
        <tr style=\"height: 10px\">
            <td style=\"font-size: 30px\">%s</td>
            <td style=\"font-size: 30px\">%s</td>
        </tr>
        ''' % (each["name"], each["time"])
        result += r
    return result
write_html(data)