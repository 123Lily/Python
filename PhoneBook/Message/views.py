from django.shortcuts import render
from django.http import HttpResponse
from Message.models import MessageUser
from .UserForm import UserForm
from django.http import HttpResponseRedirect

from django import forms

class AddForm(forms.Form):
	add_name=forms.CharField()
	add_phone=forms.CharField()
	add_address=forms.CharField()
	add_other=forms.CharField()

# Create your views here.
def index(request):  #主页
	content='欢迎光临号码不离，We Are All Here!'
	#return HttpResponse('欢迎光临号码不离，We Are All Here!')
	return render(request,'index.html',{'content':content})

def phone(request):  #通讯录首页
	messageuser=MessageUser.objects.all()
	return render(request,'phone.html',{'messageuser':messageuser})

def updata(request):  #更新数据
	messageuser=MessageUser.objects.all()
	return render(request,'updata.html',{'messageuser':messageuser})

def add(request):    #添加联系人
	if request.method=='POST':
		addform=AddForm(request.POST)
		if addform.is_valid():
			Name=addform.cleaned_data['add_name']
			PhoneNum=addform.cleaned_data['add_phone']
			Address=addform.cleaned_data['add_address']
			Other=addform.cleaned_data['add_other']
			# Name=addform.cleaned_data['add_name']
			new_user=MessageUser.objects.get_or_create(Name=Name,PhoneNum=PhoneNum,Address=Address,Other=Other)
			# return HttpResponse('添加成功！')
			return HttpResponseRedirect('..')

	else:
		addform=AddForm()
	return render(request, 'add.html',{'addform':addform})

def detail(request,pk,):  #联系人详细信息
	user=MessageUser.objects.get(pk=pk)
	return render(request, 'detail.html',{'user':user})

def delete(request):
	return render(request, 'delete.html')