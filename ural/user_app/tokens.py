from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.tokens import PasswordResetTokenGenerator

from six import text_type

class TockenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp: int):
        return (
            text_type(user.pk) + text_type(timestamp)
        )
    
generate_token = TockenGenerator()