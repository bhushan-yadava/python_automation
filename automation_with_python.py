pip install twilio requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from twilio.rest import Client
import requests
import json

# -------------------------------
# 1. Send an Email
# -------------------------------
def send_email():
    sender = "your_email@gmail.com"
    receiver = input("Enter recipient email: ")
    subject = input("Enter subject: ")
    body = input("Enter message body: ")

    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender, "your_app_password")  # Use App Password
        server.sendmail(sender, receiver, msg.as_string())
        server.quit()
        print("✅ Email sent successfully!")
    except Exception as e:
        print("❌ Error:", e)


# -------------------------------
# 2. Send SMS using Twilio
# -------------------------------
def send_sms():
    account_sid = "your_twilio_sid"
    auth_token = "your_twilio_auth_token"
    client = Client(account_sid, auth_token)

    to_number = input("Enter recipient phone number (+91...): ")
    body = input("Enter SMS text: ")

    try:
        message = client.messages.create(
            body=body,
            from_="+1234567890",  # Your Twilio number
            to=to_number
        )
        print("✅ SMS sent! SID:", message.sid)
    except Exception as e:
        print("❌ Error:", e)


# -------------------------------
# 3. Make a Phone Call using Twilio
# -------------------------------
def make_call():
    account_sid = "your_twilio_sid"
    auth_token = "your_twilio_auth_token"
    client = Client(account_sid, auth_token)

    to_number = input("Enter recipient phone number (+91...): ")
    try:
        call = client.calls.create(
            twiml='<Response><Say>Hello! This is a Python test call.</Say></Response>',
            to=to_number,
            from_="+1234567890"  # Your Twilio number
        )
        print("✅ Call initiated! SID:", call.sid)
    except Exception as e:
        print("❌ Error:", e)


# -------------------------------
# 4. Post on LinkedIn
# -------------------------------
def post_linkedin():
    access_token = "your_linkedin_access_token"
    message = input("Enter LinkedIn post message: ")

    url = "https://api.linkedin.com/v2/ugcPosts"
    headers = {"Authorization": f"Bearer {access_token}", "Content-Type": "application/json"}

    payload = {
        "author": "urn:li:person:your_profile_id",
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {"text": message},
                "shareMediaCategory": "NONE"
            }
        },
        "visibility": {"com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"}
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))
    print("✅ LinkedIn Response:", response.json())


# -------------------------------
# 5. Post on Twitter (X)
# -------------------------------
def post_twitter():
    bearer_token = "your_twitter_bearer_token"
    message = input("Enter Tweet: ")

    url = "https://api.twitter.com/2/tweets"
    headers = {"Authorization": f"Bearer {bearer_token}", "Content-Type": "application/json"}
    payload = {"text": message}

    response = requests.post(url, headers=headers, data=json.dumps(payload))
    print("✅ Twitter Response:", response.json())


# -------------------------------
# 6. Post on Facebook
# -------------------------------
def post_facebook():
    page_access_token = "your_facebook_page_token"
    message = input("Enter Facebook post: ")

    url = f"https://graph.facebook.com/v17.0/me/feed"
    payload = {"message": message, "access_token": page_access_token}

    response = requests.post(url, data=payload)
    print("✅ Facebook Response:", response.json())


# -------------------------------
# 7. Post on Instagram
# -------------------------------
def post_instagram():
    access_token = "your_instagram_access_token"
    ig_user_id = "your_instagram_user_id"
    caption = input("Enter Instagram caption: ")

    image_url = input("Enter image URL (publicly accessible): ")

    # Step 1: Create Media Object
    url = f"https://graph.facebook.com/v17.0/{ig_user_id}/media"
    payload = {"image_url": image_url, "caption": caption, "access_token": access_token}
    response = requests.post(url, data=payload)
    result = response.json()
    creation_id = result.get("id")

    # Step 2: Publish Media
    publish_url = f"https://graph.facebook.com/v17.0/{ig_user_id}/media_publish"
    publish_payload = {"creation_id": creation_id, "access_token": access_token}
    publish_response = requests.post(publish_url, data=publish_payload)
    print("✅ Instagram Response:", publish_response.json())


# -------------------------------
# 8. Send WhatsApp Message (Twilio)
# -------------------------------
def send_whatsapp():
    account_sid = "your_twilio_sid"
    auth_token = "your_twilio_auth_token"
    client = Client(account_sid, auth_token)

    to_number = input("Enter WhatsApp number (+91...): ")
    body = input("Enter WhatsApp message: ")

    try:
        message = client.messages.create(
            body=body,
            from_="whatsapp:+14155238886",  # Twilio Sandbox WhatsApp number
            to=f"whatsapp:{to_number}"
        )
        print("✅ WhatsApp sent! SID:", message.sid)
    except Exception as e:
        print("❌ Error:", e)


# -------------------------------
# Main Menu
# -------------------------------
def main():
    while True:
        print("\n====== Python Automation Menu ======")
        print("1. Send Email")
        print("2. Send SMS")
        print("3. Make a Phone Call")
        print("4. Post on LinkedIn")
        print("5. Post on Twitter (X)")
        print("6. Post on Facebook")
        print("7. Post on Instagram")
        print("8. Send WhatsApp Message")
        print("9. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            send_email()
        elif choice == '2':
            send_sms()
        elif choice == '3':
            make_call()
        elif choice == '4':
            post_linkedin()
        elif choice == '5':
            post_twitter()
        elif choice == '6':
            post_facebook()
        elif choice == '7':
            post_instagram()
        elif choice == '8':
            send_whatsapp()
        elif choice == '9':
            print("Exiting program...")
            break
        else:
            print("❌ Invalid choice! Try again.")


if __name__ == "__main__":
    main()
