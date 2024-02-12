import webbrowser
import time

def automate_checkin_checkout(action):
    # Specify the URL based on checkin or checkout action
    url = "https://kalvium.community/signal/student_check_in_v1" if action == "checkin" else "https://kalvium.community/signal/student_check_out_v1"

    # Open the URL in the default browser
    webbrowser.open(url)

    # Sleep for a few seconds to allow the page to load
    time.sleep(5)

    # You may need to manually handle authentication here if required

# Example usage
action = input("Enter 'checkin' or 'checkout': ").lower()
