# Copyright 2011 Eldar Nugaev
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

import json

import webob

from nova import compute
from nova import exception
from nova import test
from nova.tests.api.openstack import fakes


def fake_get_instance(self, context, instance_uuid):
    return {'uuid': instance_uuid}


class CatsExtensionTest(test.TestCase):

    def setUp(self):
        super(CatsExtensionTest, self).setUp()
        self.stubs.Set(compute.API, 'get', fake_get_instance)

    def test_index(self):
        req = webob.Request.blank('/v2/fake/os-cats')
        req.method = "GET"
        req.headers["content-type"] = "application/json"

        res = req.get_response(fakes.wsgi_app())
        output = json.loads(res.body)
        self.assertEqual(res.status_int, 200)

    def test_show(self):
        req = webob.Request.blank('/v2/fake/os-cats/1')
        req.method = "GET"
        req.headers["content-type"] = "application/json"

        res = req.get_response(fakes.wsgi_app())
        output = json.loads(res.body)
        self.assertEqual(res.status_int, 501)
