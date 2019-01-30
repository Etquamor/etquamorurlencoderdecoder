__author__ = "Etquamor"
__date__ = "31.01.2019"

import urllib.parse
import argparse


def parameterChecker():
    parser = argparse.ArgumentParser()

    parser.add_argument("--encode","-e", help="You need enter data which you want to encode url form" ,nargs="+")
    parser.add_argument("--decode","-d", help="You need enter data which you want to decode url form")
        
    arguments = parser.parse_args()
    if arguments.encode:
        encode(" ".join(arguments).encode)
    if arguments.decode:
        decode(arguments.decode)

def encode(data):
    encodedData = urllib.parse.quote_plus(str(data))
    if encodedData != data:
        print("\n[*] "+str(data),"\t|| Encode  ==>\t",encodedData)
    else:
        print("\n[*] "+str(data),"\t|| Encode  ==>\t","There is nothing to encode because encoded data and entered data is same")

def decode(data):
    decodedData = urllib.parse.unquote_plus(str(data))
    if decodedData != data:
        print("\n[*] "+str(data),"\t|| Decode  ==>\t",decodedData)
    else:
        print("\n[*] "+str(data),"\t|| Decode  ==>\t","There is nothing to decode because decoded data and entered data is same")

if __name__=="__main__":
    try:
        parameterChecker()
    except Exception as e:
        print("[-] Unexpected Error!\n[#] Error ==>",e)
        exit()