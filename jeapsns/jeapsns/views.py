from django.http import HttpResponse
import datetime

from django.template import Template, Context
from django.shortcuts import render_to_response
from jeapsns.models import Publisher ,Author
from jeapsns.forms import AuthorForm

def hello(request):
    l1 = Publisher.objects.all()
    au = Author.objects.all()
    f = AuthorForm()
    if request.method == 'POST':
	a = Author(email=request.POST['email'])
	a.save()
    	return render_to_response('hello.html', {'l1': l1,'f':f,'au':au})


    if 'q' in request.GET:
	message = 'You input for: %r' % request.GET['q']
	return HttpResponse(message)
    if 'list' in request.GET:
        return render_to_response('hello.html', {'l1': l1,'f':f,'au':au})

    return HttpResponse("Hello world")

def index(request):
	return HttpResponse("This is index page!")

def current_time(request,string,offset):
	print offset,string
	try:
        	offset = int(offset)
    	except ValueError:
        	raise Http404()
    	#dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    	dt = datetime.datetime.now()  
    	html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    	return HttpResponse(html)

def index_temp(request,input_name,color):
	t = Template('My name is<font color =#{{color}}> {{ name }}.</font>')
	c = Context({'name': input_name,'color':color})
	return HttpResponse(t.render(c))

def index_temp_file(request,color):
	return render_to_response('index_temp_file.html', {'color':color})
