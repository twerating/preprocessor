from gensim.models import Word2Vec
from preprocess import preprocess
from genTokenList import form_token_list
import os
from genVector import *
from subprocess import call
from threading import Thread
import scipy.io as sio
import numpy as np
# import queue
from multiprocessing import Queue

def chunck(l, n):
	tweet_list = []
	for i in xrange(0, len(l), n):
		yield l[i:i+n]

train_folder = '../dataCollection/2000train'
test_folder = '../dataCollection/2000test'

def file2vec(filename, folder):
	tweets = preprocess(open(folder + '/' + filename).read().replace('\n', ' '))
	return tweets

def getRawTrain():
	token_list = import_token_list()
	trainMatrix = []
	trainLabel = []
	cnt = 0
	for filename in os.listdir(train_folder):
		if filename[0] == '.':
			continue
		cnt += 1
		print cnt
		rating = filename[0]
		tweets = file2vec(filename, train_folder)
		token_dict = form_token_dict(tweets)	
		trainMatrix.append(gen_vector(token_dict, token_list))
		trainLabel.append([int(rating)])	

	sio.savemat("rawData/RawTrain2000-300.mat", {'trainMatrix':trainMatrix, 'trainLabel':trainLabel})

def getRawTest():
	token_list = import_token_list()
	testMatrix = []
	testLabel = []
	cnt = 0
	for filename in os.listdir(test_folder):
		if filename[0] == '.':
			continue
		cnt += 1
		print cnt
		rating = filename[0]
		tweets = file2vec(filename, test_folder)
		token_dict = form_token_dict(tweets)	
		testMatrix.append(gen_vector(token_dict, token_list))
		testLabel.append([int(rating)])	
	sio.savemat("rawData/RawTest2000-300.mat", {'testMatrix':testMatrix, 'testLabel':testLabel})


def main():
	getRawTrain()
	getRawTest()

if __name__ == '__main__':
	main()