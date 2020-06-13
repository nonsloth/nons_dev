from django.db import models

class Profile(models.Model):
    profile_name = models.CharField(max_length=20)
    profile_name_kana = models.CharField(max_length=40)
    profile_age = models.IntegerField(max_length=2)
    profile_height = models.IntegerField(max_length=3)
    profile_blood_type = models.CharField(max_length=2)
    profile_size_b = models.IntegerField(max_length=3)
    profile_size_w = models.IntegerField(max_length=2)
    profile_size_h = models.IntegerField(max_length=3)
    profile_size_c = models.CharField(max_length=1)
    profile_message = models.CharField(max_length=500)
    profile_comment = models.CharField(max_length=500)
    reserve_url = models.CharField(max_length=100)
    twitter_id = models.CharField(max_length=40)
    cast_interval = models.IntegerField(max_length=2)
    crt_prf_user_id = models.CharField(max_length=20)
    crt_prf_date_time = models.DateField()
    upd_prf_user_id = models.CharField(max_length=20)
    upd_prf_date_time = models.DateField()
    
    def __str__(self):
        return 'ID:' + str(self.id) + '| ' + \
            self.profile_name + '(' + self.profile_name_kana + ') ' + \
            str(self.profile_age) + '歳　' + str(self.profile_height) + 'cm ' + \
            self.profile_size_c + 'cup'