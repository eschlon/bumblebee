class Transformer(object):

    def __init__(self, manifest):
        self.manifest = manifest

    def transform(self, record):
        return record

    def __call__(self, record):
        return self.transform(record)
