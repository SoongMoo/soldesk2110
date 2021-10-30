# mod1.py
PI = 3.141592

def sum(num1, num2):
	result = num1 + num2
	return result

class FourCal1:
	def __init__(self, num1, num2): 
		self.first = num1
		self.second = num2
		print("객체 생성시 자동으로 실행") # 추가
	def add(self):
		self.result = self.first + self.second
		return self.result
	def sub(self):
		self.result = self.first - self.second
		return self.result
	def mul(self):
		self.result = self.first * self.second
		return self.result
	def div(self):
		self.result = self.first / self.second
		return self.result
dddd = FourCal1(30, 20)