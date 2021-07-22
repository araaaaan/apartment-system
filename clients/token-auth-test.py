import requests

def client():
    token_h  = "Token a34ddd99d2e286d7addc8040b87d56a5268a24db"
    # credentials = {"username" : "lock", "password" : "6666"}
    # response = requests.post("http://127.0.0.1:8000/api/rest-auth/login/", data=credentials)
    # print("Status Codedd: ", response.status_code)
    headers = {"Authorization": token_h}
    response = requests.post("http://127.0.0.1:8000/api/rest-auth/registration/", hearders=headers)
     
    print("Status Code: ", response.status_code)
    response_data = response.json()
    print(response_data)
if __name__ == "__main__":
    client()