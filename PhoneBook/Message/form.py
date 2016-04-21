from django import forms
from django.contrib.auth.models import User

class UserForm(forms.Form):
	Name=forms.CharField(max_length=100) #姓名
	# PhoneNum=forms.CharField(max_length=100)
	# UpdateTime=forms.DateTimeField()

	# Address=forms.TextField()		#住址
	# Other=forms.TextField()    #其他

class AddForm(forms.Form):
	add_name=forms.CharField()
	add_phone=forms.CharField()
	add_address=forms.CharField(required=False)
	add_other=forms.CharField(required=False)

class LoginForm(forms.Form):
	username=forms.CharField(
			required=True,
			label=r'用户名',
			error_messages={'required':'请输入用户名'},
			widget=forms.TextInput(
					attrs={
						'placeholder':r'用户名',
					}
				),
		)
	password=forms.CharField(
			required=True,
			label=r'密码',
			error_messages={'required':'请输入密码'},
			widget=forms.PasswordInput(
					attrs={
						'placeholder':r'密码',
					}
				),
		)
	def clean(self):
		if not self.is_valid():
			raise forms.ValidationError(r'用户名和密码为必填项')
		else:
			cleaned_data=super(LoginForm,self).clean()