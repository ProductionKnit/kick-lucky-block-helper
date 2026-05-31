import json
import urllib.request
import urllib.error

def send_webhook(url, data):
    if not url:
        return False
    
    payload = {
        "content": f"Found {len(data)} lucky block(s)!",
        "embeds": [
            {
                "title": "Lucky Block Detected",
                "description": f"Position: ({d['position']['x']}, {d['position']['y']}, {d['position']['z']})",
                "color": 16776960
            } for d in data
        ]
    }
    
    try:
        req = urllib.request.Request(
            url,
            data=json.dumps(payload).encode(),
            headers={"Content-Type": "application/json"},
            method="POST"
        )
        with urllib.request.urlopen(req, timeout=5):
            return True
    except (urllib.error.URLError, urllib.error.HTTPError):
        print("Failed to send webhook")
        return False