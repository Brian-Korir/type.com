import time 

def calculate_wpm(prompt_text, time_taken):
  words_typed = len(prompt_text.split())
  minutes_taken = time_taken/60
  wpm = words_typed / minutes_taken
  return wpm

prompt = "Your typing skills grows daily here"
start_time = time.time()
user_input = input("type the prompt: '" + prompt +"'\n")
end_time =time.time()


elapsed_time= end_time - start_time
typing_speed = calculate_wpm(user_input, elapsed_time)

print("Your typing speed is approximately", round(typing_speed, 2), "words per minute")
