FROM solr:9.7.0

USER root

# Install Python3 for the vulnerable proxy
RUN apt-get update && \
    apt-get install -y --no-install-recommends python3 && \
    rm -rf /var/lib/apt/lists/*

# Copy the vulnerable proxy and entrypoint
COPY vuln_proxy.py /opt/vuln_proxy.py
COPY entrypoint.sh /opt/entrypoint.sh
RUN chmod +x /opt/entrypoint.sh /opt/vuln_proxy.py

# Ensure directories exist with correct permissions
RUN mkdir -p /var/solr/data/configsets && \
    chown -R solr:solr /var/solr

USER solr
EXPOSE 8983

ENTRYPOINT ["/opt/entrypoint.sh"]
