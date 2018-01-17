#!/usr/bin/env python3

from flask import Flask, render_template, url_for
import requests
import json
import os
import re
import sys
import collections


PUPPETDB_API = os.getenv('PUPPETDB_API', None)
REFRESH = os.getenv('REFRESH', 100000)

app = Flask(__name__)

if not PUPPETDB_API:
    print("PUPPETDB_API unset. Aborting")
    sys.exit()

@app.route('/', methods=['GET'])
def index():
    facts = [
        'certname',
        'fqdn',
        'host_description',
        'uptime',
        'role_description',
        'datacenter',
        'environment',
        'project',
        'docker_info',
    ]
    hosts = {}
    for fact in facts:
        request_data = {
            'query': '["=", "name", "%s"]' % fact
        }
        response = requests.get(PUPPETDB_API + "/pdb/query/v4/facts", params=request_data)
        if response.ok:
            data = response.json()
            for item in data:
                certname = item['certname']
                if not certname in hosts:
                    hosts[certname] = {}
                hosts[certname]['certname'] = certname
                if fact == 'docker_info':
                    hosts[certname][fact] = {}
                    
                    id = 1
                    for line in iter(item['value'].splitlines()):
                        container_name, image_name = line.split(' ')
                        hosts[certname][fact][id] = {}
                        hosts[certname][fact][id]['container_name'] = container_name
                        hosts[certname][fact][id]['image_name'] = image_name
                        id += 1
                else:
                    hosts[certname][fact] = item['value']

    hosts_sorted = collections.OrderedDict(sorted(hosts.items()))
    return render_template('index.html', REFRESH=REFRESH, hosts=hosts_sorted)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
