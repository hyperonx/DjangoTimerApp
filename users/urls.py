from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import SignUpView



urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name ='password_reset'),

]


# pathpatterns = [
#     # path(r'^$', HomeView.as_view(), name='home'),
#     re_path(r'^register/$', register_view, name='signup'),
#     re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
#             activate, name='users_activate'),
#     re_path('login/', auth_views.LoginView, {
#         'template_name': "users/registration/login.html"},
#         name='login'),
#     re_path('logout/', auth_views.LogoutView,
#         {'next_page': settings.LOGIN_REDIRECT_path}, name='logout'),

#     re_path(r'^password_reset/$', auth_views.PasswordResetView,
#         {'template_name': "users/registration/password_reset_form.html"},
#         name='password_reset'),
#     re_path(r'^password_reset/done/$', auth_views.PasswordResetDoneView,
#         {'template_name': "users/registration/password_reset_done.html"},
#         name='password_reset_done'),
#     re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
#         auth_views.PasswordResetConfirmView,
#         {'template_name': "users/registration/password_reset_confirm.html"},
#         name='password_reset_confirm'),
#     re_path(r'^reset/done/$', auth_views.PasswordResetCompleteView,
#         {'template_name': "users/registration/password_reset_complete.html"},
#         name='password_reset_complete'),
# ]