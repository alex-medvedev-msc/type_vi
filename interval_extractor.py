import pandas as pd
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet import generic_protein
from subprocess import Popen, PIPE
from threading  import Thread
from queue import Queue, Empty
import os
from gene_extractor import get_features
from collections import deque


class Hit(object):
    def __init__(self, query, target, e):
        self.query = query
        self.target = target
        self.e = e


def enqueue_output(out, queue):
    for line in iter(out.readline, b''):
        queue.put(line)
    out.close()


def make_query(table_path, genes, out):
    table = pd.read_csv(table_path)
    records = []
    for _, row in table.iterrows():
        if row.gene in genes:
            record = SeqRecord(Seq(row.translation, alphabet=generic_protein), id=row.gene)
            records.append(record)
    SeqIO.write(records, out, "fasta")


def blast(query, target):
    args = ["blastp", "-subject", target, "-query", query, "-evalue", "1e-5",
            "-outfmt", "10 qseqid sseqid evalue", "-num_threads", "4"]
    p = Popen(args, stdout=PIPE, bufsize=1)
    q = Queue()
    t = Thread(target=enqueue_output, args=(p.stdout, q))
    t.daemon = True # thread dies with the program
    t.start()
    hits = []

    while p.poll() == None:
        try:
            line = q.get_nowait() # or q.get(timeout=.1)
        except Empty:
            pass
            #print('no output yet')
        else:
            #print(type(line))
            row = line.decode('utf-8').split(",")
            hits.append(Hit(row[0], row[1], float(row[2])))
    return hits


def genome_to_fasta(path, out_path):
    records = SeqIO.parse(path, "genbank")
    SeqIO.write(records, out_path, "fasta")


class Gene(object):
    def __init__(self, name, strand, start, end, contig):
        self.name = name
        self.strand = strand
        self.start = start
        self.end = end
        self.contig = contig


def parse_genbank_genome(path):
    genes = {}
    features = get_features(path)
    for feature in features:
        if "locus_tag" not in feature.qualifiers:
            continue
        name = feature.qualifiers["locus_tag"][0]
        genes[name] = Gene(name, feature.strand, int(feature.location.start), int(feature.location.end), feature.contig)
    return genes


def update_hits_with_location(hits, file):
    genes = parse_genbank_genome(file)
    for hit in hits:
        hit.gene = genes[hit.target]


def extract_intervals(hits, genes, min_number=9, size=10000):
    contigs = {}
    for hit in hits:
        if hit.gene.contig in contigs:
            contigs[hit.gene.contig].append(hit)
        else:
            contigs[hit.gene.contig] = [hit]
    for c in contigs:
        contigs[c].sort(key=lambda h: h.gene.start)
    window = deque()
    hits.sort(key=lambda h: h.feature.location.start)
    operons = []
    for hit in hits:
        window.append(hit)
        new_window = deque()
        for added_hit in window:
            if hit.feature.location.end - added_hit.feature.location.start <= size:
                new_window.append(added_hit)
        window = new_window
        query_ids = set([])

    return operons



def interval_to_vector(interval):
    pass


def add_vector_to_matrix(vector, matrix):
    pass


def write_matrix(matrix):
    pass


def get_fasta_path(path):
    return ".".join(path.split(".")[:-1])+".fasta"


def main():
    table_path = ""
    genes = []
    query = ""
    make_query(table_path, genes, query)
    genomes_dir = ""
    matrix = []
    for filename in os.listdir(genomes_dir):
        file = os.path.join(genomes_dir, filename)
        fasta_file = get_fasta_path(file)
        genome_to_fasta(file, fasta_file)
        hits = blast(query, fasta_file)
        update_hits_with_location(hits, file)
        intervals = extract_intervals(hits, genes)
        for interval in intervals:
            vector = interval_to_vector(interval)
            add_vector_to_matrix(vector, matrix)
    write_matrix(matrix)


if __name__ == '__main__':
    main()
