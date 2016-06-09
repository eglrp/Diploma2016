    def test_status(self):
        """Receive rtkrcv status as a dict. Check the dict is valid."""
        keys = [
            'receiver time mark count', 'ant type base', 'solution status',
            ...
        ]

        for i in xrange(0, 100):
            self.assertEqual(self.rtkrcv.get_status().keys(), keys)