import pickle

#  model load
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# FEATURE FUNCTION ZARUR HAI KYUNKI MODEL KO FEATURES CHAHIYE PREDICTION KE LIYE
def extract_features(url):
    return [
        len(url),
        url.count("."),
        1 if "https" in url else 0,
        1 if "@" in url else 0,
        1 if "-" in url else 0,
        url.count("//"),
        url.count("="),
        url.count("www"),
        1 if "login" in url else 0,
        1 if "bank" in url else 0
    ]

#  user input MAIN KHUD DALUNGA 
url = input("Enter URL: ")

#  features nikaalna
features = extract_features(url)

#  prediction
prediction = model.predict([features])

# result MAIN PASS HUA YA FAIL 
if prediction[0] == 1:
    print("Phishing URL")
else:
    print("Safe URL")