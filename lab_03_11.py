from heapq import heappush as insert, heappop as pop

class Node:
    
    def __init__(self):
        self.value = None
        
    def createDict(self):
        if self.value != None:
            return dict([(self.value, "")])

        _dict = dict()
        if self.left != None:
            _dict_l = self.left.createDict()
            for i in _dict_l.keys():
                _dict_l[i] = '0' + _dict_l[i]
            _dict.update(_dict_l)
        if self.right != None:
            _dict_r = self.right.createDict()
            for i in _dict_r.keys():
                _dict_r[i] = '1' + _dict_r[i]
            _dict.update(_dict_r)
            
        return _dict
        

def encodeHuffman(fileIn, fileOut):
    file_i = open(fileIn, "r")
    txt = file_i.read()
    file_i.close
    symbols = set(txt)

    q = []

    i = 0
    for s in symbols:
        count = list(txt).count(s)
        insert(q, (count, i, s))
        i+=1

    while len(q) != 1:
        left = pop(q)
        right = pop(q)
        
        left_e = None
        right_e = None
        n = Node()
        if not(isinstance(left[-1], Node)):
            left_e = Node()
            left_e.value = left[-1]
        else:
            left_e = left[-1]
        if not(isinstance(right[-1], Node)):
            right_e = Node()
            right_e.value = right[-1]
        else:
            right_e = right[-1]
        
        n.left = left_e
        n.right = right_e
        
        p = left[0]+right[0]
        insert(q, (p, i, n))
        i+=1
    
    _dict = pop(q)[-1].createDict()

    
    file_o = open(fileOut, "w")
    
    for i in _dict.keys():
        file_o.write(str(ord(i)) + " " + _dict[i] + " ")
    
    file_o.write('\n')
    
    encoded = ""
    for s in txt:
        encoded += _dict[s]
        
    file_o.write(encoded)
    
    file_o.close()
    
    print("Deflating by Huffman (without symbols tree): " + str((len(encoded)/(len(txt)*8))*100) + "%")
    
    
def decodeHuffman(fileIn, fileOut):
    file_i = open(fileIn, "r")
    str1 = file_i.readline()
    str2 = file_i.readline()
    file_i.close
    
    a = str1.split(" ")
    
    _dict = dict()
    for i in range(0, len(a), 2):
        if a[i] == '\n':
            continue
        _dict[a[i+1]] = chr(int(a[i]))
    
    s = ""
    start = 0
    stop = 1
    while start < len(str2):
        sl = str2[start:stop]
        if (_dict.get(sl, "") == ""):
            stop += 1
            continue
        else:
            s += _dict.get(sl)
            start = stop
            stop += 1
            
    file_o = open(fileOut, "w")
    file_o.write(s)
    file_o.close()
    
encodeHuffman("text.txt", "text_e_huf.txt")
decodeHuffman("text_e_huf.txt", "text_d_huf.txt")

def bin_l(a, length):
    bin_str = bin(a).replace("0b", "")
    while len(bin_str) != length:
        bin_str = '0' + bin_str
    
    return bin_str
    
def encodeLZW(fileIn, fileOut):
    comb = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", 
    "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", 
    "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", 
    "s", "t", "u", "v", "w", "x", "y", "z", " ", "'", "-", ",", ".", "\n", ";"]
    base_length = 6
    
    file_i = open(fileIn, "r");
    txt = file_i.read()
    file_i.close()

    out = ""

    buff = ""
    for c in range(0, len(txt)):
        buff += txt[c]
        if buff in comb:
            continue
        else:
            comb.append(buff)
            
            out += bin_l(comb.index(buff[:len(buff)-1]), base_length)
            if (c+1) == len(txt):
                out += bin_l(comb.index(txt[c]), base_length)
                break
            buff = buff[-1:]
            
            if len(comb) > 2**base_length:
                base_length += 1
    
    print(comb)
    
    file_o = open(fileOut, "w")
    file_o.write(out)
    file_o.close()
    
    print("Deflating by LZW: " + str((len(out)/(len(txt)*8))*100) + "%")
    
    
def decodeLZW(fileIn, fileOut):
    comb = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", 
    "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", 
    "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", 
    "s", "t", "u", "v", "w", "x", "y", "z", " ", "'", "-", ",", ".", "\n", ";"]
    base_length = 6
    
    file_i = open(fileIn, "r");
    txt = file_i.read()
    file_i.close()
    
    out = ""
    start = 0
    while start < len(txt):
        cur = int(txt[start:start+base_length], 2)
        out += comb[cur]
        
        if start != 0: comb[-1] += comb[cur][0]
        comb.append(comb[cur])
        
        start += base_length
        
        if len(comb) > 2**base_length:
            base_length += 1
            
    file_o = open(fileOut, "w")
    file_o.write(out)
    file_o.close()
    
    print(comb)
    
encodeLZW("text.txt", "text_e.txt")
print("\n")
decodeLZW("text_e.txt", "text_d.txt")