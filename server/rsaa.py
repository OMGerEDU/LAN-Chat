
import rsa
import os
from rsa import verify, sign, encrypt, decrypt, PublicKey, PrivateKey, pkcs1



def public_key_to_file(public_key, filepath):
    with open(filepath, 'wb+') as f:
        pk = PublicKey.save_pkcs1(public_key, format='PEM')
        f.write(pk)


def private_key_to_file(private_key, filepath):
    with open(filepath, 'wb+') as f:
        pk = PrivateKey.save_pkcs1(private_key, format='PEM')
        f.write(pk)


path = os.path.dirname(os.path.abspath(__file__))   
publicKey, privateKey = rsa.newkeys(4096)
public_path =  (path+'\\keys.text')
private_path = (path+"\\private_keys.text")
public_key_to_file(publicKey,public_path)
private_key_to_file(privateKey,private_path)

