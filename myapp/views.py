from django.template.loader import get_template
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, RequestContext
from myapp.forms import *
from myapp.models import *
from re import *
from cart import Cart
import json

#partition for instacart copy
def chunks(l, n):
    return [l[i:i+n] for i in range(0, len(l), n)]
    
def sign_up(request):
	if request.method == 'POST':
		name = request.POST.get('full_name')
		biz_name = request.POST.get('biz_name')
		email = request.POST.get('email')
		if Prelim.objects.filter(email=email).exists():
			csrfContext = RequestContext(request)
			return render_to_response('signsuccess.html', csrfContext)
		guest = Prelim(name=name,email=email,bizname=biz_name)
		guest.save()
	csrfContext = RequestContext(request)
	return render_to_response('signsuccess.html', csrfContext)
	
def add_to_cart(request):
	if request.method == 'POST':
		my_key = request.POST.get('key')
		my_qty = request.POST.get('qty')
		my_price = request.POST.get('price')
	item = Item.objects.get(id=my_key)
	cart = Cart(request)
	cart.add(item,my_price,my_qty)
	data = {'status':'success'}
	response = HttpResponse(json.dumps(data),mimetype="application/json")
	return response
	
def get_cart(request):
	cart = Cart(request)
	for item in cart:
		item.key = item.id
		print item.id
	initalData = dict(cart=Cart(request))
	csrfContext = RequestContext(request, initalData)
	return render_to_response('crt.html', csrfContext)

def remove_from_cart(request):
	cart = Cart(request)
	if request.method == 'POST':
		print "hello"
		product_id = request.POST.get('key')
		product_id = int(product_id) - 1
		product = Item.objects.get(id=product_id)
		cart.remove(product)
	initalData = dict(cart=Cart(request))
	csrfContext = RequestContext(request, initalData)
	return render_to_response('cart.html',csrfContext )
	
# Create your views here
def landing_page(request):
	csrfContext = RequestContext(request)
	return render_to_response('landing.html', csrfContext)
	#if request.user is None:
		#return HttpResponseRedirect('/landing/')
	#elif request.user.username == "":
		#return HttpResponseRedirect('/landing/')
		
#Replication of instacart page
# Create your views here, fix for corner case when number of things is 1
def instacart(request):
	list = Item.objects.all()
	big_list = chunks(list,3)
	variables = RequestContext(request,{
		'list':big_list
	})
	return render_to_response('insta.html', variables)
		
def main_page(request):
	template = get_template('buyvi.html')
	variables = Context({'user': request.user})
	output = template.render(variables)
	return HttpResponse(output)
	
def vend_view(request):
	uprof = UserProfile.objects.get(user=request.user)
	catalog = uprof.catalog.all()
	if request.method == 'POST':
		item = request.POST.get('item')
		price = request.POST.get('price')
		num = Item.objects.all().count()
		id = num+1
		newitem = Item(id=id,name=item,price=price)
		newitem.save()
		uprof.catalog.add(newitem)
	template = get_template('vendvi.html')
	variables = RequestContext(request,{
		'catalog':catalog
	})
	return render_to_response('vendvi.html', variables)
	
def vendor_search(request):
	results = []
	if request.method == 'POST':
		query = request.POST.get('query')
		if query == "":
			results = UserProfile.objects.filter(seller=True).order_by('business')
		else:
			querywords = query.split()
			for word in querywords:
				qresults = UserProfile.objects.filter(business__icontains=word,seller=True).order_by('business')
				collect = [term for term in qresults if term not in results]
				results.extend(collect)
	variables = RequestContext(request,{
		'vendors':results
	})
	return render_to_response('vendsearch.html',variables)
				
def itemlist(request,vendorname):
	uprof = UserProfile.objects.get(business=vendorname)
	items = uprof.catalog.all()
	for item in items:
		item.key = item.id
	variables = RequestContext(request,{
		'catalog':items
	})
	return render_to_response('buyvi.html', variables)
	
def register_page(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			user = User.objects.create_user(
			username=form.cleaned_data['username'],
			password=form.cleaned_data['password1'],
			email=form.cleaned_data['email']
			)
			name = form.cleaned_data['Name']
			biz, vend = False, False
			if form.cleaned_data['radio_buttons'] == 'option_one':
				biz = True
			if form.cleaned_data['radio_buttons'] == 'option_two':
				vend = True
			up = UserProfile(user=user,business=name,buyer=biz,seller=vend)
			up.save()
			return HttpResponseRedirect('/')
	else:
		form = RegistrationForm()
	variables = RequestContext(request, {
			'form': form
		})
	template = get_template('registration/register.html')
	output = template.render(variables)
	return HttpResponse(output)