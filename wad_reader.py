# Read the wad file ine binary mode
import struct

class WADReader:
    def __init__(self, wad_path):
        self.wad_file = open(wad_path, 'rb')

    def read_bytes(self, offset, num_bytes, byte_format):
        self.wad_file.seek(offset)

    def close(self):
        self.wad_file.close()