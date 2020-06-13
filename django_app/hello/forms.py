from django import forms
from.models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [\
            'profile_name', \
            'profile_name_kana', \
            'profile_age',\
            'profile_height', \
            'profile_blood_type', \
            'profile_size_b', \
            'profile_size_w', \
            'profile_size_h', \
            'profile_size_c', \
            'profile_message', \
            'profile_comment', \
            'reserve_url', \
            'twitter_id', \
            'cast_interval', \
            'crt_prf_user_id', \
            'crt_prf_date_time', \
            'upd_prf_user_id', \
            'upd_prf_date_time', \
            ]

class HelloForm(forms.Form):
    name = forms.CharField(label='Name')
    mail = forms.EmailField(label='Email')
    gender = forms.BooleanField(label='Gender', required=False)
    age = forms.IntegerField(label='Age')
    birthday = forms.DateField(label='Birth')
    
class FindForm(forms.Form):
    find = forms.CharField(label='Find', required=False)