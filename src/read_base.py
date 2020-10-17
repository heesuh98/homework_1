from Bio.Seq import Seq

#seq = 0.59.fasta
exon_seq = Seq(seq)

count_a = exon_seq.count("A")
count_t = exon_seq.count("T")
count_c = exon_seq.count("C")
count_g = exon_seq.count("G")

print(count_a)
print(count_t)
print(count_c)
print(count_g)

