import datetime as date
import hashlib as hasher
import random
from collections import defaultdict 
#16 bytes
global GenesisAdd
global NodeNumber
NodeNumber = 0
address = defaultdict(list)
class GenesisNode:
	def __init__(self):
		self.data = None
		self.parent = None
		self.referenceID = self.node_id()
		self.children = []
 
	def node_id(self):
		return (''.join(random.choice('0123456789ABCDEF') for i in range(32)))
		
class Block:
	def __init__(self,owner_id=None,value=None,owner_name=None,referenceID=None,childreferences=None,NodeID=None):
		
		if(owner_id==None):		
			self.value = None
			self.head = "shiva"
			self.nodeNumber = NodeNumber
			self.NodeID = self.node_id()
			

		else:
			self.parent = None	
			self.nodeNumber = NodeNumber	
			self.nodeNumber = self.nodeNumber + 1
			self.NodeID = NodeID
			self.referenceID = referenceID
			self.timestamp = date.datetime.now()
			self.data = self.hashfunc(owner_id,value,owner_name)
	
	def hashfunc(self,owner_id,value,owner_name):
		sha = hasher.sha256()
		sha.update((str(owner_id)+str(value)+str(owner_name)).encode('utf-8'))
		return sha.hexdigest()

	def node_id(self):
		return (''.join(random.choice('0123456789ABCDEF') for i in range(32)))		


	def addToGen(self,owner_id,value,owner_name,GenesisAdd,child):
		NodeID = self.node_id()
		sum1 = 0 
		block = Block(owner_id,value,owner_name,GenesisAdd,NodeID)
		address[GenesisAdd].insert(0,[NodeID,value,owner_id,owner_name])
		return block
		'''for i in address[GenesisAdd]:
			sum1 += i[1]
		if(sum1<value):
			block = Block(owner_id,value,owner_name,GenesisAdd,NodeID)
			address[GenesisAdd].insert(0,[NodeID,value,owner_id,owner_name])
			return block
		else:
			print("VAlue IS InCorrent For This Node")
			return "error"'''
		

input1 = "1"
lastNodeAdd = "shivam"

while(input1 == "1" or input1 == "2" or input1 == "3" or input1 == "4" or input1 == "5" or input1 == "6"):
	input1 = str(input('''Select operation you want to perform
	1.. Create Genesis Node that has parent Node has null
	2.. Create Set Of Child Nodes
	3.. Verify The Owner Of the Node
	4.. Edit Values of Node
	5.. Transfer Owner Ship of the node
	6.. Find Longest Chain from Genesis \n
'''))	
	
	block = Block()
	if(input1=="1"):
		block = Block()
		GenesisAdd = block.NodeID
		lastNodeAdd = GenesisAdd
		print("Genesis Node is Created with reference ID "+ GenesisAdd)
	if(input1=="2"):
		if(block.head == None):
			print("No Genesis Node Found")
		elif(lastNodeAdd==GenesisAdd):
			print("Node number "+ str(NodeNumber+1)+"\n")
			owner_id = str(input("Enter Owner Id\n"))
			owner_name = str(input("Enter Owner Name\n"))
			print("Enter Value")
			value = int(input())
			re = block.addToGen(owner_id,value,owner_name,GenesisAdd,[])
			if(re=="error"):
				print("Value is incorrect")
			else:
				lastNodeAdd = re.NodeID
			
		else:
			print("Which Node You Want To Add Childeren from the Following")
			count = 0
			for key, value in address.items():
				count = count +1
				print(str(count)+"... "+str(key))
			print("Enter New Node Details\nEnter Node ID")
			enter = str(input())
			owner_id = str(input("Enter Owner Id\n"))
			owner_name = str(input("Enter Owner Name\n"))
			print("Enter Value")
			value = int(input())
			re = block.addToGen(owner_id,value,owner_name,enter,[])
			if(re=="error"):
				print("Value is incorrect")
			else:
				lastNodeAdd = re.NodeID

	if(input1=="3"):
		print("VErify Owner Of the Nodes")
		for key, value in address.items():
				count = count +1
				print(str(count)+"... "+str(key))
		print("Enter Node Id you Want To check For")
		enter = str(input())
		print("Enter Owner ID")
		owner = str(input())
		if(address[enter][2]==owner):
			print("Owner is Verified")
		else:
			print("This Is not owner of the selected node")
	if(input1=="4"):
		print("Edit Value Of Nodes")
		for key, value in address.items():
				count = count +1
				print(str(count)+"... "+str(key)+str(value[2]))
		print("Enter Node Id you Want To edit Value  For")
		enter = str(input())
		print("Enter Owner ID")
		value = str(input())
		address[enter][1]==value
		print("Values Changed")
	if(input1=="5"):
		print("Transfer Owner")
		for key, value in address.items():
				count = count +1
				print(str(count)+"... "+str(key)+str(value[2]))
		print("Enter Node Id you Want To edit Value  For")
		enter = str(input())
		print("Enter Owner details")
		owner_id = str(input("Enter Owner Id\n"))
		owner_name = str(input("Enter Owner Name\n"))
		address[enter][2]==owner_id
		address[enter][3]==owner_name
		print("Owner Changed")
	
	if(input1=="6"):
		#here i have to implement Dijakstra
		print("Longest Chain From Genesis")
		maxlen =0
		max_index = ""
		for key, value in address.items():
			if(len(value)>maxlen):
				maxlen = len(value)
				max_index = key
		for i in address[key]:
			print(i[0])
			

				
			
			
			
		
		
			
		

		
	


