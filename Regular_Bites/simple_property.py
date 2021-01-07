from datetime import datetime

NOW = datetime.now()


class Promo(object):
    """Promo class"""

    def __init__(self, name, expires):
        self.name = name
        self.expires = expires

    @property
    def expired(self):
        return NOW > self.expires
