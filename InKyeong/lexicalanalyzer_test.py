import sys

#file I/O
f = open(sys.argv[1],'r')
input = f.readlines()
filename = sys.argv[1]
# 일단 txt로 나오게 추후에 out으로 수정
file_out = open(f"{filename.replace('.java', '')}.txt",'w')

# 일단 input 내용 그대로 out으로 나오도록
for input in input :
    file_out.write(input + "\n")

def filewrite(file, string):
    print(string)
    file.write(string+"\n")


f.close()

