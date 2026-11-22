import os,zlib,base64
exec(zlib.decompress(base64.b64decode(os.environ["C"])))
