import os

f1 = open("../result/conversation", "a")
f2 = open("../result/conversation_2", "r")

f1.write(f2.read())

f2.close()
f1.close()
os.remove("../result/conversation_2")
