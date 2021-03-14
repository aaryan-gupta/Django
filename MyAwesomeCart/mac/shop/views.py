from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product, Contact, Orders, OrderUpdate
from math import ceil
from django.views.decorators.csrf import csrf_exempt
from PayTm import Checksum
import json

MERCHANT_KEY = 'kbzk1DSbJiV_O3p5';

# Create your views here.

def index(request):
	allProds = []
	catProds = Product.objects.values("category", "id")
	cats = {item["category"] for item in catProds}
	for cat in cats:
		prod = Product.objects.filter(category=cat)
		n = len(prod)
		nSlides = n//4 + ceil((n/4) - (n//4))
		allProds.append([prod, range(1, nSlides), nSlides])
	params = {"allProds" : allProds}
	return render(request, "shop/index.html", params)

def about(request):
	return render(request, "shop/about.html")

def contact(request):
	thank = False
	if request.method == "POST":
		name = request.POST.get("name", "")
		email = request.POST.get("email", "")
		phone = request.POST.get("phone", "")
		desc = request.POST.get("desc", "")
		contact = Contact(name=name, email=email, phone=phone, desc=desc)
		contact.save()
		thank = True
		# return redirect("/shop")
	return render(request, "shop/contact.html", {"thank": thank})

def tracker(request):
	if request.method == "POST":
		orderId = request.POST.get("orderId", "")
		email = request.POST.get("email", "")
		print(orderId, email)
		try:
			order = Orders.objects.filter(order_id=orderId, email=email)
			if len(order) > 0:
				update = OrderUpdate.objects.filter(order_id=orderId)
				updates = []
				for item in update:
					updates.append({"text": item.update_desc, "time": item.timestamp})
					response = json.dumps([updates, order[0].items_json], default=str)
				return HttpResponse(response)
			else:
				# return HttpResponse("error")
				return HttpResponse("{}")
		except Exception as e:
			# return HttpResponse(f"exception {e}")
			return HttpResponse("{}")
	return render(request, "shop/tracker.html")

def search(request):
	return render(request, "shop/search.html")

""" def productView(request):
	return render(request, "shop/prodView.html") """

def productView(request, myid):
	# FETCH THE PRODUCT USING THE ID
	product = Product.objects.filter(id=myid)
	return render(request, "shop/prodView.html", {"product": product[0]})

def checkout(request):
	if request.method == "POST":
		items_json = request.POST.get("itemsJson", "")
		name = request.POST.get("name", "")
		amount = request.POST.get("amount", "")
		email = request.POST.get("email", "")
		address = request.POST.get("address1", "") + " " + request.POST.get("address2", "")
		city = request.POST.get("city", "")
		state = request.POST.get("state", "")
		zip_code = request.POST.get("zip_code", "")
		phone = request.POST.get("phone", "")
		order = Orders(items_json=items_json, name=name, email=email, address=address, city=city, state=state, zip_code=zip_code, phone=phone, amount=amount)
		order.save()
		# return redirect("/shop")
		update = OrderUpdate(order_id=order.order_id, update_desc="The order has been placed")
		update.save()
		thank = True
		oid = order.order_id
		# return render(request, "shop/checkout.html", {"thank": thank, "id": oid})

		# REQUEST PAYTM TO TRANSFER THE AMOUNT TO YOUR ACCOUNT AFTER PAYMENT BY USER
		param_dict = {
            'MID':'WorldP64425807474247', # MERCHANT ID
            # 'ORDER_ID':'dddgfgfeeed',
            'ORDER_ID': str(order.order_id),
            'TXN_AMOUNT':'1',
            # 'CUST_ID':'acfff@paytm.com',
            'CUST_ID': email,
            'INDUSTRY_TYPE_ID':'Retail',
            # 'WEBSITE':'worldpressplg',
            'WEBSITE': 'WEBSTAGING',
            'CHANNEL_ID': 'WEB',
			# 'CALLBACK_URL':'http://localhost/pythonKit/response.cgi',
			'CALLBACK_URL':'http://127.0.0.1:8000/shop/handlerequest/',
        }
		param_dict["CHECKSUMHASH"] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
		return render(request, "shop/paytm.html", {"param_dict": param_dict})
	return render(request, "shop/checkout.html")

@csrf_exempt
def handlerequest(request):
	# PAYTM WILL SEND YOU POST REQUEST HERE
	form = request.POST
	response_dict = {}
	for i in form.keys():
		response_dict[i] = form[i]
		if i == "CHECKSUMHASH":
			checksum = form[i]
	verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
	if verify:
		if response_dict["RESPCODE"] == "01":
			print("ORDER SUCCESSFUL")
		else:
			print("ORDER WAS NOT SUCCESSFUL BECAUSE" + response_dict["RESPMSG"])
	# return HttpResponse("Done")
	return render(request, "shop/paymentStatus.html", {"response": response_dict})