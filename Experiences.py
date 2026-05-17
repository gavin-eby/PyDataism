from datetime import datetime
import time





print("Experience Equation Generator")
birthday = input("enter the start of the 26th week of you being in the womb (example: 2006-05-19)")
birthtime = "00:00:00"

try:

    birth_datetime = datetime.strptime(f"{birthday} {birthtime}", "%Y-%m-%d %H:%M:%S")
    birth_timestamp = birth_datetime.timestamp()
    print(f"{'CURRENT CLOCK':<12} | {'TOTAL ELAPSED SECONDS':<22} | {'EXPERIENCE (Elapsed / 0.1)'}")


    tick_counter = 0

    while True:
         now = time.time()

         elapsed_seconds = now - birth_timestamp

         final_answer = elapsed_seconds / 0.1

         tick_counter += 1
         if tick_counter >= 7:
              clock_str = datetime.fromtimestamp(now).strftime("%H:%M:%S")
              print(f"{clock_str:<12} | {elapsed_seconds:<22,.6f} | {final_answer:,.6f}")

              tick_counter = 0

              time.sleep(0.1)






except ValueError:
    print("\n[Error] Invalid Format. Please Restart and use the examples as reference.")
