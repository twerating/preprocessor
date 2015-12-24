from gensim.models import Word2Vec
from preprocess import preprocess
from genTokenList import form_token_list
import os
from genVector import *
from subprocess import call
from threading import Thread
import scipy.io as sio
import numpy as np
from multiprocessing import Queue

# train_folder = '../dataCollection/newTweets'
# test_folder = '../dataCollection/newTestTweets'

train_folder = '../dataCollection/2000train'
test_folder = '../dataCollection/2000test'

def file2vec(filename, folder):
	rating = filename[0]
	tweets = preprocess(open(folder + '/' + filename).read().replace('\n', ' '))
	return tweets


def doc2Vec(vec_size, sentence, model):
	sum_vec = [0] * vec_size
	for word in sentence:
		try:
			word_vec = model[word]
			sum_vec = [x + y for x, y in zip(sum_vec, word_vec)]
		except Exception, e:
			pass
	return [x/len(sum_vec) for x in sum_vec]


def genMatlabData():	
	train_tweets = []
	test_tweets = []
	trainLabel = []
	testLabel = []

	cnt = 0
	train_out_file = open('train2000-150.txt', 'w')
	for filename in os.listdir(train_folder):
		print filename
		if filename[0] == '.':
			continue
		cnt += 1 
		print cnt
		try:
			tweets = file2vec(filename, train_folder)
			wr_line = ' '.join(tweets)
			rating = filename[0]
			
			train_out_file.write(rating + wr_line + '\n')
			trainLabel.append([int(rating)])
			train_tweets.append(tweets)
		except:
			continue;
	print "get vocab done"
	# print train_tweets

	test_out_file = open('test2000-150.txt', 'w')
	for filename in os.listdir(test_folder):
		print filename	
		if filename[0] == '.':
			continue
		cnt += 1	
		print cnt
		try:
			tweets = file2vec(filename, test_folder)
			wr_line = ' '.join(tweets)
			rating = filename[0]
			test_out_file.write(rating + wr_line + '\n')
			testLabel.append([int(rating)])
			test_tweets.append(tweets)
		except:
			continue

	W2Vsentences = []
	W2Vsentences.extend(train_tweets) 
	W2Vsentences.extend(test_tweets)
	model = Word2Vec(W2Vsentences, size = 150, window = 5, min_count = 15, workers = 6)
	model.save('W2VModel2000-150')
	print "w2v done"

	# model = Word2Vec.load('W2VModel2000')
	trainMatrix = []
	print len(train_tweets)
	for tweets in train_tweets:
		trainMatrix.append(doc2Vec(150, tweets, model))

	print len(test_tweets)
	testMatrix = []
	for tweets in test_tweets:
		testMatrix.append(doc2Vec(150, tweets, model))


	sio.savemat("W2Vtrain2000-150.mat", {'trainMatrix':trainMatrix, 'trainLabel':trainLabel})
	sio.savemat("W2Vtest2000-150.mat", {'testMatrix':testMatrix, 'testLabel':testLabel})




def main():
	genMatlabData()


if __name__ == '__main__':
	main()