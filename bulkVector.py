import os
from threading import Thread
from subprocess import call

def getVector(in_file_name):
    out_file_name = in_file_name.replace('.txt', '.out')
    in_file_path = './testTweets/' + in_file_name
    out_file_path = './testVectors/' + out_file_name
    call(["python", "genVector.py", in_file_path, out_file_path, "token_list.txt"])

def main():
    thread_list = []
    for file in os.listdir("./testTweets"):
        if file.endswith(".txt"):
            t = Thread(target=getVector, args=[file])
            thread_list.append(t)
            t.start()
            print "start convert {}".format(file)

    for t in thread_list:
        t.join()

    print "Done"

if __name__ == "__main__":
    main()
