from django.urls import path

from accounts.views import register_page, login_page, accounts_index, logout_user

urlpatterns = [
    path('', accounts_index, name='accounts_index'),
    path('register', register_page, name="register_page"),
    path('login', login_page, name='login_page'),
    path('logout', logout_user, name='logout_user')
]
