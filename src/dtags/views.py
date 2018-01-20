from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from dtags.models import Dtag

class Landing:
	def index(request):
		return render(request, 'dtags/index.html')

class Create:
	def index(request):
		if request.method == 'GET': # what the fuck is this for?
			return render(request, 'dtags/create.html')
		if request.method == 'POST':
			form = DtagForm(request.POST)
			if form.is_valid():
				# Should do some validation here ...
				dtag_temp = form.save(commit=False)
			else:
				form = DtagForm()
			return render_to_response('dtags/create.html', {'DtagForm': form})



class Read:
	def index(request):
		all_patients = Dtag.objects.order_by('severity', '-date_created')
		cxt = {"patients": all_patients}
		return render(request, 'dtags/read.html', cxt)

	def info(request, patient_id):
		patient = get_object_or_404(barcode_id=patient_id)
		cxt = {"patient": patient}
		return render(request, 'dtags/patient_info.html', cxt)

