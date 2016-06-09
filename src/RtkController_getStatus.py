    def getStatus(self):
      self.semaphore.acquire()
      self.child.send("status\r\n")

      if self.expectAnswer("get status") < 0:
          self.semaphore.release()
          return -1

      status = self.child.before.split("\r\n")
      if status != {}:
          for line in status:
              spl = line.split(":")

              if len(spl) > 1:
                  param = spl[0].strip()
                  value = spl[1].strip()

                  self.status[param] = value

      ...
