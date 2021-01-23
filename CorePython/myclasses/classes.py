class person:
    def __init__(self, pid=1, full_name='Krishna', contact_address='Ktm'):
        self.pid = pid
        self.full_name = full_name
        self.contact_address = contact_address

    def __str__(self):
        return str(self.pid)+", "+self.full_name+", "+self.contact_address