from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm

# Create your views here.
def home(request):
	# revision del usario para ingresar de manera correcta
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		# Autenticacion
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, "Login con exito!")
			return redirect('home')
		else:
			messages.success(request, "Algo salio mal, revisa tu usuario o tu password")
			return redirect('home')
	else:
		return render(request, 'home.html', {})



def logout_user(request):
	logout(request)
	messages.success(request, "has salido")
	return redirect('home')



def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "Registro Exitoso!")
			return redirect('home')
	else:
		form = SignUpForm()
		return render(request, 'register.html', {'form':form})

	



