# reading a file
with open("artifacts01.txt",'r') as f:
    text = f.read()
print(text)
print('stage 2 has completed')