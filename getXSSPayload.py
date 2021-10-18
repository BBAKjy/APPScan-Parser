from bs4 import BeautifulSoup
import html as htmlParser

f = open("INPUT FILE", 'r', encoding='UTF8')

html = f.read()

target = 'Reflected Cross Site Scripting'
index = -1
indexes = []

while True:
    index = html.find(target, index + 1)
    if index == -1:
        break
    indexes.append(index)

    #print(html[index:])

indexes = indexes[5:-2]

#print(indexes)

for i in range(len(indexes)-1):
    #print(indexes[i], indexes[i+1])
    fragment = html[indexes[i]:indexes[i+1]]
    #print(fragment)

    ahref = fragment.find('<a href="')
    gt = fragment.find('">', ahref+9)
    url = fragment[ahref+9:gt]
    
    a = url.find("/") + 1
    #print(a, url[a:])
    b = url[a:].find("/") + a + 1
    #print(b, url[b:])
    c = url[b:].find("/") + b + 1
    #print(c)
    url = url[:c - 1]
    
    begin = fragment.find("GET")

    if begin == -1:
        begin = fragment.find("POST")
        print('\n\nPOST')

    end = fragment.find("HTTP/1.1")
    path = htmlParser.unescape(fragment[begin:end].replace('<span class="mark">', '').replace('</span>', ''))[htmlParser.unescape(fragment[begin:end].replace('<span class="mark">', '').replace('</span>', '')).find(" ")+1:]

    #print(url)
    #print(path)
    result = url+path

    #if "/penta/sso" not in result:
    print(url+path)



# rxss1 = html[html.find("Reflected Cross Site Scripting"):]
# rxss2 = print(html.find("Reflected Cross Site Scripting", rxss1))

# lines = f.readlines()

# #print(lines)

# for i in range(len(lines)):
#     if('Reflected Cross Site Scripting' in lines[i]):
#         print(lines[i])