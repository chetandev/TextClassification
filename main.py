from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
import datalayer as dt;
import time
import create_model as train_model
from logger import logger
import os

start_time = time.time()

logger.info('process started')

cl = train_model.get_classifier()

curr_timestamp = time.time()*1000 - int(os.environ.get("BACKUP_TIME_OFFSET_MS"))
print int(curr_timestamp)

rows = dt.getData(curr_timestamp)

for row in rows:
    if(row.category=="others"):
        predicted_svm = cl.predict([row.msg_text])
        result = dt.updateCategory(category=predicted_svm[0], row=row)
        print result

logger.info('process ends')
print("--- %s seconds ---" % (time.time() - start_time))

