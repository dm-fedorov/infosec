#!/usr/bin/env python
#
# log2dot.py
#
# Input:
# Log files from stdin. We assume these files have been processed to
# provide the URL and Referer URL
#
# Output
# Stdout produces a dot file which can be run through graphviz
import sys, re
host_id = re.compile('^http://([^/]+)/.*$')
pairs = {}
nodes = {}
def graph_output(nodes, pairs):
    graph_header = """
                digraph graph_output {
                    rotate = 90;
                    size="7.5,10";
                """
    print(graph_header)
    a = nodes.keys()
    a.sort()
    for i in a:
        print("node [shape = circle] i;")
        a = pairs.keys()
    a.sort()
    for i in a:
        for j in pairs[i].keys():
            # Prints each link then labels it with the number of occurrences
            print('%s -> %s [label="%d"] ;' % (i,j,pairs[i][j]))
    print("}")

    if __name__ == '__main__':
        for i in sys.stdin.readlines():
            values = i[:-1].split()
            host = values[-2][:-1]
            referrer = values[-1]
            if host_id.match(referrer):
                refname = host_id.match(referrer).groups()[0]
            else:
                refname = referrer
                a = host.split('.')
            if a[0] == 'www':
                host = '.'.join(a[1:])
            a = refname.split('.')
            if a[0] == 'www':
                refname = '.'.join(a[1:])
            host = host.replace('-','_')
            host = host.replace('.','_')
            refname = refname.replace('-','_')
            refname = refname.replace('.','_')
            nodes[host] = 1
            nodes[refname] = 1
            if pairs.has_key(refname):
                if pairs[refname].has_key(host):
                    pairs[refname][host] += 1
                else:
                    pairs[refname][host] = 1
            else:
                pairs[refname] = {host:1}
        graph_output(nodes, pairs)
