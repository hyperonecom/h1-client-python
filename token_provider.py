class AccessTokenProvider():
    def __init__(self, token_provider):
        self.provider = token_provider

    def get(self):
        return self.provider.get_token()
