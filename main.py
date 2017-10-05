from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
import datalayer as dt;
import time
import create_model as train_model
from logger import logger

start_time = time.time()

logger.info('process started')
cl = train_model.get_classifier()

rows = dt.getData(1504421826);

for row in rows:
    predicted_svm = cl.predict([row.msg_text])
    result = dt.updateCategory(category=predicted_svm[0],row=row)
    print result

logger.info('process ends')
print("--- %s seconds ---" % (time.time() - start_time))

