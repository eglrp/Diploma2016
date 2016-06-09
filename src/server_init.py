    from flask import Flask, render_template, session, request, send_file
    from flask.ext.socketio import SocketIO, emit, disconnect
    from subprocess import check_output

    app = Flask(__name__)
    app.template_folder = "."
    app.debug = False
    ...

    socketio = SocketIO(app)
