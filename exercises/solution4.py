# Some imports (for 4_D)
import random
import time


## 4_A
class Pump:
	def __init__(self, device_id, connection = []):
		self.device_id = device_id
		self.connection = connection

	def run_cmd(self, command):
		'''
			Template: /device_id/command/s
		'''
		cmd = '/{}/{}/end'.format(self.device_id, command)
		
		# Send over connection (append to connection list)
		self.connection.append(cmd)

	def calibrate(self):
		self.run_cmd('CALIBRATE')

	def inject(self):
		self.run_cmd('INJECT')

	def withdraw(self):
		self.run_cmd('WITHDRAW')

	def stop(self):
		self.run_cmd('STOP')

	def valve_in(self):
		self.run_cmd('VIN')

	def valve_out(self):
		self.run_cmd('VOUT')




## 4_B
conn = []
oil = Pump('A', conn)
water = Pump('B', conn)

# 1. Calibrate both pumps
oil.calibrate()
water.calibrate()
# 2. Switch both pumps to valve in and withdraw, to fill syringes
oil.valve_in()
oil.withdraw()
water.valve_in()
water.withdraw()
# 3. Start by filling the chip with oil (switch valve to out and inject)
oil.valve_out()
oil.inject()
# 4. Now start injecting water to produce droplets
water.valve_out()
water.inject()
# 5. You blew your chip up: STOP BOTH PUMPS!
oil.stop()
water.stop()
# 6. Empty both pumps through the input (to save some of the precious precursors)
oil.valve_in()
oil.inject()
water.valve_in()
water.inject()

# print conn




## 4_C
class BetterPump:
	def __init__(self, device_id, connection = []):
		self.device_id = device_id
		self.connection = connection

	def run_cmd(self, command):
		'''
			Template: /device_id/command/s
		'''
		cmd = '/{}/{}/end'.format(self.device_id, command)
		
		# Send over connection (append to connection list)
		self.connection.append(cmd)

	def valve(self, status=True):
		if status:
			self.run_cmd('VIN')
		else:
			self.run_cmd('VOUT')

	def pump(self, status=True):
		if status:
			self.run_cmd('INJECT')
		else:
			self.run_cmd('WITHDRAW')

conn = []
p = BetterPump('A', conn)
p.pump(False)
p.pump(True)
p.valve()
p.valve(False)
# print conn




## 4_D
for i in range(50):
	valves = [random.randrange(4) for i in range(2)]
	# print valves
	# time.sleep(0.5)