import os
import json
import requests

api_token = "12930uqw98jhaskcbasgjdfvbdwksdahq"
secret = "lasdjas712yeihdasd"
passw = "C0mpl1c4t3d57r1ng"

print(api_token)

import subprocess
domain = input("Enter the Domain: ")
output = subprocess.check_output(f"nslookup {domain}", shell=True, encoding='UTF-8')
print(output)
