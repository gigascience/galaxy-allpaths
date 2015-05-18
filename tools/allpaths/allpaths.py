"""
allpaths.py
A wrapper script for ALLPATHS-LG to process S. aureus and R. sphaeroides data
Peter Li - GigaScience and BGI-HK
"""

import optparse
import os
import shutil
import sys


def stop_err(msg):
    sys.stderr.write(msg)
    sys.exit()


def cleanup_before_exit(tmp_dir):
    if tmp_dir and os.path.exists(tmp_dir):
        shutil.rmtree(tmp_dir)


def main():
    # Parse command line
    parser = optparse.OptionParser()
    parser.add_option("", "--data_source", dest="data_source")
    parser.add_option("", "--tool_dir", dest="tool_dir")
    # Outputs
    parser.add_option("", "--contigs", dest="contigs")
    parser.add_option("", "--scaffolds", dest="scaffolds")
    parser.add_option("", "--in_groups", dest="in_groups")
    parser.add_option("", "--in_libs", dest="in_libs")
    opts, args = parser.parse_args()

    print "tool_dir: ", opts.tool_dir

    # Read allpaths results into outputs
    if opts.data_source == "aureus":
        contigs_out = open(opts.contigs, 'w')
        f = open(opts.tool_dir + '/saureus/final.contigs.fasta')
        for line in f:
            contigs_out.write(line)
        contigs_out.close()

        scaffolds_out = open(opts.scaffolds, 'w')
        f = open(opts.tool_dir + '/saureus/final.assembly.fasta')
        for line in f:
            scaffolds_out.write(line)
        scaffolds_out.close()

        ingroups_out = open(opts.in_groups, 'w')
        f = open(opts.tool_dir + '/saureus/in_groups.csv')
        for line in f:
            ingroups_out.write(line)
        ingroups_out.close()

        inlibs_out = open(opts.in_libs, 'w')
        f = open(opts.tool_dir + '/saureus/in_libs.csv')
        for line in f:
            inlibs_out.write(line)
        inlibs_out.close()
    else:
        contigs_out = open(opts.contigs, 'w')
        f = open(opts.tool_dir + '/rsphaeroides/final.contigs.fasta')
        for line in f:
            contigs_out.write(line)
        contigs_out.close()

        scaffolds_out = open(opts.scaffolds, 'w')
        f = open(opts.tool_dir + '/rsphaeroides/final.assembly.fasta')
        for line in f:
            scaffolds_out.write(line)
        scaffolds_out.close()

        ingroups_out = open(opts.in_groups, 'w')
        f = open(opts.tool_dir + '/rsphaeroides/in_groups.csv')
        for line in f:
            ingroups_out.write(line)
        ingroups_out.close()

        inlibs_out = open(opts.in_libs, 'w')
        f = open(opts.tool_dir + '/rsphaeroides/in_libs.csv')
        for line in f:
            inlibs_out.write(line)
        inlibs_out.close()

    # Check results in output file
    if os.path.getsize(opts.contigs) > 0:
        sys.stdout.write('Status complete')
    else:
        stop_err("Problem with ALLPATHS process")

if __name__ == "__main__":
    main()

