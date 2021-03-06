# Copyright 2011 OpenStack LLC.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""
Cats interface (1.1 extension).
"""

from novaclient import base


class Cat(base.Resource):
    """
    A cat is a furry creature with 4 legs and whiskers.
    """
    pass


class CatManager(base.ManagerWithFind):
    resource_class = Cat

    def list(self):
        """
        Get a list of cats.
        """
        return self._list('/os-cats', 'cats')
