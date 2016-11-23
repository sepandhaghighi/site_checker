import requests
import socket
import re
import subprocess as sub

ip_pattern=r"[10-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}"
def internet(host="8.8.8.8", port=53, timeout=3):

    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except Exception as ex:
        print (ex.message)
        return False
def check_status(site_name):
    try:
        request=requests.get(site_name)
        return True

    except:
        return False

def ping(site_name):
    try:
        response=sub.Popen("ping "+site_name,stderr=sub.PIPE,stdin=sub.PIPE,stdout=sub.PIPE,shell=True)
        output_string=response.communicate()
        return output_string
    except:
        print("Error In Ping")
def ip_extract(text):
    return list(set(re.findall(ip_pattern,text)))
if __name__=="__main__":
    if internet(): # Check Internet Connection
        raw_input=input("Please Enter Your Website:") # Get Input Website As String
        if raw_input.find("http://")==-1: # Check http in input
            raw_input="http://"+raw_input # if there is no http add it
        if check_status(raw_input): # check the response of request ot find the website
            raw_response=ping(raw_input[7:len(raw_input)]) # call ping function and return response of console
            print("Your Site: "+raw_input+" is available")
            print("And IP Addresses:")
            print(ip_extract(str(raw_response))) #call regular expression and find the ip pattern in it and print output
        else:
            print("Your Site: "+raw_input+" is not available")
    else:
        print ("Error In Internet Connection")
            
        
        
    
