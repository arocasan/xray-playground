import json
import logging
import os
import re
import sys
from datetime import datetime
from typing import Any

import requests
from dotenv import load_dotenv

module_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(module_path)

import mock_data as md

# My colors

BLUE = "\33[34m"
LBLUE = "\33[94m"
GREEN = "\33[92m"
RED = "\33[91m"    
YELLOW = "\33[93m"
PURP = "\33[95m"
BOLD = "\33[1m"
END = "\33[0m"

# Get todays date

today = datetime.today().strftime("%Y-%m-%d")

# Get evnironment variables from .env file

load_dotenv()

# Cloud Environment variables 

cloud_token = os.getenv("CLOUD_TOKEN")
user_email = os.getenv("USER_EMAIL")
site_url = os.getenv("SITE_URL")

# Server Enviroment variables

server_token = os.getenv("SERVER_TOKEN")
server_account = os.getenv("SERVER_ACCOUNT")
base_url = os.getenv("BASE_URL")

# Xray Environment variables

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
xray_url = os.getenv("XRAY_URL")

# logger

def aroca_logger():

    # Ask user if they want to tail the log

    tail_log = input(f"Do you want to tail log? {YELLOW}y/n{END}?:\n")

    # Set up logging 
    if tail_log in ("y","Y"):
        print(f"Log will be tailed... but also saved to {YELLOW}{BOLD}'{today}_aroca.log'{END}")
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)
        logging.basicConfig(handlers=[logging.FileHandler(f"logs/{today}_aroca.log"),console_handler], format="[ %(asctime)s ]-[ %(process)d ]-[ %(levelname)s ]-[ %(message)s ]", level=logging.DEBUG)

    else:
        print(f"OK, will only be logging to {YELLOW}{BOLD}'{today}_aroca.log'")
        logging.basicConfig(filename=f"logs/{today}_aroca.log",format="[ %(asctime)s ]-[ %(process)d ]-[ %(levelname)s ]-[ %(message)s ]",level=logging.DEBUG)


def xray_auth():

    s = requests.Session()
    s.headers = {
        "Accept": "application/json",
        "content-type":"application/json"
    }

    payload = json.dumps({
        "client_id" : f"{client_id}",
        "client_secret": f"{client_secret}"
    })

    response = s.post(f"{xray_url}/authenticate", data=payload)

    return response.json()



xray_token = xray_auth()

xray_test_key = "QA-1"

def export_datasets():

    s = requests.Session()
    s.headers = {
        "Accept": "application/json",
        "content-type":"application/json",
        "Authorization": f"Bearer {xray_token}"
    }

    response = s.get(f"{xray_url}/dataset/export?testIssueKey={xray_test_key}")

    print(response.content, "H")


#export_datasets()

qa_1 = md.qa_1
qa_2 = md.qa_2

def import_new_executions():

    s = requests.Session()
    s.headers = {
        "Accept": "application/json",
        "content-type":"application/json",
        "Authorization": f"Bearer {xray_token}"
    }

    payload = qa_1

    response = s.post(f"{xray_url}/import/execution",data=payload)
    print(payload)
    print(response.content)


#print(md.new_execution)

import_new_executions()
