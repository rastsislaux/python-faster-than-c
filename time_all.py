#! /bin/python3

import os
import subprocess

# Results extracting and printing

def extract_time(sp):
    time = sp[-2].decode("utf-8").split()[2][2:-7].split(".")
    return float(time[0]) + float(time[1])/100


def get_stdout(command):
    return subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT
    ).stdout.readlines()


class Result:

    def __init__(self, name, compile_time, run_time) -> None:
        self.name = name
        self.compile_time = compile_time
        self.run_time = run_time

    def __repr__(self):
        return f"{self.name}\t\t| {self.compile_time} s \t| {self.run_time} s \t| {self.compile_time + self.run_time} s"


def print_head():
    print("Language\t| Compile\t| Run\t\t| Total")


def print_line():
    print("----------------+---------------+---------------+--------")


def print_results(result_list, sort_key):
    print_line()
    result_list.sort(key=sort_key)
    print_head()
    print_line()
    i = 1
    for result in result_list:
        print(f"{i}. {result}")
        i += 1
    print_line()


# Commands to run

PYTHON      = ["time", "python3", "ghoul.py"]
JAVASCRIPT  = ["time", "nodejs", "ghoul.js"]
RUBY        = ["time", "ruby", "ghoul.rb"]

CPLUSPLUS1  = ["time", "g++", "-o", "cppghoul", "ghoul.cpp"]
CPLUSPLUS2  = ["time", "./cppghoul"]

C1          = ["time", "gcc", "-o", "cghoul", "ghoul.c"]
C2          = ["time", "./cghoul"]

RUST1       = ["time", "rustc", "ghoul.rs"]
RUST2       = ["time", "./ghoul"]

# Getting the results

result_list = [
    Result("Python3\b\b\b", 0., extract_time(get_stdout(PYTHON))),
    Result("JS", 0., extract_time(get_stdout(JAVASCRIPT))),
    Result("Ruby", 0., extract_time(get_stdout(RUBY))),
    Result("C++", extract_time(get_stdout(CPLUSPLUS1)), extract_time(get_stdout(CPLUSPLUS2))),
    Result("C", extract_time(get_stdout(C1)), extract_time(get_stdout(C2))),
    Result("Rust", extract_time(get_stdout(RUST1)), extract_time(get_stdout(RUST2)))
]

print("\nBy total time:")
print_results(result_list, lambda x: x.compile_time+x.run_time)

print("\nBy compile time:")
print_results(result_list, lambda x: x.compile_time)

print("\nBy run time:")
print_results(result_list, lambda x: x.run_time)

# Delete binaries

os.system("rm cghoul cppghoul ghoul")
