import time

def time_function(f):
  start_time = time.time()
  f()
  elapsed_time_ms = int((time.time() - start_time) * 1000)
  print(f"Function call took {elapsed_time_ms} ms")
  time.sleep(0.1)
  return elapsed_time_ms

def benchmark_function(f):
  # Do it twice to warm up
  time_function(f)
  time_function(f)
  time_function(f)
  num_runs = 10
  print(f"Timing {num_runs} runs")
  total_time_ms = sum([time_function(f) for i in range(0, num_runs)])
  print(f"Average {total_time_ms/num_runs} ms")

def benchmark_applescript():
  import actions
  print("Benchmarking actions.ms_teams_mute...")
  benchmark_function(actions.ms_teams_mute)

def benchmark_fast():
  import actions_fast
  print("Benchmarking actions_fast.ms_teams_mute...")
  benchmark_function(actions_fast.ms_teams_mute)

if __name__ == '__main__':
  benchmark_fast()
#  benchmark_applescript()
