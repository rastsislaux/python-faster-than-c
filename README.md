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

My results:

By total time:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
By compile time:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
By run time:
| Language        | Compile       | Run           | Total   | Language        | Compile       | Run           | Total   | Language        | Compile       | Run             | Total
| --------------- | ------------- | ------------- | ------- | --------------- | ------------- | ------------- | ------- | --------------- | ------------- | --------------- | ------- |
| 1. Python3      | 0.0 s         | 0.01 s        | 0.01 s  | 1. Python3      | 0.0 s         | 0.01 s        | 0.01 s  | 1. C            | 0.09 s        | 0.0 s           | 0.09 s  |
| 2. Ruby         | 0.0 s         | 0.09 s        | 0.09 s  | 2. Ruby         | 0.0 s         | 0.09 s        | 0.09 s  | 2. C++          | 0.41 s        | 0.0 s           | 0.41 s  |
| 3. C            | 0.09 s        | 0.0 s         | 0.09 s  | 3. JS           | 0.0 s         | 0.22 s        | 0.22 s  | 3. Rust         | 0.69 s        | 0.0 s           | 0.69 s  |
| 4. JS           | 0.0 s         | 0.22 s        | 0.22 s  | 4. C            | 0.09 s        | 0.0 s         | 0.09 s  | 4. Python3      | 0.0 s         | 0.01 s          | 0.01 s  |
| 5. C++          | 0.41 s        | 0.0 s         | 0.41 s  | 5. C++          | 0.41 s        | 0.0 s         | 0.41 s  | 5. Ruby         | 0.0 s         | 0.09 s          | 0.09 s  |
| 6. Rust         | 0.69 s        | 0.0 s         | 0.69 s  | 6. Rust         | 0.69 s        | 0.0 s         | 0.69 s  | 6. JS           | 0.0 s         | 0.22 s          | 0.22 s  |
