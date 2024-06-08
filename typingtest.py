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
