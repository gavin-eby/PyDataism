import time
import sys
from datetime import datetime

def true_cosmic_tracker():
    # --- 1. THE PRE-1970 BASELINE ---
    # Total milliseconds in 13.8 billion years
    years = 13_800_000_000
    days_per_year = 365.2425  # Precise Gregorian calendar average to account for leap years
    hours = 24
    minutes = 60
    seconds = 60
    ms = 1000
    
    pre_1970_ms = int(years * days_per_year * hours * minutes * seconds * ms)
    
    print("=" * 60)
    print("        TRUE LIVE COSMIC MILLISECOND CLOCK")
    print("=" * 60)
    print("Tracking every exact ms from 13.8B years ago to RIGHT NOW.")
    print("Press Ctrl+C to stop.\n")
    time.sleep(1)

    try:
        while True:
            # --- 2. THE LIVE MODERN ERA ---
            # time.time() gets the exact seconds (with decimals for ms) since Jan 1, 1970
            live_modern_ms = int(time.time() * 1000)
            
            # --- 3. THE TRUE GRAND TOTAL ---
            # Combining the ancient baseline with the exact live time of today
            exact_total_ms = pre_1970_ms + live_modern_ms
            
            # Print the live updating number
            sys.stdout.write(f"\rMilliseconds since the Big Bang: {exact_total_ms:,} ms")
            sys.stdout.flush()
            
            # Sleep for a tiny fraction of a second to prevent CPU overload
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\n\nClock paused.")
        print("=" * 60)

if __name__ == "__main__":
    true_cosmic_tracker()