import google.generativeai as palm
import os
import config


def palm_promt(promptt):
    palm.configure(api_key=config.details['PALM_API'])
    response = palm.generate_text(prompt=promptt)
    #print(response.result) #  'cold.'
#
    return response.result
    

#print(palm_promt("can you craft a professional email to info@digitalscholar.in asking job in their companey [filings] beclear can images required paramenters"))



    
