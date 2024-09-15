from flask import Flask, request, jsonify
from notify import send_email_notification

app = Flask(__name__)

@app.route('/notify', methods=['POST'])
def notify():
    data = request.json

    # Extract relevant data from the request
    location = data.get('location')
    alert_type = data.get('alert_type')
    email = data.get('email')

    # Basic validation
    if not location or not alert_type or not email:
        return jsonify({'error': 'Missing data'}), 400

    # Call the function to send the email notification
    if send_email_notification(email, location, alert_type):
        return jsonify({'message': 'Notification sent successfully!'}), 200
    else:
        return jsonify({'error': 'Failed to send notification'}), 500

if __name__ == '__main__':
    app.run(debug=True)
