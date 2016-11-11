"""
Author: Derek Leung (dxl3349@rit.edu)
Description: A simple virus scanner that checks all files in a given directory 
for signatures from a given signature file
"""
import os
from os.path import join
from collections import defaultdict

class Scanner:
	def __init__(self, directory, sig_path):
		self.directory = directory
		self.matches = defaultdict(list)
		self.sig_file = self.openFile(sig_path)
		self.sigs = []

		self.getSigs()

	def getSigs(self):
		for sig in self.sig_file:
			self.sigs.append(sig)

	def traverse(self):
		"""
		root - path of top directory
		subdirs - list of subdirectories
		files - list of files
		"""
		for root, subdirs, files in os.walk(self.directory):
			for name in files:
				path = join(root, name)
				file = self.openFile(path)
				for sig in self.sigs:
					if sig in file.read():
						self.matches[path].append(sig)

	def openFile(self, path):
		try:
			file = open(path)
		except IOError:
			print "Error: File does not appear to exist."
			sys.exit(1)
		return file

	def printSigs(self):
		print 'signatures in signature file:'
		print self.sigs
		print ''

	def printMatches(self):
		for k, v in self.matches.iteritems():
			print k, 'contains the following signatures: ', v


if __name__ == '__main__':
	directory = raw_input("Enter directory: ")
	sig_path = raw_input("Enter signature file path: ")
	s = Scanner(directory, sig_path)
	s.printSigs()
	s.traverse()
	s.printMatches()
