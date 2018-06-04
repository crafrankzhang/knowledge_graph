# -*- coding: utf-8 -*-


import gevent
from gevent.monkey import patch_all
patch_all()
from server import app
from server.config import *

if __name__ == '__main__':
     app.run(debug=True, host='0.0.0.0', port=8080)
