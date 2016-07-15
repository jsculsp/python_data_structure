# Implements the Edit Buffer ADT using a doubly linked list of vectors.
class EditBuffer(object):
	# Constructs an edit buffer containing one empty line of text.
	def __init__(self):
		self._firstLine = _EditBufferNode(['\n'])
		self._lastLine = self._firstLine
		self._curLine = self._firstLine
		self._curLineNdx = 0
		self._curColNdx = 0
		self._numLines = 1
		self._insertMode = True
		
	# Returns the number of lines in the buffer.
	def numLines(self):
		return self._numLines
	
	# Returns the number of characters in the current line.
	def numChars(self):
		return len(self._curLine.text)
		
	# Returns the index of the current row.(first row has index 0)
	def lineIndex(self):
		return self._curLineNdx
		
	# Returns the index of the current column (first col has index 0).
	def columnIndex(self):
		return self._curColNdx
		
	# Sets the entry mode based on the boolean value insert.
	def setEntryMode(self, insert = True):
		self._insertMode = insert
		
	# Toggles the entry mode insert and overwrite.
	def toggleEntryMode(self):
		self._insertMode = not self._insertMode
		
	# Returns True if the current entry mode is insert.
	def inInsertMode(self):
		return self._insertMode == True
		
	# Returns the character at the current cursor position.
	def getChar(self):
		return self._curLine.text[self._curColNdx]
		
	# Returns the current line as a string.
	def getLine(self):
		lineStr = ''
		for char in self._curLine.text:
			lineStr += char
		return lineStr
		
	# Moves the cursor up num lines.
	def moveUp(self, nlines = 1):
		if nlines <= 0:
			return None
		elif self._curLineNdx - nlines < 0:
			nlines = _curLineNdx
			
		for i in range(nlines):
			self._curLine = self._curLine.prev
		
		self._curLineNdx -= nlines
		if self._curColNdx >= self.numChars():
			self.moveLineEnd()
	
	# Moves the cursor down num lines.
	def moveDown(self, nlines = 1):	
		if nlines <= 0:
			return None
		elif self.numLines() <= self._curLineNdx + nlines:
			nlines = self.numLines() - self._curLineNdx
			
		for i in range(nlines):
			self._curLine = self._curLine.next
			
		self._curLineNdx += nlines
		if self._curColNdx >= self.numChars():
			self.moveLineEnd()
	
	# Moves the cursor to the document's home position.
	def moveDocHome(self):
		self._curLine = self._firstLine
		self._curLineNdx = 0
		self._curColNdx = 0
		
	# Moves the cursor to the document's end position, which is the
	# last line and first character position in that line.
	def moveDocEnd(self):
		self._curLine = self._lastLine
		self._curLineNdx = self.numLines() - 1
		self._curColNdx = 0
	
	# Moves the cursor to the left one position.
	def moveLeft(self):
		if self._curColNdx == 0:
			if self._curLineNdx > 0:
				self.moveUp(1)
				self.moveLineEnd()
		else:
			self._curColNdx -= 1
			
	# Moves the cursor to the right one position.
	def moveRight(self):
		if self._curColNdx == self.numChars() - 1:
			if self._curLineNdx < self.numLines() - 1:
				self.moveDown(1)
				self.moveLineHome()
		else:
			self._curColNdx += 1
	
	# Moves the cursor to the front of the current line.
	def moveLineHome(self):
		self._curColNdx = 0
		
	# Moves the cursor to the end of the current line.
	def moveLineEnd(self):
		self._curColNdx = self.numChars() - 1
		
	# Starts a new line at the cursor position.
	def breakLine(self):
		# Save the text following the cursor position.
		nlContents = self._curLine.text[self._curColNdx:]
		# Insert newline character and truncate the line.
		del self._curLine.text[self._curColNdx:]
		self._curLine.text.append('\n')
		# Insert the new line and increment the line counter.
		self._insertNode(self._curLine, nlContents)
		# Move the cursor.
		self._curLine = self._curLine.next
		self._curLineNdx += 1
		self._curColNdx = 0
	
	# Removes the entire line containing the cursor.
	def deleteLine(self):
		if self._curLine is self._lastLine:
			self._curLine = self._curLine.prev
			self._removeNode(self._curLine.next)
			self._curLineNdx -= 1
			self._curColNdx = 0
		else:
			self._curLine = self._curLine.next
			self._removeNode(self._curLine.prev)
			self._curColNdx = 0
		
	# Removes all of the characters at the end of the current line
	# starting at the cursor position.
	def truncateLine(self):
		# Insert newline character and truncate the line.
		del self._curLine.text[self._curColNdx:]
		self._curLine.text.append('\n')
		self.moveLineEnd
		
	# Inserts the given character into the buffer at the current position.
	def addChar(self, char):
		if char == '\n':
			self.breakLine()
		else:
			ndx = self._curColNdx
			if self.inInsertMode():
				self._curLine.text.insert(ndx, char)
			else:
				if self.getChar() == '\n':
					self._curLine.text.insert(ndx, char)
				else:
					self._curLine.text[ndx] = char
			self._curColNdx += 1
		
	# Removes the character at the current position and leaves the cursor 
	# at the same position.
	def deleteChar(self):
		if self.getChar() != '\n':
			self._curLine.text.pop(self._curColNdx)
		else:
			if self._curLine is self._lastLine:
				return None
			else:
				nextLine = self._curLine.next
				self._curLine.text.pop()
				self._curLine.text.extend(nextLine.text)
				self._removeNode(nextLine)
		
	# Removes the character preceding the current position and 
	# moves the cursor left one position.
	def ruboutChar(self):
		if self._curColNdx != 0:
			self._curLine.text.pop(self._curColNdx - 1)
			self._curColNdx -= 1
		else:
			if self._curLine is self._firstLine:
				return None
			else:
				prevLine = self._curLine.prev
				prevLine.text.pop()
				self._curColNdx = len(self._prevLine.text) - 1
				prevLine.text.extend(self._curLine.text)
				self._curLine = prevLine
				self._removeNode(self._curLine.next)
		
	# Deletes the entire contents of the buffer and resets it to 
	# the same state as in the constructor.
	def deleteAll(self):
		self.__init__()
	
	# Inserts a new node following the one pointed to by _curLine and 
	# containing the supplied contents.
	def _insertNode(curLine, nlContents):
		newLine = _EditBufferNode(nlContents)
		if curLine.next is None:
			newLine.prev = curLine
			curLine.next = newLine
		else:
			newLine.prev = curLine
			newLine.next = curLine.next
			curLine.next.prev = newLine
			curLine.next = newLine
		self._numLines += 1
		
	def _removeNode(line_to_remove):
		if line_to_remove.prev is not None and line_to_remove.next is not None:
			line_to_remove.prev.next = line_to_remove.next
			line_to_remove.next.prev = line_to_remove.prev
		elif line_to_remove.prev is not None and line_to_remove.next is None:
			line_to_remove.prev.next = None
		elif line_to_remove.prev is None and line_to_remove.next is not None:
			line_to_remove.next.prev = None
		self._numLines -= 1
		
# Define a private storage class for creating the list nodes.
class _EditBufferNode(object):
	def __init__(self, text):
		self.text = text
		self.prev = None
		self.next = None