from django.shortcuts import render_to_response, get_list_or_404

from pastebin.pasteapp.models import Pastebin

def text_by_user(request, text):
	textList = get_list_or_404(Pastebin, nick=text)
	return render_to_response('text_by_user.html',{'textList': textList})