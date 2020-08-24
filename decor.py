import time

def time_this(num_runs=10):
	print('Вычисляем ', num_runs, 'раз функцию, суммирующую члены последовательности Фибоначчи.')
	def decorator(func):
		def wrap(param):
			time_a = 0
			for k in range(num_runs):
				t0 = time.time()
				for i in range(param):
					func(param)
				print(k+1, 'проход')
				t1 = time.time()
				time_a += (t1 - t0)
			time_avr = time_a/num_runs	
			print('Среднее за ', num_runs, 'повторов время выполнения функции =', time_avr, ' сек.')
		return wrap
	return decorator

# Выполняем функцию fibon_it "num" раз

num = int(input('Введите количество проходов вычисления функции (примерно 10 - 20) '))

@time_this(num)
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