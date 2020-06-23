#!/usr/bin/env python

import pytest
from getpass import getpass
from netmiko import ConnectHandler
from pyeapi.client import Node
import pyeapi


password = getpass("Type password for api user in Arista: ")


@pytest.fixture(scope="module")
def netmiko_conn(request):
    net_connect = ConnectHandler(
        host="0.0.0.0",
        device_type="arista_eos",
        username="api",
        password=password,
        port=2002,
    )

    def fin():
        net_connect.disconnect()

    request.addfinalizer(fin)
    return net_connect

@pytest.fixture(scope="module")
def eapi_conn(request):
    connection = pyeapi.connect(
        transport="https",
        host="0.0.0.0",
        username="api",
        password=password,
        port=9002,
    )
    node = Node(connection)
    return node
