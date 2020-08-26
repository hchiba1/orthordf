#!/usr/bin/env python3
import sys
import argparse

parser = argparse.ArgumentParser(description='RDFize HomoloGene')
parser.add_argument('homologene', help='HomoloGene data file')
args = parser.parse_args()

print("@prefix")
print("@prefix")
print()

fp = open(args.homologene, 'r')
for line in fp:
    fields = line.strip().split('\t')
    if len(fields) != 6:
        print("err", file=sys.stderr, flush=True)
        continue
    grp, taxid, geneid, symbol, protid, refseqid = fields
    print(f'grp:grp')
