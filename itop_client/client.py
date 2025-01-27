import json
import warnings
from typing import Any, Union

import requests
import urllib3

# Disable insecure warnings
urllib3.disable_warnings()
warnings.filterwarnings(action="ignore", message='.*using SSL with verify_certs=False is insecure.')


class ITopClient:
    url: str
    user: str
    passwd: str
    verify: bool


    def __init__(self, base_url: str, user: str, passwd: str, verify: bool = True) -> None:
        self.url = f"{base_url}/webservices/rest.php?version=1.4"
        self.user = user
        self.passwd = passwd
        self.verify = verify


    def request(self, json_data: dict[str, Any]):
        encoded_data = json.dumps(json_data)
        data = {
            'auth_user': self.user,
            'auth_pwd': self.passwd,
            'json_data': encoded_data
        }

        return requests.post(self.url, data, verify=self.verify, timeout=100).json()


    def check_credentials(self):
        json_data = {
            "operation": "core/check_credentials",
            "user": self.user,
            "password": self.passwd
        }

        result = self.request(json_data)
        if "authorized" in result.keys() and result['authorized'] is True:
            return True
        else:
            return False


    def get_object(self,
            class_name: str,
            key: Union[dict[str, Any], str],
            output_fields: Union[list[str], str] | None = None):
        data = {
            "operation": "core/get",
            "class": class_name,
            "key": key
        }
        if output_fields:
            data["output_fields"] = output_fields if isinstance(output_fields, str) else ','.join(output_fields)

        r = self.request(data)
        if r["code"] != 0 or r["objects"] is None:
            raise Exception(f'Failed to get {class_name} "{key}" : {r["message"]}')

        return list(r["objects"].values())


    def update_object(self,
            class_name: str,
            key: Union[dict[str, Any], str],
            fields: dict[str, Any],
            output_fields: Union[list[str], str] | None = None,
            comment: str = "itop_client"):
        data = {
            "operation": "core/update",
            "comment": comment,
            "class": class_name,
            "key": key,
            "fields": fields
        }
        if output_fields:
            data["output_fields"] = output_fields if isinstance(output_fields, str) else ','.join(output_fields)

        r = self.request(data)
        if r["code"] != 0 or r["objects"] is None:
            raise Exception(f'Failed to update {class_name} "{key}" : {r["message"]}')

        return list(r["objects"].values())


    def create_object(self, 
            class_name: str, 
            fields: dict[str, Any], 
            output_fields: Union[list[str], str] | None = None, 
            comment: str = "itop_client"):
        data = {
            "operation": "core/create",
            "comment": comment,
            "class": class_name,
            "fields": fields
        }
        if output_fields:
            data["output_fields"] = output_fields if isinstance(output_fields, str) else ','.join(output_fields)

        r = self.request(data)
        if r["code"] != 0 or r["objects"] is None:
            raise Exception(f'Failed to create {class_name} : {r["message"]}')

        return list(r["objects"].values())


    def apply_stimulus(self,
            class_name: str, 
            key: Union[dict[str, Any], str],
            stimulus: str,
            fields: dict[str, Any], 
            output_fields: Union[list[str], str] | None = None, 
            comment: str = "itop_client"):
        data = {
            "operation": "core/apply_stimulus",
            "comment": comment,
            "class": class_name,
            "key": key,
            "stimulus": stimulus,
            "fields": fields
        }
        if output_fields:
            data["output_fields"] = output_fields if isinstance(output_fields, str) else ','.join(output_fields)

        r = self.request(data)
        if r["code"] != 0 or r["objects"] is None:
            raise Exception(f'Failed to apply stimulus on {class_name} : {r["message"]}')

        return list(r["objects"].values())
