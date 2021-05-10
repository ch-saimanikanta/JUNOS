#!/usr/bin/python

from jnpr.junos import Device
from lxml import etree
from pprint import pprint

if __name__=='__main__':
	with Device('66.129.235.10',port='49000',user='jcluser',passwd='Juniper!1') as dev:
		
		pprint(dev.facts['version'])
		
		config_json = dev.rpc.get_config( options={"format": "json"})
		pprint(config_json["configuration"]["system"]["host-name"])
		
		print("configured interfaces:")
		for interface in config_json["configuration"]["interfaces"]["interface"]:
			print(interface["name"])
		
		print("\nInterface operational status:")
		rpc_result = dev.rpc.get_interface_information()
		#etree.dump(rpc_result)
		interfaces = rpc_result.xpath("physical-interface")
		for interface in interfaces:
			print("Interface: {}, Status: {}".format(interface.findtext("name").strip(), interface.findtext("oper-status").strip()))
		
		#list_interfaces = dev.rpc.get_interface_information()
		#print(etree.tostring(list_interfaces))

