from linklistqueue import Queue

class ExpressionTree(object):
	# Builds an expression tree for the expression string.
	def __init__(self, expStr):
		self._expTree = None
		self._buildTree(expStr)
		
	# Evaluates the expression tree and returns the resulting value.
	def evaluate(self, varMap = None):
		return self._evalTree(self._expTree, varMap)
		
	# Returns a string representation of the expression tree.
	def __str__(self):
		return self._buildString(self._expTree)
		
	# Recursively builds a string representation of the expression tree.
	def _buildString(self, treeNode):
		# If the node is a leaf, it's an operand.
		if treeNode.left is None and treeNode.right is None:
			return str(treeNode.data)
		else:	# Otherwise, it's an operator.
			expStr = '('
			expStr += self._buildString(treeNode.left)
			expStr += str(treeNode.data)
			expStr += self._buildString(treeNode.right)
			expStr += ')'
			return expStr
			
	def _evalTree(self, subtree, varDict):
		# See if the node is a leaf node, in which case return its value.
		if subtree.left is None and subtree.right is None:
			# Is the operand a literal digit?
			if subtree.data >= '0' and subtree.data <= '9':
				return int(subtree.data)
			else:	# Or is it a variable?
				assert subtree.data in varDict, 'Invalid variable.'
				return varDict[subtree.data]
				
		# Otherwise, it's an operator that needs to be computed.
		else:
			# Evaluate the expression in the left and right subtrees.
			lvalue = self._evalTree(subtree.left, varDict)
			rvalue = self._evalTree(subtree.right, varDict)
			# Evaluate the operator using a helper method.
			return self._computeOp(lvalue, subtree.data, rvalue)
			
	# Compute the arithmetic operation based on the supplied op string.
	def _computeOp(self, left, op, right):
		return eval(str(left) + str(op) + str(right))
		
	def _buildTree(self, expStr):
		# Build a queue containing the tokens in the expression string.
		expQ = Queue()
		for token in expStr:
			if token != ' ':
				expQ.enqueue(token)
				
		# Create an empty root node.
		self._expTree = _ExpTreeNode(None)
		# Call the recursive function to build the expression tree.
		self._recBuildTree(self._expTree, expQ)
		
	# Recursively builds the tree given an initial root node.
	def _recBuildTree(self, curNode, expQ):
		# Extrate the next token from the queue.
		token = expQ.dequeue()
		
		# See if the token is a left paren: '('
		if token == '(':
			curNode.left = _ExpTreeNode(None)
			self._recBuildTree(curNode.left, expQ)
			
			# The next token will be an operator: + - / * %
			curNode.data = expQ.dequeue()
			curNode.right = _ExpTreeNode(None)
			self._recBuildTree(curNode.right, expQ)
			
			# The next token will be a ), remove it.
			expQ.dequeue()
			
		# Otherwise, the token is a digit that has to be converted to an int.
		else:
			curNode.data = token
	
# Storage class for creating the tree nodes.
class _ExpTreeNode(object):
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None
			