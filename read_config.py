from configparser import ConfigParser
def get_config(cat,key):
    con=ConfigParser()
    con.read("./PyTest/config.ini")
    return con.get(cat,key)
