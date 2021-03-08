#!/usr/bin/env python3
import sys
import argparse

parser = argparse.ArgumentParser(description='RDFize HomoloGene')
parser.add_argument('homologene', help='HomoloGene data file')
parser.add_argument('-p', '--protein', action='store_true', help='to NCBI protein accession')
args = parser.parse_args()

print("@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .")
# print("@prefix homologene: <https://ncbi.nlm.nih.gov/homologene/> .")
print("@prefix homologene: <http://identifiers.org/homologene/> .")
if args.protein:
    print("@prefix ncbiprotein: <http://identifiers.org/ncbiprotein/> .")
else:
    print("@prefix ncbigene: <http://identifiers.org/ncbigene/> .")
print()

fp = open(args.homologene, 'r')
prev_grp_id = ""
genes = []
for line in fp:
    fields = line.strip().split('\t')
    if len(fields) != 6:
        print("err", file=sys.stderr, flush=True)
        continue
    grp_id, tax_id, gene_id, symbol, gi, refseq = fields
    if args.protein:
        print(f'homologene:{grp_id} rdfs:seeAlso ncbiprotein:{refseq} .')
    else:
        print(f'homologene:{grp_id} rdfs:seeAlso ncbigene:{gene_id} .')
