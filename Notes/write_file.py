
#this only work in jupiter note book
#this is sudo code here

%%writefile my_new_file.txt
ONE ON FIRST
TWO ON SECOND
THREE ON THIRD

with open('my_new_file', mode='r') as f:
    print(f.read())
