    @socketio.on("launch rover", namespace="/test")
    def launchRover():
        rtk.launchRover()
