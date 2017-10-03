from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from cassandra import ConsistencyLevel
import os

auth_provider = PlainTextAuthProvider(username=os.environ.get("CASSANDRA_USER"), password=os.environ.get("CASSANDRA_PASSWORD"))
cluster = Cluster(os.environ.get("CASSANDRA_SERVER").split(","),port=9042,auth_provider=auth_provider)
session = cluster.connect('messagemicroservice')

getQuery = session.prepare("SELECT user_id,backup_tx_stamp,msg_hash,category,msg_text from messages_by_users where backup_tx_stamp>? ALLOW FILTERING")
getQuery.consistency_level = ConsistencyLevel.QUORUM

updateQuery = session.prepare("insert into messages_by_users (user_id,backup_tx_stamp,msg_hash,category) values (?,?,?,?)")
getQuery.consistency_level = ConsistencyLevel.QUORUM

def getData(time):
    rows = session.execute(query=getQuery, parameters=[time])
    return rows


def updateCategory(category,userId,backupTime,hash):
    result = session.execute(query=updateQuery, parameters=(userId, backupTime, hash, category))
    return result





