import re
from datetime import datetime, timedelta

from pydantic import ValidationError

from RequestParse.parsed_data_clasess import NotificationData, RemindsData, InstructionData
from RequestParse.support_functions import validation_check
from constants import notification_pattern_words, reminder_pattern_words, instruction_pattern_words


def get_notification(user_id: int, message: str):
    pattern = '|'.join(notification_pattern_words)
    user_id, message = validation_check(user_id, message, pattern)

    request_text = re.findall(pattern, message)[0].strip()
    notif_text = message.replace(request_text, '', 1).strip()

    if request_text == 'завтра' or request_text == 'tomorrow':
        request_text = 'in 1 day'
    elif re.match(r'^day after tomorrow|^послезавтра', request_text):
        request_text = 'in 2 days'
    elif re.match(r'^через неделю|^a week later', request_text):
        request_text = 'in 7 days'

    if re.search(r'\d+', request_text):
        if re.match(r'^\d{2}\.\d{2}\.\d{4}', request_text):
            exec_date = datetime.strptime(request_text, '%d.%m.%Y')
        elif re.match(r'^\d{2}\.\d{2}\.\d{2}', request_text):
            exec_date = datetime.strptime(request_text, '%d.%m.%y')
        else:
            value = int(re.search(r'\d+', request_text).group())
            exec_date = datetime.today() + timedelta(days=value)
    else:
        raise ValidationError

    return NotificationData(user_id=user_id, notif_text=notif_text, exec_datetime=exec_date)


def get_remind(user_id: int, message: str):
    pattern = '|'.join(reminder_pattern_words)
    user_id, message = validation_check(user_id, message, pattern)

    request_text = re.findall(pattern, message)[0].strip()
    rem_text = message.replace(request_text, '', 1).strip()

    exec_str_time = re.search(r'\d?\d:\d\d', request_text).group()
    request_text = request_text.replace(exec_str_time, '')
    if len(exec_str_time) < 5:
        exec_str_time = '0' + exec_str_time
    if exec_str_time == '24:00':
        exec_str_time = '00:00'
    exec_time = datetime.strptime(exec_str_time, '%H:%M').time()
    val = re.search(r'\d+', request_text)
    if val is None:
        if 'каждый день' in request_text or 'every day' in request_text:
            cycle = 1
        else:
            cycle = 0
    else:
        cycle = int(val.group())
    return RemindsData(user_id=user_id, rem_text=rem_text, exec_time=exec_time, day_cycle=cycle)


def get_instruction(user_id: int, message_key: str, val_message_id: int):
    pattern = '|'.join(instruction_pattern_words)
    user_id, message_key = validation_check(user_id, message_key, pattern, False)
    if val_message_id is None or val_message_id < 0:
        raise ValueError
    if isinstance(val_message_id, str):
        val_message_id = int(val_message_id)
    elif not isinstance(val_message_id, int):
        raise TypeError
    if re.search(r'^"([^"]+)"', message_key):
        message_key = message_key.replace('"', '').strip()

    return InstructionData(user_id=user_id, key_text=message_key, message_id=val_message_id)
