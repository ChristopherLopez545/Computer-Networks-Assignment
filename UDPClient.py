from socket import *
from utils import *
from list import linked_list,node
import pickle

serverName = '127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)




##### Define your preparation protocol here!
def prepMsg(sentence):
    words = sentence.split() # splits the sentence into words
    segments = []
    #assign each word with a index ex 0 cat 1 food
    for index, words in enumerate(words):
        segments.append(f"{index}:{words}")
    
    # using picke to turn this into byte like objects 
    pickle_segments = pickle.dumps(segments) 
    return pickle_segments

##### Define your processing protocol for responses here!
def parseResponse(responseList):
    words = pickle.loads(responseList)
    linkedList = linked_list()
    # append each word into the linked list in correct order then put the words
    #together with put_together() method
    print(words) 
    for segment in words:
        if ":" in segment: # when we hit a segment with "!@#$"
            orderNum, word = segment.split(":",1) # spliting the segment   
                                         # ex) 0:cat , orderNum = 0 and word = cat
            linkedList.inorder_Insert(int(orderNum),word)

    # put the message back together
    sentence = linkedList.put_together()                                 
    return sentence

# Load a message from your text file
messages = []
with open('demoMessages.txt', 'r') as f:
    for sentence in f.readlines():
        messages.append(sentence)

message = prepMsg(messages[0]) # Grabs the first message in the demo file, you can change this (0-4)
# message = input('input lowercase: sentence:') # Use this for your own test sentence

clientSocket.sendto(message, (serverName, serverPort))
response, serverAddress = clientSocket.recvfrom(2048)
response = parseResponse(response)
print(response)
demoAccuracy(messages[0], response) # Testing one sentence from the demo


# TESTING BLOCK (Once you are done with your checking algorithm)
# set done to True once you're ready!
done = True
if done:
    tests = []
    total = 0
    with open('testMessages.txt', 'r') as f:
        for sentence in f.readlines():
            clientSocket.sendto(prepMsg(sentence), (serverName, serverPort))
            response, _ = clientSocket.recvfrom(2048)
            response = parseResponse(response)
            total += testAccuracy(sentence, response)
        print(f'Your test score is: {total}%!')

clientSocket.close()