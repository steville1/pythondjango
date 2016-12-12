from django.shortcuts import render
from .models import Assignment
from django.http import HttpResponse
from django.template import loader
#from forms import AssignmentForm
from .forms import AssignmentForm
from django.http import HttpResponseRedirect
from django.template.context_processors import csrf


# Create your views here.
def index(request):
	return render(request, "index.html")

def listdata(requests):
		all_assignment=Assignment.objects.all()
		template=loader.get_template('list_data.html')
		context={
		'all_assignment':all_assignment,

		}
		return HttpResponse(template.render(context, requests))

def create(request):
	if request.POST:
		form=AssignmentForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/assignment/list')
	else:
		form=AssignmentForm()
	args = {}
	#args.update(csrf(request))
	args['form']=form
	#return render('create_assignment.html', args)
	return render(request, 'create_assignment.html', args)

	


	