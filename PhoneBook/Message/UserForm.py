from django import forms
from django.core.validators import RegexValidator

class UserForm(forms.Form):
	Name=forms.CharField(max_length=100) #姓名
	# PhoneNum=forms.CharField(max_length=100)
	# UpdateTime=forms.DateTimeField()

	# Address=forms.TextField()		#住址
	# Other=forms.TextField()    #其他