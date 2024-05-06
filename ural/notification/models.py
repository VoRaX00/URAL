from django.db import models
from user_app.models import User

MAYBECHOICE = (
    ('y', 'Yes'),
    ('n', 'No'),
    ('u', 'Unknown'),
)
class Notify(models.Model):
    name = models.TextField()
    first_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='first_user_notifications')
    second_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='second_user_notifications')
    status = models.CharField(max_length=1, choices=MAYBECHOICE)

    class Meta:
        db_table='notify'