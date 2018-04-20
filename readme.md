# Mossad Challenge

## Level 0:
### Parsing:
In order to extract the brainfuck code from the image I used tesseract:
```
tesseract level0_right.png stdout > level0_right.txt
tesseract level0_left.png stdout > level0_left.txt
```

### Processing:
Before running the code I had to replace the '—' character with '-':
```
sed -i -e 's/—/-/g' level0_right.txt
sed -i -e 's/—/-/g' level0_left.txt
```

### Running:
In order to run the brainfuck code I have used https://copy.sh/brainfuck/.

The out of the script in level_left.txt is:
xor-with-key

After running the script from level0_right.txt i got no output.
When looked into the memory dump there was the following data:
```
0000:  7A  46  5C  53  55  59  03  5A  41  03  06  01  zF\SUY.ZA...
```

### Solution:
To solve this all we need to do is find the key.
After some guesses I found out that the key is:
```
Israel-is-70
```
The result of XORing the memory and the key is:
```
35.205.32.11
```
