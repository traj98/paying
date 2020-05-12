from django.contrib.auth import views
from accounts import views
from django.urls import path
from .views import *
from django.conf.urls import url
# from .views import validate_username
# from .views import (
#     RemindUsernameView,ActivateView,ChangeEmailView, ChangeEmailActivateView,ResendActivationCodeView

# )
		

urlpatterns =[
			path('signup/',register,name='signup'),
			path('index/',index,name='index'),
			# path('profile',profile,name='profile'),
			# url(r'^ajax/validate_username/$',validate_username,name='validate_username'),
           	path('login/',login_user,name='login'),
			path('logout/',logout_user,name='logout'),
			url(r'^user/edit/(?P<id>[0-9A-Za-z_\-]+)/$',views.edit_profile,name='edit'),
			#url(r'^view_profile/$', view_profile, name ='view_profile'),
			# path('password-change/',views.PasswordChangeView.as_view(),name='password_change'),
			# path('password-change/done/',views.PasswordChangeDoneView.as_view(),name='password_change_done'),
			# path('password-reset/',views.PasswordResetView.as_view(),name='password_reset'),
			# path('password-reset/done/',views.PasswordResetDoneView.as_view(),name='password_reset_done'),
			# path('reset/<uidb64>/<token>/',views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
			# path('reset/done/',views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
			# path('remind/username/', RemindUsernameView.as_view(), name='remind_username'),
			# path('activate/<code>/', ActivateView.as_view(), name='activate'),
			# path('user_done/',User_message,name='user_done'),
   #  		path('change/email/', ChangeEmailView.as_view(), name='change_email'),
   #  		path('change/email/<code>/', ChangeEmailActivateView.as_view(), name='change_email_activation'),
			# path('resend/activation-code/', ResendActivationCodeView.as_view(), name='resend_activation_code'),

	
	
]