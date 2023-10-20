from flask import Flask, render_template, request,flash,jsonify,Response
from get_email import get_emaillist
from send_mail import sendMail
from pla import palm_promt
from flask_bootstrap import Bootstrap
import time 


#from pla import palm_promt
app = Flask(__name__)
app.secret_key = 'your_secret_key_here'
Bootstrap(app)
cake="hello world "
prompt='software'
messages = ""
#global selected_email
@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html",cake=cake)


@app.route('/fetch_emails', methods=['POST'])
def fetch_emails():
    # Handle the AJAX request for fetching email IDs based on the search query
    query = request.json['query']
    # Perform a database query or any other data retrieval here
    # Example: email_list = get_emails_from_db(query)
    #prompt = request.get_json()
    email_list=get_emaillist(query)
    return jsonify(email_list=email_list)


@app.route('/generate_email', methods=['POST'])
def generate_email():
    # Handle the AJAX request for generating the email
    selected_email = request.json['selectedEmail']
    prompt = request.json['prompt']
   
    # Generate the email here (combine email and prompt)
    generated_email = palm_promt(selected_email+' '+prompt)
    return jsonify(generated_email=generated_email)
    #return 

@app.route('/send_email', methods=['POST'])
def send_email():
    
   
    # Access the generated email and subject from the form
    json=request.get_json()
    generated_email=json['generate_email']
    subject = json['subject']
    selected_email = json['selected_email']
    #print(selected_email)
    #sendMail(email_receiver=selected_email, body=generated_email, subject=subject)
    
  

        #Send the email (e.g., using a mail library)
    if sendMail(email_receiver=selected_email, body=generated_email, subject=subject):
       flash('success', "Email sent successfully.")
       messages
       print('flit')
    else:
        flash('failure', "Email sending failed.")
    
    
    # Redirect to a response page or render a template
    return render_template('response.html')




def event_stream():
    while True:
        if len(messages) > 0:
            yield f"data: {messages.pop(0)}\n\n"
        else:
            time.sleep(1)

@app.route('/subscribe')
def subscribe():
    return Response(event_stream(), content_type='text/event-stream')

@app.route('/push', methods=['POST'])
def push():
    message = request.form.get('message')
    messages.append(message)
    flash(message)  # Flash the message
    return "Message sent"


if __name__ == "__main__":
    
    app.run(debug=True)
    


