from flask import Flask, render_template
from dotenv import load_dotenv
from pydactyl import PterodactylClient
from modules.config import *
import os, json, time

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


if not os.path.exists('uptime.json'):
    with open('uptime.json', 'w') as f:
        json.dump({}, f)

@app.route('/uptime')
def uptime():
    monitors = []
    uptime_data = {}
    with open('uptime.json', 'r') as f:
        uptime_data = json.load(f)

    for key, value in config['monitor'].items():
        hostname = value['hostname']
        name = value['name']
        response = os.system("ping -c 1 " + hostname)
        if response == 0:
            status = '🟢'
        else:
            status = '🔴'

        if name not in uptime_data:
            uptime_data[name] = {
                'uptime_percentage': 100,
                'total_uptime': 0,
                'total_downtime': 0
            }

        if status == '🟢':
            uptime_data[name]['total_uptime'] += 1
        else:
            uptime_data[name]['total_downtime'] += 1

        total_checks = uptime_data[name]['total_uptime'] + uptime_data[name]['total_downtime']
        uptime_percentage = round((uptime_data[name]['total_uptime'] / total_checks) * 100, 2)
        uptime_data[name]['uptime_percentage'] = uptime_percentage

        monitors.append({'name': name, 'hostname': hostname, 'status': status, 'uptime_percentage': uptime_percentage})

    with open('uptime.json', 'w') as f:
        json.dump(uptime_data, f)

    return render_template('uptime.html', title=title, monitors=monitors, uptime_percentage=uptime_percentage)