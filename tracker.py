from datetime import datetime

def log_lines(count):
    today = datetime.today().strftime('%Y-%m-%d')
    with open("history.csv", "a") as f:
        f.write(f"{today},{count}\n")
    print(f"[✓] Logged {count} lines on {today}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python3 tracker.py <line_count>")
    else:
        log_lines(int(sys.argv[1]))
        
