# python-faster-than-c
In some cases Python maybe faster than C, and JS may be faster than C++

## Quick start

You can see that all programs do the same thing.

```console
$ gcc -o ghoul .ghoul.c && ./ghoul
$ g++ -o ghoul ghoul.cpp && ./ghoul
$ rustc ghoul.rs && ./ghoul
$ nodejs ghoul.js
$ python3 ghoul.py
$ ruby ghoul.rb
```

And then test the speed of compiling and exectuion

```console
$ python3 time_all.py
```
