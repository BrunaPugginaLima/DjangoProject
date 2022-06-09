from django.views import generic
from django.http import HttpResponse
from ipam.models import Vlan
from ipam.models import Subnet ####adicionado
from django.urls import reverse_lazy

def index(request): 
    return HttpResponse("Hello World")

#VLANS

class VlanList(generic.ListView):
    model = Vlan
    context_object_name = 'vlans'

class VlanCreate(generic.CreateView):
    model = Vlan
    fields = '__all__'

class VlanDetail(generic.DetailView):
    model = Vlan
    context_object_name = 'vlan'

class VlanUpdate(generic.UpdateView):
    model = Vlan
    fields = ['vlan_id', 'vlan_name', 'vlan_desc']
    template_name_suffix = '_update_form'

class VlanDelete(generic.DeleteView):
    model = Vlan
    success_url = reverse_lazy('ipam:vlan-list')

def vlan_detail(request, vlan_id):
    return HttpResponse("Detalhes da Vlan : " + str(vlan_id))

#SUBNETS   

class SubnetList(generic.ListView):
    model = Subnet
    context_object_name = 'subnets'

class SubnetCreate(generic.CreateView):
    model = Subnet
    fields = '__all__'

class SubnetDetail(generic.DetailView):
    model = Subnet
    context_object_name = 'subnet'

class SubnetUpdate(generic.UpdateView):
    model = Subnet
    fields = ['subnet_name', 'subnet_desc', 'addr', 'vlan'] 
    template_name_suffix = '_update_form' 

class SubnetDelete(generic.DeleteView):
    model = Subnet
    success_url = reverse_lazy('ipam:subnet-list')

def subnet_detail(request, subnet_name): 
    return HttpResponse("Detalhes da Subnet : " + str(subnet_name))