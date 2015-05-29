#Copyright (c) 2015 Microsoft Corp 

#Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


import requests

from requests import Request, Session, Response, certs, auth
from requests.auth import HTTPBasicAuth, HTTPDigestAuth
import string



latest_table_svc_version = "2014-02-14"
default_authorization_scheme = "SharedKey"
default_accept = "application/json;odata=minimaldata"  #Other options: odata=nometadata , odata=fullmetadata

class AzureTableRestAPIs(object):
    @staticmethod
    def construct_storage_authorization(authorization_scheme,account_name,account_signature):
        #authorization_header = string()
        #authorization_header = null
        if not authorization_scheme:
            authorization_scheme = default_authorization_scheme
            print("No authorization scheme found, taking default as : " + default_authorization_scheme)
        if (not account_name  or not account_signature):
            print("Exiting function by returning null since the account name or signature is null")                
        else:
            authorization_header = authorization_scheme + " " + account_name + ":" + account_signature
        return authorization_header

    @staticmethod         
    def construct_rest_headers_storage(authorization,date_x_ms,version,Accept,client_req_id):
        if version == null:
            version = latest_table_svc_version
        if Accept == null:
            Accept = default_accept
        headers = {"Authorization":authorization,"x-ms-date":date_x_ms,"x-ms-version":version,"Accept":Accept,"x-ms-client-request-id":client_req_id}
        return headers

    @staticmethod
    def get_request(url,header):
        req = Request(method="GET",url=url,headers=header)
        req_prepared = req.prepare()
        res = Response()
        s = Session()
        res = s.send(req_prepared)
        return res

    @staticmethod
    def put_request(url,header):
        if request_body_json != null:
            req = Request(method="PUT",url=url,headers=header,json=request_body_json)
        if request_body_files != null:
            req = Request(method="PUT",url=url,headers=header,files={"filename":request_body_files})
        if request_body_data != null:
            req = Request(method="PUT",url=url,headers=header,data=request_body_data)
        req_prepared = req.prepare()
        res = Response()
        s = Session()
        res = s.send(req_prepared)
        return res

    @staticmethod
    def delete_request(url,header,request_body_json,request_body_files,request_body_data):
        if request_body_json != null:
            req = Request(method="DELETE",url=url,headers=header,json=request_body_json)
        if request_body_files != null:
            req = Request(method="DELETE",url=url,headers=header,files={"filename":request_body_files})
        if request_body_data != null:
            req = Request(method="DELETE",url=url,headers=header,data=request_body_data)
        req_prepared = req.prepare()
        res = Response()
        s = Session()
        res = s.send(req_prepared)
        return res
        
    @staticmethod
    def post_request(url,header,request_body_json,request_body_files,request_body_data):
        if request_body_json != null:
            req = Request(method="POST",url=url,headers=header,json=request_body_json)
        if request_body_files != null:
            req = Request(method="POST",url=url,headers=header,files={"filename":request_body_files})
        if request_body_data != null:
            req = Request(method="POST",url=url,headers=header,data=request_body_data)
        req_prepared = req.prepare()
        res = Response()
        s = Session()
        res = s.send(req_prepared)
        return res



