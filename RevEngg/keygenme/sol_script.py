import hashlib
from cryptography.fernet import Fernet


#4,5,3,6,2,7,1,8
username_trial = "GOUGH"
aaa = "picoCTF{1n_7h3_|<3y_of_xxxxxxxx}"
arr = [4 , 5 , 3 , 6 , 2 , 7 , 1 , 8]

i = 23
for ele in arr:
    ch = hashlib.sha256(str(username_trial).encode('utf-8')).hexdigest()[ele]
    aaa = aaa[:i] + ch + aaa[i + 1 : ] 
    i += 1

print(aaa);
