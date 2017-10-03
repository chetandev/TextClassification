from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
import datalayer as dt;
import time
import create_model as train_model

start_time = time.time()
cl = train_model.get_classifier()

rows = dt.getData(1504421826);

for row in rows:
    predicted_svm = cl.predict([row.msg_text])
    result = dt.updateCategory(category=predicted_svm[0],userId=row.user_id,backupTime=row.backup_tx_stamp,hash=row.msg_hash)
    print result

print("--- %s seconds ---" % (time.time() - start_time))
