from IronDB.logic import checks, DB_config, SetDB
import os

SetDB.file()

DB_config.config(status=True, back_up=None, main_file="main.py", key_word={"A" : "B"}, custom_config="uh.json")

checks.DB_check()