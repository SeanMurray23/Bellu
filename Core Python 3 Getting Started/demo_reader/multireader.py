import os

from demo_reader.compressed import gzipped, bzipped

extension_map = {
    '.bz2': bzipped.opener,
    '.gz': gzipped.opener
}

class MultiReader:
    def __init__(self, filename):
        extension = os.path.splitext(filename)[1]
        self.f = open(filename, 'rt')
        
    def close(self):
        self.f.close()
        
    def read(self):
        return self.f.read()
    