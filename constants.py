import numpy as np

from base_classes import *
import pydantic

KEYS = Keys(_env_file='.env', _env_file_encoding='utf-8')

notification_pattern_words = np.array([r'^через \d+ дней', r'^через \d+ день', r'^завтра', r'^послезавтра', r'^через неделю', r'^\d{2}\.\d{2}\.\d{2}', r'^\d{2}\.\d{2}\.\d{4}', r'^in \d+ day', r'^in \d+ days', r'^tomorrow', r'^day after tomorrow', r'^a week later', r'^in a week'])
reminder_pattern_words = np.array([r'^\d?\d:\d\d', r'^в \d?\d:\d\d', r'^\d?\d:\d\d every \d+ days', r'^\d?\d:\d\d every \d+ day', r'^\d?\d:\d\d every day', r'^\d?\d:\d\d каждый день', r'^\d?\d:\d\d каждый \d+ день', r'^\d?\d:\d\d каждые \d+ дней'])
instruction_pattern_words = np.array([r'^"([^"]+)"'])

