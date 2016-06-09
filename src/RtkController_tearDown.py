    def tearDown(self):
        self.rtkrcv.shutdown()
        self.assertFalse(self.rtkrcv.isAlive())