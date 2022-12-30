import json
import os

from DataBase.crud_service import *

with Session(engine) as db:
    for filename in os.listdir('../TG_bot_backup/'):
        if '.json' not in filename:
            continue
        user_id = filename[filename.find('_') + 1: filename.find('.')]
        with open('../TG_bot_backup/' + filename, 'r') as f:
            data = json.load(f)
            print(len(data))
        if 'instructions' in filename:
            for row in data:
                add_inst(db, int(user_id), row['key'], row['message_id'])
        if 'notification' in filename:
            for row in data:
                activ_date = datetime.strptime(row['activation_date'], '%Y-%m-%dT%H:%M:%S')
                add_notif(db, int(user_id), row['remind_text'], activ_date)
        if 'rem' in filename:
            for row in data:
                activ_time = datetime.strptime(row['activation_time'], '%H:%M').time()
                add_remind(db, int(user_id), row['remiand_text'], activ_time)

