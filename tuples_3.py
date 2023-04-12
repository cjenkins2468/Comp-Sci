import urllib.request
import xarray as xr
import io

url = ('https://gist.githubusercontent.com/henry7720/429604fe4eb16bea0256a4f8f6330746/raw/b01607aedc62970a0f126a5dbf767bba89ed3469/the-full-bee-movie-script.txt')
point = urllib.request.urlopen(url)
word = {}
data = str(point.read())
words = data.split()
for single_word in words:
    character = (single_word[0]).split()
    character = str(character)
    word[character] = word.get(character, 0) + 1
lst = []
for key, value in word.items():
    lst.append((key,value))
lst.sort(reverse=False)
print(lst)
percent_total = 0
for t in lst:
    add = int(t[1])
    percent_total = (percent_total + add)
thing = "%"
for t in lst:
    pct = (t[1]/percent_total) * 100

    print(t[0],thing,pct)
    


''' 
characters = words.split()
word[characters] = word.get(characters, 0) + 1
lst = []
for key, value in word.items():
    print(key)
    lst.append((key,value))
#lst.sort(reverse=False)
#print(lst)
#for t in lst:
 #   print(t[0], t[1])

#with urllib.request.urlopen(point) as text:
    #words = text.read()
    #print(words)
    #ds = xr.open_dataset(io.BytesIO(text.read()))
'''