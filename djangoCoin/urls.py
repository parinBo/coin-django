from django.contrib import admin
from django.urls import path
from coin import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('logout', auth_views.LogoutView.as_view(),name='logout'),
    path('login/signup',views.register,name="register"),
    path('addcoin',views.addcoin)

]
