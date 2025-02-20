#!/usr/bin/env PYTHONHASHSEED=1234 python3

# Copyright 2014-2024 Brett Slatkin, Pearson Education Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

### Start book environment setup
import random
random.seed(1234)

import logging
from pprint import pprint
from sys import stdout as STDOUT

# Write all output to a temporary directory
import atexit
import gc
import io
import os
import tempfile

TEST_DIR = tempfile.TemporaryDirectory()
atexit.register(TEST_DIR.cleanup)

# Make sure Windows processes exit cleanly
OLD_CWD = os.getcwd()
atexit.register(lambda: os.chdir(OLD_CWD))
os.chdir(TEST_DIR.name)

def close_open_files():
    everything = gc.get_objects()
    for obj in everything:
        if isinstance(obj, io.IOBase):
            obj.close()

atexit.register(close_open_files)
### End book environment setup


print("Example 1")
from threading import Lock

lock = Lock()
with lock:
    # Do something while maintaining an invariant
    pass


print("Example 2")
lock.acquire()
try:
    # Do something while maintaining an invariant
    pass
finally:
    lock.release()


print("Example 3")
import logging

logging.getLogger().setLevel(logging.WARNING)

def my_function():
    logging.debug("Some debug data")
    logging.error("Error log here")
    logging.debug("More debug data")


print("Example 4")
my_function()


print("Example 5")
from contextlib import contextmanager

@contextmanager
def debug_logging(level):
    logger = logging.getLogger()
    old_level = logger.getEffectiveLevel()
    logger.setLevel(level)
    try:
        yield
    finally:
        logger.setLevel(old_level)


print("Example 6")
with debug_logging(logging.DEBUG):
    print("* Inside:")
    my_function()

print("* After:")
my_function()


print("Example 7")
with open("my_output.txt", "w") as handle:
    handle.write("This is some data!")


print("Example 8")
handle = open("my_output.txt", "w")
try:
    handle.write("This is some data!")
finally:
    handle.close()


print("Example 9")
@contextmanager
def log_level(level, name):
    logger = logging.getLogger(name)
    old_level = logger.getEffectiveLevel()
    logger.setLevel(level)
    try:
        yield logger
    finally:
        logger.setLevel(old_level)


print("Example 10")
with log_level(logging.DEBUG, "my-log") as my_logger:
    my_logger.debug(f"This is a message for {my_logger.name}!")
    logging.debug("This will not print")


print("Example 11")
logger = logging.getLogger("my-log")
logger.debug("Debug will not print")
logger.error("Error will print")


print("Example 12")
with log_level(logging.DEBUG, "other-log") as my_logger:  # Changed
    my_logger.debug(f"This is a message for {my_logger.name}!")
    logging.debug("This will not print")
