from ipam.models import Vlan, Subnet

v801 = Vlan.objects.get(vlan_id=801)
#print(v801.vlan_desc)
sub801 = v801.subnet_set.all()
#print(sub801)

print("Subnets:")
for s in sub801:
    print(str(s.addr) + '     '+'Vlan: ' + str(s.vlan.vlan_id))  