from django.shortcuts import render_to_response, get_list_or_404
from pastebin.pasteapp.models import Pastebin
from pastebin.forms import PasteForm
import datetime


def text_by_user(request, text):
	textList = get_list_or_404(Pastebin, nick=text)
	return render_to_response('text_by_user.html',{'textList': textList})
	

def index(request):
	if request.method == 'POST': #form has been submitted
		form = PasteForm(request.POST) #store POST data
		if form.is_valid(): #Validation rules
			nick = form.cleaned_data['nick']
			title = form.cleaned_data['title']
			content = form.cleaned_data['content']
			expiration = form.clenaed_data['expiration']
			datetime = datetime.datetime.now()
			expiredate = datetime.datetime.now() + datetime.timedelta(seconds=int(expiration))
			
			model = Pastebin(nick, datetime, title, content, expiredate)
			model.save
			
			return HttpResponseRedirect('/' + nick + '/') #message after post
	else:
		form = PasteForm()	
	return render_to_response('index.html',{'form':form})
	

def paste(request):
	if request.method == 'POST': #form has been submitted
		form = PasteForm(request.POST) #store POST data
		if form.is_valid(): #Validation rules
			nick = form.cleaned_data['nick']
			title = form.cleaned_data['title']
			content = form.cleaned_data['content']
			expiration = form.clenaed_data['expiration']
			datetime = datetime.datetime.now()
			expiredate = datetime.datetime.now() + datetime.timedelta(seconds=int(expiration))
			
			model = Pastebin(nick, datetime, title, content, expiredate)
			model.save
			
			return HttpResponseRedirect('/' + nick + '/') #message after post
	else:
		form = pasteForm()
		
	return render_to_response('index.html')#,{'form':form})