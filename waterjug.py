
class waterjug:

	def __init__(self, m ,n ,q) -> None:
			self.m = m
			self.n = n
			self.q = q
			self.list = [(0,0)]
			
			g = self.gcd(self.m, self.n)

			if q % g == 0:
				
				self.solution()
			
			else:
				
				print('problem not solvable')
			

	def gcd(self, a, b):

			while b:
					a, b = b, a % b
			return a

	def solution(self):
		
			self.jug_m = 0
			self.jug_n = 0

		
			smallestVolume = min(self.m, self.n)
			
			maximumVolume = max(self.m, self.n)
			
			self.jug_n = smallestVolume

			self.list.append((self.jug_m, smallestVolume))
			

			count = 0 

			while(True):
				

				
				if self.jug_m == maximumVolume:

					self.jug_m = 0
					self.list.append((self.jug_m, self.jug_n))

					self.jug_m += self.jug_n
					self.jug_n = 0 
					self.list.append((self.jug_m, self.jug_n))

					self.jug_n = smallestVolume
					self.list.append((self.jug_m, self.jug_n))

				else:

					self.rq = maximumVolume - self.jug_m
					
					if self.rq >= self.jug_n:
						
						self.jug_m += self.jug_n
						self.jug_n = 0
						self.list.append((self.jug_m, self.jug_n))
						self.jug_n = smallestVolume
						self.list.append((self.jug_m, self.jug_n))

					else:

						self.jug_m = maximumVolume
						self.jug_n -= self.rq
						self.list.append((self.jug_m, self.jug_n))
				
				
				if self.jug_m == self.q or self.jug_n == self.q:
					break
				else:
					pass
			
			print(self.list)
			
# w = waterjug(9,6,7)
w = waterjug(7,13,8)