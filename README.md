# coin-django

## Startserver
python3 manage.py runserver 
---
## Auth django
[auth default](https://docs.djangoproject.com/en/3.1/topics/auth/default/)
### create user 
include from django.contrib.auth.models import User
[auth user mode](https://docs.djangoproject.com/en/3.1/ref/contrib/auth/)

### login and logout
* login [docs](https://docs.djangoproject.com/en/2.0/topics/auth/default/#django.contrib.auth.login)
* logout [docs](https://docs.djangoproject.com/en/2.0/topics/auth/default/#django.contrib.auth.logout)
login and logout  easy way to manage is add  *from django.contrib.auth import views as auth_views,logout* like this
and add path login/logout
```
from django.contrib.auth import views as auth_views,logout
path('login/', auth_views.LoginView.as_view(template_name='login.html'),name='login'),
path('logout', auth_views.LogoutView.as_view(),name='logout'),
```


### login rquired
* limit access user  don't *forget* include *LOGIN_URL* in setting.py
[login access](https://docs.djangoproject.com/en/2.0/topics/auth/default/#django.contrib.auth.decorators.login_required)

