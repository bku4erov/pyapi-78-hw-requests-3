from datetime import datetime, timedelta

import time

import requests


end_date = datetime.date(datetime.today())
start_date = end_date - timedelta(days=2)
# print(start_date, end_date)
start_date_epoch = int(time.mktime(start_date.timetuple()))
end_date_epoch = int(time.mktime(end_date.timetuple()))
# print(start_date_epoch, end_date_epoch)

questions_url = 'https://api.stackexchange.com/2.3/questions'
questions_params = {
    'site': 'stackoverflow',
    'fromdate': start_date_epoch,
    'todate': end_date_epoch,
    'tagged': 'Python',
    'sort': 'activity',
    'order': 'desc'
}
# print(questions_params)
res = requests.get(url=questions_url, params=questions_params)
if res.status_code != 200:
    print(f'Something went wrong! {res}\n{res.json()}')
    exit(-1)
for question in res.json()['items']:
    print(question['title'])