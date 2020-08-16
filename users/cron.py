from datetime import datetime
from .models import Profile
from django.contrib.auth.models import User
import pytz


def delete_expired_user():
    users_to_check = Profile.objects.filter(user_type=False)
    f = open("log.txt",'a')
    now_datetime= datetime.now()
    utc=pytz.UTC
    now_datetime = utc.localize(now_datetime)
    f.write(" Log Entry triggered at : "+now_datetime)
    for i in u:
        if i.expire_date < now_datetime:
            userid = i.user_id
            u = User.objects.get(id = userid)
            u.delete()
            f.write("The user with id: "+userid+" expired at "+i.expire_date+" is deleted.\n")