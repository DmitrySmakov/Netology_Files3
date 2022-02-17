import os
import operator

def join_files(dir):
    os.chdir(dir) # './txt'
    if os.path.isfile('.DS_Store'):
        os.remove('.DS_Store')
    if os.path.isfile('output.txt'):
        os.remove('output.txt')
    list_dir = os.listdir()
    # print(list_dir)
    file_len = {}
    for fn in list_dir:
        # print(fn)
        f = open(fn,"r",encoding="utf-8")
        file_len[fn] = len(f.readlines())
        f.close()
    # print(file_len)
    file_len = (sorted(file_len.items(), key=operator.itemgetter(1)))
    # file_len = (sorted(file_len.items(), key=lambda x: x[1]))
    # print(file_len)
    output = open('output.txt',"w")
    for fn in file_len:  # [('4.txt', 1), ('output.txt', 1), ('2.txt', 2), ('1.txt', 3), ('3.txt', 4)]
        with open(fn[0],"r",encoding="utf-8") as f:
            output.write(fn[0]+'\n')
            output.write(str(fn[1])+'\n')
            for str1 in f:
              output.write(str1)
            output.write('\n')
    output.close()
    return

if __name__ == '__main__':
    join_files('./txt')