from flask import Flask
from modules.routes import *

from dotenv import load_dotenv
import os
load_dotenv()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.getenv('PORT') ,debug=True)