import re

from pydantic import ValidationError

from RequestParse.parsed_data_clasess import NotificationData
from constants import notification_pattern_words


def get_notification(user_id: int, message: str):
    pattern = '|'.join(notification_pattern_words)
    if not re.match(pattern, message):
        raise ValidationError
    if user_id is None:
        raise ValueError

    request_text = re.findall(pattern, message)[0].strip()
    notif_text = message.replace(request_text, '', 1).strip()

    return request_text, notif_text


