    def launch(self, config_name = None):
      if config_name is None:
        config_name = "reach_single_default.conf"

      if not self.launched:
        self.semaphore.acquire()

        if "/" in config_name:
          spawn_command = self.bin_path + "/rtkrcv -o " + config_name
        else:
          spawn_command = self.bin_path + "/rtkrcv -o " + self.config_path + "/" + config_name

        self.child = pexpect.spawn(spawn_command, cwd = self.bin_path, echo = False)

        if self.expectAnswer("spawn") < 0:
          self.semaphore.release()
          return -1

        self.semaphore.release()
        self.launched = True
        self.current_config = config_name

        return 1

      return 2