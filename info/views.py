from django.shortcuts import render
import json, urllib, urllib2, requests
import sys
# Create your views here.

def ll(request):
	return render(request, 'info/ll.html')

def add(request):
	return render(request, 'info/add.html')

def mp(request):
	return render(request, 'info/mp.html')

def sgl(request):
	return render(request, 'info/sgl.html')

def gl(request):
	params={}
	params['address'] = request.GET['address']
	params['key'] = 'AIzaSyC4N_gMQj94cG7Wp_dr6QUlQ4dSxR5paXc'
	address = urllib.urlencode(params)
	url = 'https://maps.googleapis.com/maps/api/geocode/json' + '?' + address
	try: urllib2.urlopen(url)
	except URLError as e:
		print e.reason
	data = urllib2.urlopen(url)
	d = json.load(data)
	print d
	lat = d['results'][0]['geometry']['location']['lat']
	print lat
	lng = d['results'][0]['geometry']['location']['lng']
	print lng
	return render(request, 'info/sgl.html', {'lat': lat, 'lng' : lng })


def sga(request):
	return render(request, 'info/sga.html')

def ga(request):
	params={}
	params['latlng'] = request.GET['latlng']
	params['key'] = 'AIzaSyC4N_gMQj94cG7Wp_dr6QUlQ4dSxR5paXc'
	latlng = urllib.urlencode(params)
	url = 'https://maps.googleapis.com/maps/api/geocode/json' + '?' + latlng
	try: urllib2.urlopen(url)
	except URLError as e:
		print e.reason
	data = urllib2.urlopen(url)
	d = json.load(data)
	print d
	address = d['results'][0]['formatted_address']
	print address
	return render(request, 'info/sga.html', {'address': address})