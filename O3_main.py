from mq_o3 import *
import sys
import datetime
import json
# Instantiating datetime object
dt = datetime.datetime.now()


#try:
#print("Press CTRL+C to abort.")

mq = MQ_131()
while True:
  #storage location
     output_filename = r"/home/pi/logs/{}.{}".format(
         dt.strftime("%Y-%m-%d"), "json")    
    #creating a dictionary to store the data
     msg = {} 
     msg.update({"timestamp": time.strftime("%Y-%m-%d %H:%M:%S")})
     perc = mq.MQPercentage()

     msg.update({"O3": round(perc["O3"], 4)})
        
     with open(output_filename, "a") as output:
         output.write("\n\r")
         json.dump(msg, output)
#         
     time.sleep(60) # delay

     
     
       

#except:
    #print("\nAbort by user")
