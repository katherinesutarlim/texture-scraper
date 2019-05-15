import requests
import urllib.request


# Made to download all textures from Cadhatch. There are 3 pages
# with different html lines, so the same steps are repeated for
# each page.


# FABRIC
# PAGE 1
file = urllib.request.urlopen("http://www.cadhatch.com/seamless-fabric-textures/4588167781")
page1_bytes = file.read()

page1 = page1_bytes.decode("utf8")
file.close()

# Writes the html to a file, used to determine line numbers
# with open('html.txt','w') as f:
#             f.write(page1)


page1_lines = page1.split('\n')[918:979]

for line in page1_lines:
    if (line[1] != '/'):
        end = line.find('" target="_self" ><img')
        url = "http://www.cadhatch.com"+line[9:end]
        filename = line[9+44:end]        
        r = requests.get(url)
        with open("Cadhatch Fabric/"+filename, 'wb') as f:
            f.write(r.content)


# WOOD
# PAGE 1
file = urllib.request.urlopen("http://www.cadhatch.com/seamless-wood-textures/4588167771")
page1_bytes = file.read()

page1 = page1_bytes.decode("utf8")
file.close()

page1_lines = page1.split('\n')[1075:1158]

for line in page1_lines:
    if (line[1] != '/'):
        end = line.find('" target="_self" ><img')
        url = "http://www.cadhatch.com"+line[9:end]
        filename = line[9+44:end]
        r = requests.get(url)
        with open("Cadhatch Wood/"+filename, 'wb') as f:
            f.write(r.content)


# PAGE 2
file = urllib.request.urlopen("http://www.cadhatch.com/wood-textures-page-2/4588437917")
page2_bytes = file.read()

page2 = page2_bytes.decode("utf8")
file.close()

page2_lines = page2.split('\n')[837:870]

for line in page2_lines:
    if (line[1] != '/'):
        end = line.find('" target="_self" ><img')
        url = "http://www.cadhatch.com"+line[9:end]
        filename = line[9+44:end]
        r = requests.get(url)
        with open("Cadhatch Wood/"+filename, 'wb') as f:
            f.write(r.content)


# Made thanks to these posts:
# https://stackoverflow.com/questions/24153519/how-to-read-html-from-a-url-in-python-3
# https://stackoverflow.com/questions/14652080/receive-attachment-with-urllib-python
