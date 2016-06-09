    def start(self):
      if not self.started:
        self.semaphore.acquire()
        self.child.send("start\r\n")

        if self.expectAnswer("start") < 0:
          self.semaphore.release()
          return -1

        self.semaphore.release()
        self.started = True
        return 1

      # already started
      return 2
