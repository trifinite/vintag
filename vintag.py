#!/usr/bin/env python3

"""
VINTAG - wrapper fot the Tesla VIN Identifier API on rapidAPI
"""

__author__ = "Martin Herfurt (trifinite.org)"
__version__ = "0.1.1"
__license__ = "MIT"

import argparse
import http.client
# Please get your own API key at rapidapi.com
# https://rapidapi.com/trifinite/api/tesla-vin-identifier/

def main(args):
    conn = http.client.HTTPSConnection("tesla-vin-identifier.p.rapidapi.com")

    headers = {
        'X-RapidAPI-Host': "tesla-vin-identifier.p.rapidapi.com",
        'X-RapidAPI-Key': "1e12496bb8mshdc0de8feddd35fdp1951efjsna070c95275f5"
        }

    conn.request("GET", "/s3xy/"+args.identifier, headers=headers)
    res = conn.getresponse()
    data = res.read()
    print("Model Type: " + data.decode("utf-8"))

    conn.request("GET", "/location/"+args.identifier, headers=headers)
    res = conn.getresponse()
    data = res.read()
    print("Manufacturing Location: " + data.decode("utf-8"))

    conn.request("GET", "/year/"+args.identifier, headers=headers)
    res = conn.getresponse()
    data = res.read()
    print("Manufacturing Year: "+ data.decode("utf-8"))

    conn.request("GET", "/vin/"+args.identifier, headers=headers)
    res = conn.getresponse()
    data = res.read()
    print("VIN: "+data.decode("utf-8"))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    # Required positional argument
    parser.add_argument("identifier", help="VIN Identifier 8 hex-encoded bytes (e.g. 0f7885c2af1a6ef9)")

    # Specify output of "--version"
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s (version {version})".format(version=__version__))

    args = parser.parse_args()
    main(args)