#!/usr/bin/env python
"""
Use Arista eAPI

example for BGP (keep in mind that this is a cEOS - docker instancce):
    $ python eos.py -u api -p bgp -P 9002 -i 0.0.0.0 -H r02
"""

from pyeapi.client import Node
import pyeapi

# import re
# import sys
import argparse
from getpass import getpass

__author__ = "Tomas Morales"
__version__ = "0.0.1"


class Arista:
    def response(self, value, message=None):
        if message:
            print("%s: %s" % (value, message))
        else:
            print(value)
        # sys.exit(value)

    def bgp_status(self, node, hostname):
        """
        Use Arista eAPI to check if BGP neighbors are established.
        """
        exit_code = "OK"
        bgp_message = "BGP status of Neighbors in %s:" % hostname

        show_bgp = node.enable("show ip bgp summary")
        list_bgp = show_bgp[0]["result"]["vrfs"]["default"]["peers"]

        for key, value in list_bgp.items():
            if not value["peerState"] == "Established":
                exit_code = "CRITICAL"
                bgp_message = bgp_message + " Neighbor " + key + " is not ESTABLISHED."

        self.response(exit_code, bgp_message)


"""
    def ospf_status(self, node, hostname, num_neighbors=0):
        exit_code = "OK"
        ospf_message = "OSPF status of Neighbors in %s is correct." % hostname
        show_ospf = node.enable('show ip ospf neighbor')
"""


def parse_args():
    parser = argparse.ArgumentParser(description="Arista Testing")
    parser.add_argument("-p", "--protocol", help="Protocol to verify")
    parser.add_argument("-P", "--port", help="Port for connection eAPI")
    parser.add_argument("-i", "--ip", help="Device IP address")
    parser.add_argument("-u", "--username", help="Username in device")
    parser.add_argument("-H", "--hostname")
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version="%(prog)s (version {})".format(__version__),
    )

    # if len(sys.argv) <= 1:
    #    sys.argv.append('--help')

    args = parser.parse_args()
    return args


def main():
    """
    Check if BGP/OSPF neighbors for an Arista device are ESTABLISHED/FULL. Anything else is CRITICAL
    """
    # print("STARTING TIME " + str(datetime.datetime.now()) + "\n")
    args = parse_args()

    my_password = getpass("Password for user allowed to connect to eAPI: ")

    check_arista = Arista()

    connection = pyeapi.connect(
        transport="https",
        host=args.ip,
        username=args.username,
        password=my_password,
        port=args.port,
    )
    node = Node(connection)

    if args.protocol == "bgp":
        check_arista.bgp_status(node, args.hostname)
    elif args.protocol == "ospf":
        check_arista.ospf_status(node, args.hostname, 0)
    else:
        print("CRITICAL - Command not supported or wrong")


if __name__ == "__main__":
    main()
