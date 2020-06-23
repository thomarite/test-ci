#!/usr/bin/env python

import pytest
from netmiko import ConnectHandler
from pyeapi.client import Node
import pyeapi
from jsonrpclib import Server
import jsonrpclib
import ssl


ssl._create_default_https_context = ssl._create_unverified_context


@pytest.fixture(scope="module")
def netmiko_conn(request):
    net_connect = ConnectHandler(
        host="0.0.0.0",
        device_type="arista_eos",
        username="api",
        password="api123",
        port=2002,
    )

    def fin():
        net_connect.disconnect()

    request.addfinalizer(fin)
    return net_connect


@pytest.fixture(scope="module")
def eapi_conn(request):
    connection = pyeapi.connect(
        transport="https", host="0.0.0.0", username="api", password="api123", port=9002,
    )
    node = Node(connection)
    return node


@pytest.fixture(scope="module")
def json_conn(request):
    node = Server("https://api:api123@0.0.0.0:9002/command-api")
    return node
