from django.shortcuts import render_to_response, get_list_or_404

from pastebin.pasteapp.models import Pastebin

def text_by_user(request, text):
	textList = get_list_or_404(Pastebin, nick=text)
	return render_to_response('text_by_user.html',{'textList': textList})
	

def index(request):
	return render_to_response('index.html')
	
	
def pasteForm(request):
	if request.method = 'POST': #form has been submitted
		form = pasteForm(request.POST) #store POST data
		if form.is_valid(): #Validation rules
			
			return HttpResponseRedirect('/thanks/') #message after post
	else:
		form = pasteForm()
		
	return render_to_response('contact.html',{'form':form})
		