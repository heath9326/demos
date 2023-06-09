from django.urls import path

from accounts.views import register_page, login_page, logout_user, GetPersonView

urlpatterns = [
    path('register', register_page, name="register_page"),
    path('login', login_page, name='login_page'),
    path('logout', logout_user, name='logout_user'),
    path('getview', GetPersonView.as_view(), name='getview')
]
