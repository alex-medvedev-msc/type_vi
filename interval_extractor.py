import pandas as pd
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet import generic_protein
from subprocess import Popen, PIPE
from threading  import Thread
from queue import Queue, Empty
import os


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


def extract_intervals(hits, genes, size = 10000):
    found = set()
    needed = set(genes)
    hits.sort(key=lambda x:x.)
    for hit in hits:
        found.add(hit.target)

    if found == needed:
        return


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
        intervals = extract_intervals(hits, genes)
        for interval in intervals:
            vector = interval_to_vector(interval)
            add_vector_to_matrix(vector, matrix)
    write_matrix(matrix)


if __name__ == '__main__':
    main()
