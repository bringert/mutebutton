import actions

import time

def time_ms_teams_mute():
  start_time = time.time()
  actions.ms_teams_mute()
  elapsed_time_ms = int((time.time() - start_time) * 1000)
  print(f"Muting mic took {elapsed_time_ms} ms")
  time.sleep(0.1)
  return elapsed_time_ms

if __name__ == '__main__':
  # Do it twice to warm up
  time_ms_teams_mute()
  time_ms_teams_mute()

  num_runs = 10
  print(f"Timing {num_runs} runs")
  total_time_ms = sum([time_ms_teams_mute() for i in range(0, num_runs)])
  print(f"Average {total_time_ms/num_runs} ms")
