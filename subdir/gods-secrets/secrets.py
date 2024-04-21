class ClassOfGodsSecrets:
    def __init__(self, secret):
        self.secret = secret
    
    def get_secret(self):
        return self.secret
    
    def get_secret_length(self):
        return len(self.secret)
    
    def get_secret_hash(self):
        return hash(self.secret)