    def broadcastSatellites(self):
      count = 0
      while self.server_not_interrupted:
        self.rtkc.getObs()
        if count % 10 == 0:
          print("Sending sat rover levels:\n" + str(self.rtkc.obs_rover))
          print("Sending sat base levels:\n" + str(self.rtkc.obs_base))

        self.socketio.emit("satellite broadcast rover", self.rtkc.obs_rover, namespace = "/test")
        self.socketio.emit("satellite broadcast base", self.rtkc.obs_base, namespace = "/test")
        count += 1
        time.sleep(1)
