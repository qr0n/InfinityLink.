import json
import os
from re import L

from IronDB.key_gen import assigner

import flask
import time

from flask import Flask
import time
import sys
db_file = []



def db_load():
  """Internal DB load method, importable: True"""
  with open("IronDB/config.json", "r") as R:
    l_R = json.load(R)
    with open(l_R["file"], "r") as K:
      l_K = json.load(K)
      return dict(l_K)

class checks:
  @staticmethod
  def web_check():
    with open("IronDB/config.json", 'r') as E:
      l_E = json.load(E)
      if l_E["attrs"]["web_access"] == True:
        return print("Web mode is enabled/.")

  @staticmethod
  def DB_check():

    with open("IronDB/config.json", "r") as A:
      l_A = json.load(A)
      if l_A["attrs"]["web_access"] == "True":
        return print(os.popen("python3 IronDB/web_view.py").read())

class Utilities:
  @staticmethod
  def make_file(file_name=None):
    try:

      file_nae = file_name or assigner.Create()

      with open("config.json", "r") as R:

        L = json.load(R)
        L["file"] = f"{file_nae}.json"

        with open("config.json", "w") as R:
          json.dump(R, L)

      with open(f"{file_nae}.json", 'w') as E:
        E.write("{\n\n}")

        print("file configured. {}".format(file_nae))
        db_file.append(file_nae)

        pass
    except Exception as R:

      return R

def IronPy(main_file):
    try:
      exec(os.system(f"python{sys.version[:3]} {main_file}"))
    except Exception as E:
      return E

def key_replace(key, rep_val):
  with open("IronDB/config.json", "r") as E:
    l_E = json.load(E)
    with open(l_E["file"], "r") as A:
      l_A = json.load(A)
      for value in l_A:
        if value == key:
          l_A[key] = rep_val
      with open(l_E["file"], "w") as A:
        json.dump(A, l_A)



class DB_config:
  @staticmethod
  def config(status : bool = None, back_up: str = None, main_file : str = None, key_word : dict =None, custom_config : str = None):
    if status:
      checks.DB_check()
    if back_up is not None:
      with open(back_up, "r") as E:
        l_E = json.load(E)
        pass
    if main_file is not None:
      return IronPy(main_file=main_file)
    if key_word is not None:
      key_replace()

    
class SetDB:
  @staticmethod
  def file(file : str=None):
    Utilities.make_file(file_name=file)
        
def make_file(file_name=None):
  try:

    file_nae = file_name or assigner.Create()

    with open("config.json", "r") as R:

      L = json.load(R)
      L["DB_file"] = f"{file_name}.json"

    with open("config.json", "w") as R:
      json.dump()

    with open(f"{file_nae}.json", 'w') as E:
      E.write("{\n\n}")

      print("file configured. {}".format(file_nae))
      db_file.append(file_nae)

      pass
  except Exception as R:

    return R

class SetDB:
  @staticmethod
  def file(file : str=None):
    make_file(file_name=file)
        
class internal_config:
  def config(config_file = "IronDB/config.json" or "config.txt", setting=None):
    if setting == "random_key":
      return assigner.Create()
    if setting == "web_access":
      with open(str(db_file)[2:-2], 'r') as E:
        return json.load(E) 
