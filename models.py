from django.db import models
from django.urls import reverse
from netfields import InetAddressField, NetManager

class Vlan(models.Model):
    vlan_id = models.IntegerField(default = 0)
    vlan_name = models.CharField(max_length=32)
    vlan_desc = models.CharField(max_length=200)

    def __str__(self):
        return self.vlan_name
    def get_absolute_url(self):
        """Returns the url to access a detail record for this vlan."""
        return reverse('ipam:vlan-detail', kwargs={'pk': self.id })

class Subnet(models.Model):
    subnet_name = models.CharField(max_length=32)
    subnet_desc = models.CharField(max_length=200)
    addr = InetAddressField()
    objects = NetManager()
    vlan = models.ForeignKey(Vlan, on_delete=models.CASCADE) #relacionamento

    class Meta:
        ordering = ['id']
    
    def __str__(self):
        return self.subnet_name 

    def get_absolute_url(self): ##adicionado url return
        """Returns the url to access a detail record for this subnet."""
        return reverse('ipam:subnet-detail', kwargs={'pk': self.id })
