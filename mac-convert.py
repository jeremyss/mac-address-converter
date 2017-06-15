#!/usr/bin/python
import netaddr
import argparse

_author__ = "Jeremy Scholz"

parser = argparse.ArgumentParser(description='Convert MAC Address to specified format')
parser.add_argument('-v', action='store_true', help='Output results to terminal')
parser.add_argument('-f', type=str, metavar='[Input-File]', help='Input file')
parser.add_argument('-o', type=str, metavar='[Output-File]', help='Output file')
parser.add_argument('-c', action='store_true', help='Cisco MAC Output')
parser.add_argument('-j', action='store_true', help='Juniper MAC Output')
args = parser.parse_args()

if not (args.f and args.o and (args.c or args.j)):
    parser.print_usage()
    exit(1)
infile = args.f
outfile = args.o

try:
    filein = open(infile, 'r')
except IOError:
    print("File " + infile + " not found")
    exit(0)
fileout = open(outfile, 'w')

for line in filein:
    mac = netaddr.EUI(line)
    if args.c:
        mac.dialect = netaddr.mac_cisco
    elif args.j:
        mac.dialect = netaddr.mac_unix_expanded
    if args.v:
        print mac
    fileout.write("%s\n" % str(mac))
filein.close()
fileout.close()
