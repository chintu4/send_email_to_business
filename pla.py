import google.generativeai as genai
import os
import config


def palm_promt(promptt):


    genai.configure(api_key=config.details['PALM_API'])

    # palm.configure(api_key=config.details['PALM_API'])
    
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(promptt)
 
    return response.text
    

#print(palm_promt("can you craft a professional email to info@digitalscholar.in asking job in their companey [filings] beclear can images required paramenters"))



    
