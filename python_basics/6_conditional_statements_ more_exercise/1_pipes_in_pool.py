pool_v = int(input())
pipe_1_v = int(input())
pipe_2_v = int(input())
hours_gone = float(input())

percent = pool_v / 100

pool_full = ((pipe_1_v * hours_gone) + (pipe_2_v * hours_gone)) / percent
pool_full_percent = ((pipe_1_v * hours_gone) + (pipe_2_v * hours_gone)) / 100
percent_p1 = ((pipe_1_v * hours_gone) / pool_full_percent)
percent_p2 = ((pipe_2_v * hours_gone) / pool_full_percent)

difference = (pipe_1_v * hours_gone) + (pipe_2_v * hours_gone)
more = difference - pool_v
if pool_v >= difference:
    print(f"The pool is {pool_full:.2f}% full. Pipe 1: {percent_p1:.2f}%. Pipe 2: {percent_p2:.2f}%.")
else:
    print(f"For {hours_gone} hours the pool overflows with {more:.2f} liters.")