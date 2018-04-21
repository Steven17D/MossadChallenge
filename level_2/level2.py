import hashlib
import time
import socket
from itertools import count


IP = '35.204.90.89'
PORT = 5555
MD5_LENGTH = 32


def reverse_md5(md5_hash):
    for solution in count():
        md5_object = hashlib.md5()
        md5_object.update(str(solution))
        if md5_object.hexdigest() == md5_hash:
            return solution


def main():
    # Connect to the server
    sock = socket.socket()
    sock.connect((IP, PORT))

    # Receive the challenge
    md5_challenge = sock.recv(MD5_LENGTH)
    md5_solution = reverse_md5(md5_challenge)
    print md5_challenge
    sha512_object = hashlib.sha512()
    sha512_object.update(str(md5_solution + 1))
    challenge_solution = sha512_object.hexdigest()
    print challenge_solution

    # Send the solution
    sock.send(challenge_solution)
    # Receive the authorization message
    time.sleep(1)
    print sock.recv(1024)
    sock.close()


if __name__ == '__main__':
    main()
