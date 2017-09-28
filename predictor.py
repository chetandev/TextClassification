import os
import cPickle as pickle
import time
import create_model as train_model


start_time = time.time()
cl = train_model.get_classifier()
predicted_svm = cl.predict(["Hello! We have credited Payment of Rs. 588.0 to your Vodafone mobile phone 9920183969. Your outstanding as on 2017-09-25 Rs. 0.19. Thank You.",
                        "Rakshita, we make a great team! We've counted your runs from last week & added Uber credits to your account. Check your app for more. T&C: t.uber.com/cric",
                        "Enjoy your weekend with Uber in Mumbai. Use code 'JOY50X3' & get 50% off (up to Rs 75) on 3 rides. Valid only on non uberPOOL rides until Sept 24. Ride now!",
                        "Hooray Rakshita! You've unlocked uberPASS rewards this week. Get access to rides at flat Rs.99 upto 8km & Rs.159 from 8-15km, till 23 July. t.uber.com/pass5",
                         "An amount of Rs.191.80 has been debited from A/C no. XXXX9001 for an online payment done using HDFC Bank NetBanking. Exclusive offer http://bit.ly/2eN7UNz",
                         "Enjoy the rains by ordering in with UberEATS. Use code EATS50 to get 50% off on first 2 orders up to Rs.150. Valid in Mumbai until 30th June t.uber.com/eatsm"
                        ])
print((predicted_svm))

print("--- %s seconds ---" % (time.time() - start_time))