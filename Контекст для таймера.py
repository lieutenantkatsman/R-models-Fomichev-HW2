import time

class MyTimer:
	def __init__(self, units):
		self.units = units

	def __enter__(self):
		self.first_time = time.perf_counter()
		return self

	def __exit__(self, exc_type, exc_value, exc_tb):
		self.last_time = time.perf_counter()

	def elapsed_time(self):
		self.all_time = self.last_time - self.first_time
		if self.units == "h":
			return self.all_time / 3600
		elif self.units == "m":
			return self.all_time / 60
		return self.all_time

with MyTimer(units="h") as t:
	print("Hello world")

print(t.elapsed_time())