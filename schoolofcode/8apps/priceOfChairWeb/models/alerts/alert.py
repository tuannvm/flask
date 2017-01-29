class Alert(object):
    def __init__(self, user, priceLimit, item):
        self.user = user
        self.priceLimit = priceLimit
        self.item = item

    def __repr__(self):
        return "Alert for {} on item {} with price {}".format(self.user, self.item, self.priceLimit)
        