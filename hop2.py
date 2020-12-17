#!/usr/bin/env python3
import sys
import argparse

parser = argparse.ArgumentParser(description='RDFize hOP')
parser.add_argument('data', help='hOP data directory')
args = parser.parse_args()

print("@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .")
print("@prefix dct: <http://purl.org/dc/terms/> .")
print("@prefix ncbigene: <http://identifiers.org/ncbigene/> .")
print("@prefix ncbiprotein: <http://identifiers.org/ncbiprotein/> .")
print("@prefix homologene: <https://ncbi.nlm.nih.gov/homologene/> .")
print("@prefix taxid: <http://identifiers.org/taxonomy/> .")
print("@prefix orth: <http://purl.org/net/orth#> .")
print()
print('<https://orth.dbcls.jp/data/hop/>')
print('    a orth:OrthologyDataset ;')
print('    dct:title "HomoloGene" .')
print()

def print_profile(group_no, label, prifoke, member):
    print(f'group:{group_no} a orth:OrthologsCluster ;')
    print(f'    orth:inDataset <https://orth.dbcls.jp/data/hop/> ;')

fp = open(args.data + '/profile', 'r')
for line in fp:
    fields = line.strip().split('\t')
    # print(fields)
    print_profile(group_no, label, prifoke, member)
