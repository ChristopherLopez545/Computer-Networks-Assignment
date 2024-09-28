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
    # Load the pickled response
    words = pickle.loads(responseList)

    # Check if the loaded data is actually a list
    if not isinstance(words, list):
        raise ValueError("Expected response to be a list.")

    linkedList = linked_list()  # Assuming you have a linked list implementation

    # Print the received words for debugging
    print("Received words:", words)  # Debugging line
    
    # Process each segment
    for segment in words:
        # Check if the segment is a string and contains ":"
        if isinstance(segment, str) and ":" in segment:
            orderNum, word = segment.split(":", 1)  # Split the segment

            # Handle corrupted segments
            if word == "!@#$":
                linkedList.inorder_Insert(int(orderNum), None)  # Insert None for corrupted segment
            else:
                linkedList.inorder_Insert(int(orderNum), word)  # Insert the valid word

    # Assemble the full message
    sentence = linkedList.put_together() 
    
    # Debugging output to see the final constructed sentence
    print("Constructed sentence:", sentence)

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