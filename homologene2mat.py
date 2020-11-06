#!/usr/bin/env python3

import sys
import argparse

parser = argparse.ArgumentParser(description='RDFize HomoloGene')
parser.add_argument('homologene', help='HomoloGene data file')
args = parser.parse_args()

def print_group(grp_id, genes, taxids):
    if not grp_id:
        return
    print(grp_id, taxids)

fp = open(args.homologene, 'r')
prev_grp_id = ""
genes = []
taxids = []
taxid_dict = {}
gene_info = {}
grp_info = {}

for line in fp:
    fields = line.strip().split('\t')
    if len(fields) != 6:
        print("err", file=sys.stderr, flush=True)
        continue
    grp_id, tax_id, gene_id, symbol, gi, refseq = fields
    taxid_dict[tax_id] = True
    gene_info[gene_id] = (symbol, tax_id, refseq);
    if prev_grp_id != grp_id:
        # print_group(prev_grp_id, genes, taxids)
        if prev_grp_id:
            grp_info[prev_grp_id] = taxids
        prev_grp_id = grp_id
        genes = []
        taxids = []
    genes.append(gene_id)
    taxids.append(tax_id)
    # grp_info[grp_id] = taxids

# print_group(prev_grp_id, genes, taxids)
grp_info[prev_grp_id] = taxids


print("grp_id\t", "\t".join(list(taxid_dict.keys())))
# for taxid in taxid_dict:
    
def print_profile(grp_id, taxids):
    print(grp_id, taxids)

for grp in grp_info:
    # print(grp, grp_info[grp])
    print_profile(grp, grp_info[grp])
