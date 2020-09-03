#!/usr/bin/env python3
import sys
import argparse

parser = argparse.ArgumentParser(description='RDFize HomoloGene')
parser.add_argument('homologene', help='HomoloGene data file')
args = parser.parse_args()

print("@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .")
print("@prefix ncbigene: <http://identifiers.org/ncbigene/> .")
print("@prefix ncbiprotein: <http://identifiers.org/ncbiprotein/> .")
print("@prefix taxid: <http://identifiers.org/taxonomy/> .")
print("@prefix orth: <http://purl.org/net/orth#> .")
print("@prefix group: <http://purl.org/orthordf/homologene/group/> .")
print()

fp = open(args.homologene, 'r')
for line in fp:
    fields = line.strip().split('\t')
    if len(fields) != 6:
        print("err", file=sys.stderr, flush=True)
        continue
    grp_id, tax_id, gene_id, symbol, gi, refseq = fields
    print(f'group:{grp_id} a orth:OrthologsCluster ;')
    print(f'    orth:hasHomologous ncbigene:{gene_id} .')
    print(f'ncbigene:{gene_id} a orth:Gene ;')
    print(f'    rdfs:label "{symbol}" ;')
    print(f'    orth:taxon taxid:{tax_id} ;')
    print(f'    orth:protein ncbiprotein:{refseq} .')
    print()
