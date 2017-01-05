#!/usr/bin/env python
# encoding: utf-8
from project.app import app

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, threaded=True)
