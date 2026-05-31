import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from lucky_block import LuckyBlockScanner
from config import load_config
import time

def test_scanner_basic():
    config = load_config()
    config["detection_chance"] = 1.0  # Always detect
    scanner = LuckyBlockScanner(config)
    
    results = scanner.scan()
    assert len(results) > 0, "Should find at least one lucky block"
    assert "type" in results[0], "Result should have type field"
    assert "position" in results[0], "Result should have position field"
    print("test_scanner_basic: PASS")

def test_scanner_empty():
    config = load_config()
    config["detection_chance"] = 0.0  # Never detect
    scanner = LuckyBlockScanner(config)
    
    results = scanner.scan()
    assert len(results) == 0, "Should find no lucky blocks"
    print("test_scanner_empty: PASS")

def test_scanner_rate_limit():
    config = load_config()
    config["detection_chance"] = 1.0
    scanner = LuckyBlockScanner(config)
    
    scanner.scan()  # First call
    results = scanner.scan()  # Immediate second call
    assert len(results) == 0, "Should be rate limited"
    print("test_scanner_rate_limit: PASS")

if __name__ == "__main__":
    test_scanner_basic()
    test_scanner_empty()
    test_scanner_rate_limit()
    print("\nAll tests passed!")