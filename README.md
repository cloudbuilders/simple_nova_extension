Overview
========
This is a simple nova extension to demonstrate how to write extensions for
nova.  The files included in this repo are designed to be 'dropped' into nova
and python-novaclient.

Installing Server Component
===========================
This is designed as a minimal base for a "core extension," meaning it is
designed to be run from the nova source tree.  To use it:

    # First, clone and run devstack
    git clone https://github.com/openstack-dev/devstack.git
    cd devstack
    ./stack.sh

    cd /opt/stack/
    git clone git@github.com:cloudbuilders/simple_nova_extension.git
    cp simple_nova_extension/nova/nova/api/openstack/compute/contrib/cats.py nova/nova/api/openstack/compute/contrib/cats.py
    cp simple_nova_extension/nova/nova/tests/api/openstack/compute/contrib/test_cats.py nova/nova/tests/api/openstack/compute/contrib/test_cats.py

    # Then, restart your nova-api process!

Installing Client Component
===========================
python-novaclient has no direct extension mechanism, but it
is easy to modify.  To add cat support to python-novaclient,
first, copy the client code to python-novaclient

    cp simple_nova_extension/python-novaclient/novaclient/v1_1/cats.py python-novaclient/novaclient/v1_1/cats.py

Now, we will add api client support by modifying python-novaclient/novaclient/v1_1/client.py:

    --- a/novaclient/v1_1/client.py
    +++ b/novaclient/v1_1/client.py
    @@ -1,4 +1,5 @@
     from novaclient import client
    +from novaclient.v1_1 import cats
     from novaclient.v1_1 import certs
     from novaclient.v1_1 import aggregates
     from novaclient.v1_1 import flavors
    @@ -54,6 +55,7 @@ class Client(object):
             # extensions
             self.dns_domains = floating_ip_dns.FloatingIPDNSDomainManager(self)
             self.dns_entries = floating_ip_dns.FloatingIPDNSEntryManager(self)
    +        self.cats = cats.CatManager(self)
             self.certs = certs.CertificateManager(self)
             self.floating_ips = floating_ips.FloatingIPManager(self)
             self.floating_ip_pools = floating_ip_pools.FloatingIPPoolManager(self)

This diff is approximate, and only intended as a hint!

Finally, add cli support by adding this to python-novaclient/novaclient/v1_1/shell.py

    --- a/novaclient/v1_1/shell.py
    +++ b/novaclient/v1_1/shell.py
    @@ -1640,3 +1640,12 @@ def do_ssh(cs, args):
             print "ERROR: No %s %s address found." % (address_type,
                                                       pretty_version)
             return
    +
    +
    +def do_cat_list(cs, args):
    +    """Print a list of available 'flavors' (sizes of servers)."""
    +    cats = cs.cats.list()
    +    utils.print_list(cats, [
    +        'ID',
    +        'THUMB',
    +        'URL'])

This diff is approximate, and only intended as a hint!

Now, you should be able to see some cats!

    nova cat-list
