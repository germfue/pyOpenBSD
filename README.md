---
---
# pyOpenBSD

OpenBSD.org provides a lot of useful information but there is no easy and
programmatically way to access it. pyOpenBSD tries to solve that problem.

A core principle of pyOpenBSD is not to perform any request to OpenBSD.org at
runtime. Instead, test cases are in place to identify when resources get
updated.

For now pyOpenBSD provides mirror information only. Here there is a code
snippet to show how to use it:

```python
from pyOpenBSD import mirrors, Protocol
print mirrors[Protocol.http]
```

OpenBSD offers mirrors using 3 protocols:

* HTTP
* FTP
* rsync

# License
BSD 2-Clause License
