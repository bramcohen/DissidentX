DissidentX is a censorship resistance tool.

It has the capability of steganographically encoding messages in
files. Special features include:

* Messages cannot be decoded without the key

* A single decoder for all file types and encoding techniques,
including all future ones

* Format-specific encoders can be easily written without having to
worry about information theoretic encoding or cryptography

* Support for multiple messages to multiple keys in a single file

The primary use case for DissidentX is encoding messages in files on 
the web. There should be a utility which scans all objects the user's 
web browser downloads (html files, images, css files, etc.) for messages
using all of the keys the user has entered. Someone sending messages 
to that person provides a web service where users who have widely 
viewed web sites can upload their files and get back slightly modified
version with messages steganographically added. The web users should 
not be able to read what the messages are, and it should be possible for 
the service doing the encoding to not have to keep messages in plaintext. 
Because encoding rates are so low, a number of the parameters to the 
encoding and decoding libraries have been lowered to not be appropriate 
for all use cases. They should be evaluated in the context of this one.

The same technology should alse be used for easter egg hunts, because 
that's fun and provides cover traffic.


Usage guide:

Uses Python3, PyCrypto, and sha3
http://pypi.python.org/pypi/pycrypto
http://pypi.python.org/pypi/pysha3/

As examples, the command line tools line_ending_encoder and 
universal_decoder are included. line_ending_encoder is based on adding 
trailing spaces to the end of lines in a text file.

Use line_ending_encoder like this:

python3 line_ending_encoder.py myfile.txt key1 payload1 key2 payload2

That will modify myfile.txt, hiding payload1 to the key key1 and 
payload2 to the key key2. Any number of key/payload pairs are allowed,
although any given file can only support a certain total length of 
payloads.

The keys are assumed to be in unicode, which is correct. The payloads 
are also assumed to be in unicode, which is a hack to make the output 
pretty, and not completely general.

After you encode data with line_ending_encoder you can get it back out 
like this:

python3 universal_decoder.py myfile.txt key1

which will print out payload1. Likewise for payload2 and key2.

Note that line_ending_encoder only gets one bit per line, with overhead 
of seven bytes, and that repeating the same section of text repeatedly in 
a text file doesn't get extra bits.


Encoder writing guide:

The prepare_message() function takes a key and plaintext, both byte strings, 
and returns another key and ciphertext to be used later. This is done as a 
separate step to enable the use case where messages to be encoded are stored 
on a server already encrypted.

The pack_and_encode_messages() function takes an array of results from 
prepare_message() and a processed file for the messages to be stored in. The 
processed file is an array consisting alternately of fixed binary strings and 
arrays of length two giving alternate possible values for that position. 
Alternates can be anything semantically valid for the file format being used. 
For example in human readable text files eliminating unnecessary commas in 
text, or alternate spellings for words, or alternative word orders can all 
be used. Multiple methods of generating alternates can be used in the same 
file.

Simple implementations are in line_endings_encoder.py and tab_encoder.py, 
both designed to work on common computer language files.

More detail on the math involved is in Explanation.txt


FAQ:

Q. Can someone modify the message stored in a file?

A. No. Changing even a single byte of the file will completely
obliterate any message which was stored.

Q. Why did you use Python3 as a reference language?

A. Because not having distinct binary and unicode string types is barbaric.

Q. Can I get a copy of this for another language?

A. If somebody writes it. This code is being released as a reference
in the hopes that other people will pick it up and run with it.

Q. Why are you doing row reduction manually in Python instead of using numpy?

A. Because I don't know how. Feel free to implement improvements.

Q. Can someone detect that a file has messages encoded in it?

A. That depends on the encoding used and the properties of the file the data is 
being encoded in. There's a whole field of academic literature 
on steganography, none of which is invalidated by this code. What this code 
does is vastly simplify the implementation of new steganographic techniques, 
and allow a universal decoder and encoding of multiple messages to different 
keys in the same file.

Q. How much data can be encoded in a file?

A. That's entirely dependant on the file type and specific encoding, but if 
you insist on a made up number, let's say a ratio of around 500:1, and the 
encoded message has overhead of about 7 bytes.

Q. Why can't it be given more than two alternates for one position to encode 
more information?

A. Because of math. See Explanation.txt for a bit more detail.

Q. Your code is horribly inefficient and can be optimized in all kinds of ways.

A. That's why it's called 'reference' code.

Q. It would be possible to pack in data more densely if alternates are
required to always be the same length, or variable bytes are allowed to be set 
to arbitrary values.

A. Yes, but those put severe restrictions on what can be done in an
encoder, and hence are less likely to be useful in practice.

Q. Why don't you use public key encryption?

A. Because bits are precious enough for that to be unweildy, and it would 
disallow use of arbitrary human readable strings as keys. The symmetry is 
best viewed as a feature: because the value of a key is severely diminished 
if it's widely known, there's a reason to horde them, which is the desired 
behavior.
