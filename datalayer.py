from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from cassandra import ConsistencyLevel
from logger import logger
import os
import time


auth_provider = PlainTextAuthProvider(username=os.environ.get("CASSANDRA_USER"), password=os.environ.get("CASSANDRA_PASSWORD"))
cluster = Cluster(os.environ.get("CASSANDRA_SERVER").split(","),port=9042,auth_provider=auth_provider)
session = cluster.connect('messagemicroservice')

getQuery = session.prepare("SELECT * from messages_by_users where backup_tx_stamp>? ALLOW FILTERING")
getQuery.consistency_level = ConsistencyLevel.QUORUM

updateQuery = session.prepare("""INSERT INTO messages_by_users
(user_id,device_key, msg_hash,msg_time,address,app_type,category,conv_id,device_msg_id,backup_tx_stamp,msg_type,name,operation,msg_text)
VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)
""")
getQuery.consistency_level = ConsistencyLevel.QUORUM

def getData(time):
    try:
        logger.info('inside getData function try block')
        rows = session.execute(query=getQuery, parameters=[time])
        logger.info('inside getData function try block data fetched successfully')
        return rows
    except Exception as e:
        logger.error('error while getting the data',exc_info=True)


def updateCategory(category,row):
    try:
        logger.info('inside updateCategory function try block')
        print category
        curr_timestamp = time.time()*1000
        result = session.execute(query=updateQuery, parameters=[row.user_id,row.device_key,row.msg_hash,row.msg_time,row.address,row.app_type,category,row.conv_id,row.device_msg_id,curr_timestamp,row.msg_type,row.name,row.operation,row.msg_text])
        logger.info('inside updateCategory function try block data inserted successfully', extra={"userid":row.user_id,"devicekey":row.device_key,"hash":row.msg_hash})
        return result
    except Exception as e:
        logger.error('error while updating  the data', exc_info=True)








