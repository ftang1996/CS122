import sys
import os
from os.path import join
import time
sys.path.insert(0, os.path.abspath("/Users/Fiona/Desktop/CS 122/projects/"))
from helpers import read_reads, read_reference, pretty_print_aligned_reads_with_ref


def hamming(s, t):
    """Finds hamming distance (i.e. number of char mismatches between two strings)"""
    dH = 0;
    if s == t:
        return dH;
    l = len(s);
    for i in range(0, l):
        if s[i] != t[i]:
            dH += 1;
    return dH;

def genome_hash(genome, k):
    """Build hash table of kmers from reference genome"""
    table = {}
    for i in range(len(genome)-k+1):
        kmer = genome[i:i+k]
        if kmer in table:
            table[kmer].append(i)
        else:
            table[kmer] = [i]
    return table

def read_align(read, k, ref_genome, genome_table):
    """Aligns a single read against a reference genome

    :param read: read sequence
    :param k: length of kmer used in genome table
    :param ref_genome: reference genome sequence
    :param genome_table: kmer table created for reference genome
    :return: position and mismatches for alignment with min mismatches
    """
    n_read = len(read)
    n_genome = len(ref_genome)
    kmers = {}

    # Divide read into segments
    for i in range(len(read)//k):
        kmer_read_pos = i*k;
        kmer = read[kmer_read_pos:kmer_read_pos+k]
        kmers[kmer] = kmer_read_pos

    # Find match with minimum mismatches
    min_mismatch = n_read + 1
    min_mismatch_pos = -1
    for kmer in kmers:
        if kmer in genome_table:
            positions = genome_table[kmer]
            for p in positions:
                left_end = p - kmers[kmer]
                right_end = p - kmers[kmer] + n_read
                if left_end >= 0 and right_end <= n_genome:
                    align_with = ref_genome[left_end:right_end]
                    # find alignment with min mismatches
                    mismatch = hamming(read, align_with)
                    if mismatch <= min_mismatch:
                        min_mismatch = mismatch
                        min_mismatch_pos = left_end
    return min_mismatch, min_mismatch_pos


def genome_align(paired_end_reads, ref, k, gap_min, gap_max):
    """
    Aligns paired-end reads of a donor genome against a reference genome

    :param paired_end_reads: list of paired-end reads with format [[left_read1, right_read1],
            [left_read2, right_read2], ...]
    :param ref: reference genome sequence
    :param k: size of kmers for alignment
    :param gap_min: minimum bases that separate left and right reads
    :param gap_max: gap_max: maximum bases that separate left and right reads
    :return: list of aligned pair-end positions and the pair-end reads written in the
                orientation that presented the best alignment
    """
    genome_table = genome_hash(ref, k)
    all_alignment_pos = []
    all_oriented_reads = []

    count = 0
    start = time.clock()

    for read_pair in paired_end_reads:
        aligned_pos = []
        oriented_reads = []

        # Find best alignment for each read pair
        for read in read_pair:
            # Align single read in pair
            min_mismatch, min_mismatch_pos = read_align(read, k, ref, genome_table)

            # Align reverse of read
            rev_read = read[::-1]
            rev_min_mismatch, rev_mismatch_pos = read_align(rev_read, k, ref, genome_table)

            # Get best alignment from read vs. reversed read
            if rev_min_mismatch < min_mismatch:
                min_mismatch = rev_min_mismatch
                min_mismatch_pos = rev_mismatch_pos
                read = rev_read

            # Throw out read if # of mismatches is more than acceptable amount
            if min_mismatch < 4:
                aligned_pos.append(min_mismatch_pos)
                oriented_reads.append(read)

        # Append only if both reads in pair have acceptable alignment
        if len(aligned_pos) >= 2:
            gap = abs(aligned_pos[0] - aligned_pos[1])
            if gap_min <= gap <= gap_max:
                all_alignment_pos.append(aligned_pos)
                all_oriented_reads.append(oriented_reads)

        # Timer
        count += 1
        if count % 100 == 0:
            time_passed = (time.clock() - start) / 60
            print('{} reads aligned'.format(count), 'in {:.3} minutes'.format(time_passed))
            remaining_time = time_passed / count * (len(paired_end_reads) - count)
            print('Approximately {:.3} minutes remaining'.format(remaining_time))


    return all_alignment_pos, all_oriented_reads


if __name__ == "__main__":
    data_folder = 'hw2undergrad_E_2'
    input_folder = join('../data/', data_folder)
    f_base = '{}_chr_1'.format(data_folder)
    reads_fn = join(input_folder, 'reads_{}.txt'.format(f_base))
    start = time.clock()
    input_reads = read_reads(reads_fn)
    small_input = input_reads[:100]

    reference_fn = join(input_folder, 'ref_{}.txt'.format(f_base))
    reference = read_reference(reference_fn)
    alignments, reads = genome_align(input_reads, reference, 16, 140, 160)

    print(alignments)
    print(reads)
    output_str = pretty_print_aligned_reads_with_ref(reads, alignments, reference)
    output_fn = join(input_folder, 'aligned_{}.txt'.format(f_base))
    with(open(output_fn, 'w')) as output_file:
         output_file.write(output_str)
