import webbrowser
import time

def automate_checkin_checkout(action):
    # Specify the URL based on checkin or checkout action
    url = "https://kalvium.community/signal/student_check_in_v1" if action == "checkin" else "https://kalvium.community/signal/student_check_out_v1"

