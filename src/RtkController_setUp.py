    def setUp(self):
        self.rtkrcv = RtkController("RTKLIB")
        self.rtkrcv.launch("rtk.conf")
        self.assertTrue(self.rtkrcv.isAlive())