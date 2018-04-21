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

After running the script from level0_right.txt I got no output.\
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

## Level 1:
**Disclaimer: This level was not solve by me**

Our goal is to get the administration page <http://35.205.32.11/administration>.\

### Research results:
* The login request is sent in the following format:\
`http://35.205.32.11/login.php?user_name={username}&password={password}`
* The site downloads a picture from the url that we give in the registration page (`http://35.205.32.11/register`) into a folder named `profilePics`.\
We can cause the server to download any page by sending a request in the following format:\
`http://35.205.32.11/testProfilePng?u={processed URL}`.\
Because the server wants to download only pictures it checks every URL for the `.png` ending.
We can bypass this check by appending `%00.png` to the URL.
Also the URL (with to .png extension) is sent to server in base64.\
So if we want to cause the server to download the page `www.google.com` we need to do the following:
    1. Add %00.png ending. (Resulting `www.google.com%00.png`).
    2. Encode in base64. (Resulting `d3d3Lmdvb2dsZS5jb20lMDAucG5n`)
    3. Sending a request to `http://35.205.32.11/testProfilePng?u=d3d3Lmdvb2dsZS5jb20lMDAucG5n`.
* From the HTTP headers we know that the server runs on Apache.

### Exploiting:
1. Because the server run on Apache if you login from the localhost to the admin account a password is not needed.\
In order to login to the admin account the server have to browse to: `http://35.205.32.11/login.php?user_name=admin`.\
So we send a request to the following URL:\
<http://35.205.32.11/testProfilePng?u=aHR0cDovLzM1LjIwNS4zMi4xMS9sb2dpbi5waHA/dXNlcl9uYW1lPWFkbWluJTAwLnBuZw==>\
This will cause the server to browse with a cookie which is associated with the admin session.
2. Next we need to cause the server to download the administration page (`http://35.205.32.11/administration`).\
So we send a request to the following URL:
<http://35.205.32.11/testProfilePng?u=aHR0cDovLzM1LjIwNS4zMi4xMS9hZG1pbmlzdHJhdGlvbiUwMC5wbmc==>\
This will download the administration page to the `profilePics` folder.
3. To view the administration page we simply request <http://35.205.32.11/profilePics/administration>.
4. In the administration page we will find a link the the next challenge: <http://35.205.32.11/ch1_success>.

## Level 2:
At the start of level 2 we get an [unknown file](level_2/451d79109ac842ef92217932c0567761).\
We can figure out that this is a zip file by using [binwalk](https://github.com/ReFirmLabs/binwalk) or by recognizing the magic PK at the beginning of the file.  
After extracting the content from the zip we need to examine the [pcap](level_2/pcap.pcap) file.

After examining the tcp streams in the pcap file we can see that there is a connection to 35.204.90.89 over port 5555.\
In this connection the server sends a string that looks like md5 as a challenge, and receives a response that looks like sha512.
I noticed that when reversing the md5 and the sha512 it resulted in two adjacent numbers.\
So for the a given challenge the response would be the sha512 of the md5 reverse + 1.\
I have created a [python script](level_2/level2.py) which does the following:
1. Connects to the server
2. Receives the challenge
3. Reverses the md5 (challenge == md5)
4. Calculates the response by hashing using sha512 the reverse of the md5 + 1
5. Sends the response
6. Receives the authorization message
