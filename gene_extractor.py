import pandas as pd
import os
from Bio import SeqIO


def get_features(filename):
    features = []
    for record in SeqIO.parse(filename, "genbank"):
        for feature in record.features:
            if feature.type == 'CDS':
                feature.contig = record.name
                features.append(feature)
    return features


def update_genes(genes, features, org, query):
    s = set(query.keys())
    for feature in features:
        gene = feature.qualifiers["locus_tag"]
        if gene in s:
            genes["gene"].append(gene)
            genes["strand"].append(feature.strand)
            genes["start"].append(int(feature.location.start))
            genes["end"].append(int(feature.location.end))
            genes["contig"].append(feature.contig)
            genes["kegg_id"].append(query[s])
            genes["org_id"].append(org)
            genes["name"].append(feature.qualifiers["product"])
            genes["translation"].append(feature.qualifiers["translation"][0])


def get_codes(gen_type, file_name):
    d = {}
    tab1 = pd.read_csv(file_name, ",")
    filtered = tab1[tab1.TYPE == gen_type]

    for i, row in filtered.iterrows():
        a, b = row.PROTEIN, row.GENE.split(" ")
        for j in b:
            d[j] = a
    return d


def main():
    genomes_dir = ""
    organisms_table = "type_vi_organisms.csv"
    organisms = pd.read_csv(organisms_table)
    names = {u.split("/")[-1]: t for u, t in zip(organisms.ncbi, organisms.organism)}
    genes = {"gene": [], "strand": [], "start": [], "end": [], "contig": [], "kegg_id": [], "org_id": [], "name": [],
             "translation": []}
    for filename in os.listdir(genomes_dir):
        file = os.path.join(genomes_dir, filename)
        for name in names:
            if name in file:
                org = names[name]
                break
        query = get_codes(org.toupper(), "codes.csv")
        features = get_features(file)
        update_genes(genes, features, org, query)

    result = pd.DataFrame.from_dict(genes)
    result.to_csv("genes.csv")


if __name__ == '__main__':
    main()
