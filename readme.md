# Mossad Challenge

## Level 0:

### Parsing:
tesseract level0\_right.png stdout > level0\_right.txt
tesseract level0\_left.png stdout > level0\_left.txt

### Processing:
sed -i -e 's/—/-/g' level0\_right.txt
sed -i -e 's/—/-/g' level0\_left.txt

### Running:
In order to run the brainfuck code I have used https://copy.sh/brainfuck/.

The out of the script in level\_left.txt is:
xor-with-key

After running the script from level0\_right.txt i got no output.
When looked into the memory dump there was the following data:
0000:  7A  46  5C  53  55  59  03  5A  41  03  06  01  zF\SUY.ZA...

