#!/usr/bin/env python3


config_item_len   = 4
blank_config_line = [""] * config_item_len

#filename, title, description, enabled

class config_item:
    def __init__(self,item_line=blank_config_line):
        self.filename    = item_line[0]
        self.title       = item_line[1]
        self.description = item_line[2]
        self.enabled     = item_line[3]
    def __str__(self):
        return(self.filename)
    def __repr__(self):
        out_line = "<wwh config item %s:%s>" % (self.title,self.filename)
        return(out_line)
