from flask import Flask, render_template
from dotenv import load_dotenv
from pydactyl import PterodactylClient
from modules.config import *
import os, json

app = Flask(__name__)
api = PterodactylClient(panel_url, api_key)
app = Flask(__name__, template_folder='../views', static_folder='../static', static_url_path='/static')

@app.route('/')
def index():
    nodes = api.nodes.list_nodes().data
    nodes = [{'name': node['attributes']['name']} for node in nodes]

    users = api.user.list_users().data
    users = [{'attributes': {'id': user['attributes']['id']}, 'object': 'user'} for user in users]
    users_count = len(users)

    servers = api.servers.list_servers().data
    servers = [{'attributes': {'id': server['attributes']['id']}, 'object': 'server'} for server in servers]
    servers_count = len(servers)
    return render_template('index.html', title=title, alert=alert, nodes=nodes, users=users_count, servers=servers_count)

@app.route('/uptime')
def uptime():
    response = os.system("ping -c 1 " + hostname)
    if response == 0:
        print(hostname + ' is up!')
        status = '🟢 Online'
    else:
        print(hostname + ' is down!')
        status = '🔴 Offline'
    return render_template('uptime.html', title=title, status=status, hostname=hostname)
