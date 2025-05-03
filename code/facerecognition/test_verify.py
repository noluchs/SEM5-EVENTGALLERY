import requests

with open("img1.jpg", "rb") as f1, open("img2.jpg", "rb") as f2:
    response = requests.post(
        "http://127.0.0.1:5002/face/verify",
        files={"img1": f1, "img2": f2}
    )

    print("Status:", response.status_code)
    try:
        print("JSON:", response.json())
    except Exception:
        print("Kein gültiges JSON:")
        print(response.text)