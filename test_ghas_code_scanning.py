import os
import json
import requests

api_token = "Password_testing_github_code_scanning"

print(api_token)

import subprocess
domain = input("Enter the Domain: ")
output = subprocess.check_output(f"nslookup {domain}", shell=True, encoding='UTF-8')
print(output)
