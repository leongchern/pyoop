""" An example to show how we can how we can extend the dict class """
from chapter_3.classes.longname import LongNameDict

longkeys=LongNameDict()
longkeys['hello']=1
longkeys['longest yet']=5
longkeys['hello2']='world'
longkeys.longest_key()