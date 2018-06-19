from multiprocessing import cpu_count

bind = ['0.0.0.0:8000', '[::0]:8000']
daemon = False
workers = cpu_count() * 2 + 1
# workers = cpu_count() * 1
max_requests = 1000
