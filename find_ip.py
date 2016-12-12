from mistral.actions.openstack.actions import NeutronAction


class GetFreeIP(NeutronAction):
    def run(self):
        client = self._get_client()
    
        ips = client.list_floatingips()
    
        ips = [ip['floating_ip_address'] for ip in ips['floatingips'] if
               ip['port_id'] is None]

        if ips:
            return {'ip_address': ips[0]}

        else:
            raise Exception("No free IP")


