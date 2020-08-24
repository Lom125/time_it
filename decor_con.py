import time

class Secundomer:
	def __init__(self, num_runs):
		self.num_runs = num_runs
		self.t0 = time.time()
		print('Вычисляем ', num_runs, 'раз функцию, суммирующую члены последовательности Фибоначчи.')
	
	def run(self):
		def decorator(func):
			def wrap(param):
				time_a = 0
				for k in range(self.num_runs):
					for i in range(param):
						func(param)
					print(k+1, 'проход')		
				t1 = time.time()
				time_avr = (t1 - self.t0)/self.num_runs
				print('Среднее за ', self.num_runs, 'повторов время выполнения функции =', time_avr, ' сек.')	
			return wrap
		return decorator

	def __enter__(self):
		return self.run()

	def __exit__(self, mmm, type, value):
		return self

# Выполняем функцию fibon_it "num" раз
num = int(input('Введите количество проходов вычисления функции (примерно 10 - 20) '))

with Secundomer(num) as time_this: 
	@time_this
	def fibon_it(val):
		f = [1,2]
		s = 3
		while f[len(f)-1] < val:
			f_next = f[-1] + f[-2]
			f.append(f_next)
			s += f_next
		return s

# Функция вычисляет члены последовательности Фибонваччи примерно до значения "val" и их сумму.
val = 100000
fibon_it(val)