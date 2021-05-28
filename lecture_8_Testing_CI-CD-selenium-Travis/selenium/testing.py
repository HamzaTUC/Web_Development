import os
import pathlib
import unittest

from selenium import webdriver

def file_uri():
    return pathlib.Path(os.path.abspath("counter.html")).as_uri()




