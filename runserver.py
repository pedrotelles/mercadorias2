# encoding: utf-8

"""
This script runs the mercadorias application using a development server.
"""

from os import environ
from mercadorias import app

if __name__ == '__main__':
    environ['TZ'] = 'America/Sao_Paulo'
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
