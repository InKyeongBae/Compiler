import sys

#file I/O
f = open(sys.argv[1],'r')
input = f.readlines()
filename = sys.argv[1]
# 일단 txt로 나오게 추후에 out으로 수정
file_out = open(f"{filename.replace('.java', '')}.txt",'w')

# 일단 input 내용 그대로 out으로 나오도록
for inputStr in input :
    print(inputStr)
    print(len(inputStr))
    print("############")
    for i in range(len(inputStr)) :
        print(">>",inputStr[i])
    file_out.write(inputStr + "\n")

def filewrite(file, string):
    # print(string)
    file.write(string+"\n")


f.close()
