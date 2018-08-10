from django.db import models

class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=32)
    password = models.CharField(max_length=256)
    true_name = models.CharField(max_length=32, blank=True, null=True)
    id_card = models.CharField(max_length=32, blank=True, null=True)
    avatar = models.CharField(max_length=64, blank=True, null=True)
    true_avatar = models.CharField(max_length=64, blank=True, null=True)
    nickname = models.CharField(max_length=32, blank=True, null=True)
    tel = models.IntegerField(blank=True, null=True)
    sex = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=32, blank=True, null=True)
    more_address = models.CharField(max_length=32, blank=True, null=True)
    email = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'

