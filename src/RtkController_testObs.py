    def testObs(self):
        """Receive rtkrcv observations as a dict. Check the dict is valid."""
        for i in xrange(0, 100):
            self.assertTrue(self.rtkrcv.getObs())