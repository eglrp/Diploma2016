    def expectAnswer(self, last_command = ""):
        a = self.child.expect(["rtkrcv>", pexpect.EOF, "error"])
        # check rtklib output for any errors
        if a == 1:
            print("Encountered exception: " + str(self.child))
            return -1

        if a == 2:
            return -2

        return 1