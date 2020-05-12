from django.contrib.auth.models import User


class EditProfileForm(ModelForm):
	class Meta:
		model = User
		fields = ('email','first_name','last_name')


class ProfileForm(ModelForm):
	class Meta:
		model = UserProfile
		fields = ('phone', 'sex') #Note that we didn't mention user field here.
