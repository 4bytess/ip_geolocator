#!/usr/bin/python3

import json, sys, signal, argparse
import requests as req

def ctrlc(sig, frame):
    print("\nExit...")
    sys.exit(1)

signal.signal(signal.SIGINT, ctrlc)

API_Key = ""

parser = argparse.ArgumentParser(
        description="ipgeolocation.io API geolocator",
        usage="ip_geolocator.py <ip_address> <api_key> (optional)"
        )

parser.add_argument("-i", "--ip", required=True, type=str, help="IP address to geolocate")
parser.add_argument("-k", "--key", required=False, type=str, help="API Key (optional)")

args = parser.parse_args()

ip_addr = args.ip

if (args.key):
    API_Key = args.key
else:
    API_Key = "9a668a0944bb46d68536972f2fbd38bd"

if (args.key is None and API_Key == ""):
    print("No API Key specified")
    sys.exit(1)

API_Route = "https://api.ipgeolocation.io/ipgeo?apiKey=%s&ip=%s" % (API_Key, ip_addr)

if __name__ == '__main__':

    print("Geolocating %s..." % ip_addr)

    r = req.get(API_Route)
    jsonData = json.loads(r.text)

    print("\nContinent: %s" % jsonData["continent_name"])
    print("Continent code: %s" % jsonData["continent_code"])
    print("Country: %s" % jsonData["country_name"])
    print("Country codes: %s, %s" % (jsonData["country_code2"],jsonData["country_code3"]))
    print("Country capital: %s" % jsonData["country_capital"])
    print("State_Prov: %s" % jsonData["state_prov"])
    print("State code: %s" % jsonData["state_code"])
    if jsonData["is_eu"]:
        print("Its in the EU")
    else:
        print("Is not in the EU")
    print("Languages: %s" % jsonData["languages"])
    print("Geoname ID: %s" % jsonData["geoname_id"])
    print("Calling code: %s" % jsonData["calling_code"])
    print("Country TLD: %s" % jsonData["country_tld"])
    print("ISP: %s" % jsonData["isp"])
