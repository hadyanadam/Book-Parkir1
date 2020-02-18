from django.shortcuts import get_object_or_404, render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.utils import IntegrityError
from api.forms import ParkirForms, SaldoForms
from api.models import Parkir, Saldo, DeadlineParkir
from django.contrib.auth import login, authenticate
import datetime
from .forms import SignUpForm

@login_required(login_url='/accounts/login/')
def index(request):
	if(request.method == 'POST'):
		booking_place = request.POST.get('booking_place')
		print(booking_place)

		parkir_instance = Parkir.objects.get(booking_place=booking_place)
		print(parkir_instance)
		DT = datetime.datetime.now() + datetime.timedelta(minutes=10)
		new_DT = DT.strftime("%b %d, %Y %H:%M:%S")
		try:
			deadline = DeadlineParkir(parkir=parkir_instance,deadline=new_DT)
			deadline.save()
		except IntegrityError:
			deadline = DeadlineParkir.objects.get(parkir=parkir_instance)
			deadline.deadline = new_DT
			deadline.save()
		form = ParkirForms(request.POST or None, instance=parkir_instance)
		if(form.is_valid()):
			# print(form.fields)
			new_form = form.save(commit=False)
			new_form.user = str(request.user)
			new_form.book_status = True
			# print(new_form)
			value_saldo = Saldo.objects.get(user=request.user.id)
			field_value = getattr(value_saldo, 'saldo')
			saldo_val = int(field_value) - 5000
			value_saldo.saldo = saldo_val
			if saldo_val < 0:
				return HttpResponse('<html><body><h1>Saldo Tidak Mencukupi</h1><h1>Silahkan isi saldo</h1><a href="/">Back</a></body></html>')
			else:
				value_saldo.save()
				form.save()
				return redirect('book_status/')
	parkir_objek= Parkir.objects.all().order_by("booking_place")
	# A2= Parkir.objects.all()
	# A3= Parkir.objects.all()
	print(parkir_objek)
	saldo = Saldo.objects.get(user=request.user.id)
	context = {
		'title': 'Halaman Utama',
		'heading': 'Silahkan Booking parkir anda',
		'subheading': '',
        'icon': 'static/img/iconmobil.png',
		'icon_x': 'static/img/icon-x.png',
		'parkir_objek':parkir_objek,
		# 'A2':A2,
		# 'A3':A3,
		'saldo':saldo,
	}

	return render(request,'main_page.html',context)

def requestSuccess(request):
	context = {

	}
	return render(request, 'requestsuccess.html',context)

def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			saldo = Saldo(user = user)
			saldo.save()
			login(request, user)
			return redirect('/')
	else:
		form = SignUpForm()
	context = {
		'form': form,
		'title' : 'Signup Page',
		'header': 'Registration Here'
	}
	return render(request, 'signup.html', context)

def update_time(request):
	if request.method == 'POST':
		if 'time' in request.POST:
			time = request.POST['time']
			return HttpResponse('success')
	
# 	return HttpResponse("FAIL")

def recharge(request):
	saldo_instance = get_object_or_404(Saldo,user=request.user.id)
	saldo_asli = saldo_instance.saldo
	if request.method == "POST":
		formset = SaldoForms(request.POST, instance=saldo_instance)
		if formset.is_valid():
			new_form = formset.save(commit=False)
			new_form.saldo = int(request.POST['saldo']) + int(saldo_asli)
			formset.save()
			return redirect('/')
	else:
		formset = SaldoForms()
	saldo = Saldo.objects.get(user=request.user.id)
	context =	{
				'title'		: "Isi Saldo",
				'heading'	: "Silahkan Isi Saldo",
				'formset'	: formset,
				'saldo'		: saldo
				}
	return render(request, 'recharge.html', context)

def booking_true(request):
	try:
		parkir = Parkir.objects.get(user=request.user)
		print(parkir)
	except:
		return redirect('/')
	print(parkir)
	deadline = DeadlineParkir.objects.get(parkir=parkir)
	print(deadline)
	saldo = Saldo.objects.get(user=request.user.id)
	context = {
		'title'		: 'Status Tempat Parkir',
		'heading'	: 'Status Tempat Booking',
		'icon_x'	: '/static/img/iconmobil.png',
		'saldo'		: saldo,
		'parkir'	: parkir,
		'batas'		: deadline,
		}

	return render(request, 'booking_true.html', context)