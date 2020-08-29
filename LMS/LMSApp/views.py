from django.shortcuts import render
from . models import Education, CProgram, JAVA, Networking, DS, CloudComputing, OS, Python, EthicalHack
# Create your views here.
def index(request):
    #details of the course using object
    all_edu = Education.objects.all()
    return render(request,'index.html',{'all_edu':all_edu})

def c(request):
    #details for c
    c_contents = CProgram.objects.all()
    return render(request, 'c.html', {'c_contents':c_contents})

def java(request):
    #details for java
    java_contents = JAVA.objects.all()
    return render(request, 'java.html', {'java_contents': java_contents})

def network(request):
    #details for java
    net_contents = Networking.objects.all()
    return render(request, 'network.html', {'net_contents': net_contents})

def ds(request):
    #details for java
    ds_contents = DS.objects.all()
    return render(request, 'ds.html', {'ds_contents': ds_contents})

def cloud(request):
    #details for java
    cloud_contents = CloudComputing.objects.all()
    return render(request, 'cloud.html', {'cloud_contents': cloud_contents})

def os(request):
    #details for java
    os_contents = OS.objects.all()
    return render(request, 'os.html', {'os_contents': os_contents})

def python(request):
    #details for java
    py_contents = Python.objects.all()
    return render(request, 'python.html', {'py_contents': py_contents})

def ethical(request):
    #details for java
    eth_contents = EthicalHack.objects.all()
    return render(request, 'ethical.html', {'eth_contents': eth_contents})
