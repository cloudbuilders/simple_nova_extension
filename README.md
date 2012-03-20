Overview
========
This is a simple nova extension to demonstrate how to write extensions for
nova.

Installing
==========
This is designed as a minimal base for a "core extension," meaning it is
designed to be run from the nova source tree.  To use it:

    # First, clone and run devstack
    git clone https://github.com/openstack-dev/devstack.git
    cd devstack
    ./stack.sh

    cd /opt/stack/
    git clone git@github.com:cloudbuilders/simple_nova_extension.git
    cp simple_nova_extension/nova/api/openstack/compute/contrib/cats.py nova/api/openstack/compute/contrib/cats.py
    cp simple_nova_extension/nova/tests/api/openstack/compute/contrib/test_cats.py nova/tests/api/openstack/compute/contrib/test_cats.py


    # Then, restart your nova-api process!
