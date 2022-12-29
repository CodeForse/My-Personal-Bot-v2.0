import re

from pydantic import ValidationError


def validation_check(user_id, message, pattern):
    if user_id is None or message == '':
        raise ValidationError

    if isinstance(user_id, str):
        user_id = int(user_id)
    elif not isinstance(user_id, int):
        raise TypeError

    if not re.match(pattern, message):
        raise ValidationError

    message = message.lower()
    return user_id, message
