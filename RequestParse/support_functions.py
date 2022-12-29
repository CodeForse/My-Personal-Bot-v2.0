import re

from pydantic import ValidationError


def validation_check(user_id, message, pattern, lower_mess = True):
    if user_id is None or message == '':
        raise ValidationError

    if isinstance(user_id, str):
        user_id = int(user_id)
    elif not isinstance(user_id, int):
        raise TypeError

    if not re.match(pattern, message):
        raise ValidationError

    if lower_mess:
        message = message.lower()
    return user_id, message
