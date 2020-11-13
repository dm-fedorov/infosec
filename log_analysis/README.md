# Log Analysis

* Data Sources Discussion - including PCAP, Firewall, IDS, Threat Intelligence (TI) Feeds, CloudTrail, CloudWatch, etc.
* Data Analysis and Visualization Linux (DAVIX)
* Log Data Processing (CSVKit, ...)
* SIEM, and Big Data

* Log Management and SIEM Overview
* LogStash (Elastic Stack) and Moloch
* Big Data - Hadoop, Spark, ElasticSearch, Hive, Impala
* Data Science

* Introduction to Data Science
* Hunting

# Visualization

* Information Visualization History
* Visualization Theory
* Data Visualization Tools and Libraries (e.g., Mondrian, Gephi, AfterGlow, Graphiti)
* Visualization Resources
* Security Visualization Use-Cases

* Perimeter Threat
* Network Flow Analysis
* Firewall Visualization
* IDS/IPS Signature Analysis
* Vulnerability Scans
* Proxy Data
* User Activity
* Host-based Data Analysis

# Sample of Tools and Techniques

Tools to gather data:
* argus, nfdump, nfsen, and silk to process traffic flows
* snort, bro, suricata as intrusion detection systems
* p0f, npad for passive network analysis
* iptables, pf, pix as examples of firewalls
* OSSEC, collectd, graphite for host data

We are also using a number of visualization tools to analyze example data in the labs:

* graphviz, tulip, cytoscape, and gephi
* afterglow
* treemap
* mondrian, ggobi

Under the log management section, we are going to discuss:

* rsyslog, syslog-ng, nxlog
* logstash as part of the elastic stack, moloch
* commercial log management and SIEM solutions

# The section on big data is covering the following:

* hadoop (HDFS, map-reduce, HBase, Hive, Impala, Zookeper)
* search engines like: elastic search, Solr
* key-value stores like MongoDB, Cassandra, etc.
* OLAP and OLTP
* The Spark ecosystem