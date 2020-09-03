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

gene_info = {}

def print_gene_info(gene_id):
    symbol, taxid, refseq = gene_info[gene_id]
    
    print(f'ncbigene:{gene_id} a orth:Gene ;')
    print(f'    rdfs:label "{symbol}" ;')
    print(f'    orth:taxon taxid:{tax_id} ;')
    print(f'    orth:protein ncbiprotein:{refseq} .')
    print()

def print_genes(genes):
    n = len(genes)
    for i in range(n-1):
        print(f'    orth:hasHomologous ncbigene:{genes[i]} ;')
    print(f'    orth:hasHomologous ncbigene:{genes[n-1]} .')
    print()
    for gene in genes:
        print_gene_info(gene)

fp = open(args.homologene, 'r')
genes = []
prev_grp_id = ""
for line in fp:
    fields = line.strip().split('\t')
    if len(fields) != 6:
        print("err", file=sys.stderr, flush=True)
        continue
    grp_id, tax_id, gene_id, symbol, gi, refseq = fields
    gene_info[gene_id] = (symbol, tax_id, refseq);
    genes.append(gene_id)
    if prev_grp_id == grp_id:
        continue
    if prev_grp_id != "" and len(genes) != 0:
        print_genes(genes)
    prev_grp_id = grp_id
    print(f'group:{grp_id} a orth:OrthologsCluster ;')
    genes = [gene_id]
    
print_genes(genes)
