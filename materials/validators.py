import re
from rest_framework.exceptions import ValidationError


class YouTubeLinkValidator:
    reg = re.compile(r"\b(?!https?://(?:www\.)?youtube\.com)https?://(?:www\.)?\S+\b")

    def __init__(self, fields):
        self.fields = fields

    def __call__(self, value):
        for field_name in self.fields:
            field = value.get(field_name, '')
            if self.reg.findall(field):
                raise ValidationError('Запрещенная ссылка. Можно использовать материалы ссылок только с youtube.com!')
