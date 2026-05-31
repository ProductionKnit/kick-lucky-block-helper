import sys
import time
from lucky_block import LuckyBlockScanner
from config import load_config
from webhook import send_webhook

def main():
    config = load_config()
    scanner = LuckyBlockScanner(config)
    
    print("Kick Lucky Block Helper started")
    print(f"Scanning interval: {config['scan_interval']}s")
    
    try:
        while True:
            results = scanner.scan()
            if results:
                print(f"Found {len(results)} lucky block(s)")
                if config.get("webhook_url"):
                    send_webhook(config["webhook_url"], results)
            time.sleep(config["scan_interval"])
    except KeyboardInterrupt:
        print("\nStopped by user")
        sys.exit(0)

if __name__ == "__main__":
    main()