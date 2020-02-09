from django.shortcuts import render
from django.http import HttpResponse
import nmap
# Create your views here.

def home(request):
	return render(request, 'home.html')


def scanip(request):
	
	nmScan = nmap.PortScanner()


	ip_adr = request.POST['ipadr']
	#nmScan.scan(ip_adr)
	#hosts,states = [],[]
	#for h in nmScan.all_hosts():
	#	hosts.append(nmScan[h].hostname())
	#	states.append(nmScan[h].state())

		#for proto in nmScan[h].all_protocols():
			#lport = nmScan[host][proto].keys()

	return render(request, 'result.html', {'IPAddress':ip_adr})


