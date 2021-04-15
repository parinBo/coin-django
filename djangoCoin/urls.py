from django.contrib import admin
from django.urls import path,include
from coin.Views import coinviews,homeviews
from django.contrib.auth import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.LoginView.as_view(template_name='login.html'),name='login'),
    path('logout', views.LogoutView.as_view(),name='logout'),
    path('',homeviews.home,name="home"),
    path('login/signup',homeviews.register,name="register"),
    path('coin/addcoin',coinviews.addcoin),
    path('coin/history',coinviews.history),
    path('coin/mycoin',coinviews.mycoin),
    path('coin',coinviews.mycoin)

]
