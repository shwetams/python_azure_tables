from base_rest_calls import *
import uuid
import time
import datetime
from builtins import str
from base_rest_calls import AzureTableRestAPIs


version = "2014-02-14"
storageAccountName = "<storage account name>"
storageAccountKey = "<storage account key>"
storageKeyType = "<SharedKey|SharedKeyLite>"
entities = list()

def _new_boundary():
    uuid_boundary = str(uuid.uuid1()).encode('utf-8')
    return uuid_boundary

def insert_batch_entity(entities,table_name,partition_key):
    baseurl = "https://" + storageAccountName + ".table.core.windows.net/$batch"
    batch_boundary = str(_new_boundary())
    changeset_boundary = str(_new_boundary())
    authorization_header = str(AzureTableRestAPIs.construct_storage_authorization(storageKeyType,storageAccountName,storageAccountKey))
    #headers = {"x-ms-version":version,"Accept-Charset":"UTF-8","DataServiceVersion":"3.0","Content-Type":"multipart/mixed;"+" boundary="+"batch_"+ batch_boundary,"Accept":"application/json;odata=nometadata","Authorization":authorization_header,"Connection":"Keep-Alive"}
    request_body = b"--batch_" +  batch_boundary + b"\n"
    request_body += "Content-Type:multipart/mixed; boundary=" 
    request_body += b"changeset_" + changeset_boundary + b"\n\n"
    content_id = 1

    for entity in entities:
        
        url = "https://" + storageAccountName + ".table.core.windows.net/" + table_name + "(PartitionKey='" + partition_key + "',RowKey='" + entity["RowKey"]+"')"
        entity_keys = entity.keys()
        request_body += b'--' + changeset_boundary + b'\n'
        request_body += "Content-Type:application/http\n"
        request_body += "Content-Transfer-Encoding: binary\n\n"
        request_body += "PUT" + " " +url+ " "+ "HTTP/1.1\n"
        request_body += "x-ms-version:" + version
        request_body += "Content-Type:application/json"
        request_body += "Accept: application/json;odata=nometadata"
        request_body += "Prefer: return-no-content"
        request_body += "DataServiceVersion: 3.0;"
        request_body += str(entity)
        request_body += " HTTP/1.1\n"
        request_body += "Content-ID: " + str(content_id) + "\n"        
        content_id += 1 
    request_body += b"--changeset" + changeset_boundary + "--" + b"\n"
    request_body += b"--batch" + batch_boundary + b"--"
    print(request_body)

def insert_single_entity(entity,table_name,partition_key,row_key):
    url = "https://" + storageAccountName + ".table.core.windows.net/"+table_name


if __name__ == "__main__":
    ts = time.time()
    dttime = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    ent1 = {"RowKey":str(dttime), "FlatNumber" : "821", "Street":"Kirol Road", "City":"Mumbai"}
    ent2 = {"RowKey":"234","FlatNumber": "112","Street":"Missy lane","City":"Mumbai" }
    entities.append(ent1)
    entities.append(ent2)
    
    insert_batch_entity(entities,"address","sg_address")









