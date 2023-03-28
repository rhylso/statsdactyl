from flask import Flask, render_template
from dotenv import load_dotenv
from pydactyl import PterodactylClient
from dotenv import load_dotenv
import os
load_dotenv()

app = Flask(__name__)
api = PterodactylClient(os.getenv("PANEL_URL"), os.getenv("APPLICATION_API_KEY"))
app = Flask(__name__, template_folder='../views', static_folder='../static', static_url_path='/static')

TITLE = os.getenv('TITLE')
ALERT = os.getenv('ALERT')

@app.route('/')
def index():
    nodes = api.nodes.list_nodes().data
    nodes = [{"name": node["attributes"]["name"]} for node in nodes]

    users = api.user.list_users().data
    users = [{"attributes": {"id": user["attributes"]["id"]}, "object": "user"} for user in users]
    users_count = len(users)

    servers = api.servers.list_servers().data
    servers = [{"attributes": {"id": server["attributes"]["id"]}, "object": "server"} for server in servers]
    servers_count = len(servers)
    return render_template('index.html', title=TITLE, alert=ALERT, nodes=nodes, users=users_count, servers=servers_count)
