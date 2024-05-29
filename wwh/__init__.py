#!/usr/bin/env python3
'''
wwh - Wireplumber W31rd Hax

Common python library for GUI and CLI
'''

import os,sys

class _lib_meta:
    lib_ver = "0.1.0"

class default_var:
    config_dirs       = ['/usr/share/wireplumber-w31rd-hax','/usr/local/share/wireplumber-w31rd-hax']
    user_config_dir   = "%s/.config/wireplumber/wireplumber.conf.d" % os.getenv("HOME")

class colors:
    '''pretty terminal colors'''
    reset='\033[0m'
    bold='\033[01m'
    yellow='\033[93m'

def warn(message):
    message = "tor_util_cli: %s%s¡WARN!:%s %s" % (colors.yellow, colors.bold, colors.reset, message)
    print("tor_util_cli:" + colors.yellow + colors.bold + "¡WARN!: " + colors.reset + message, file=sys.stderr)
    return

def list_config_files():
    '''Get list of available configs, return as list'''
    
    input_files = []
    # get files in directories, put them in input_files list[], as full path
    for item in default_var.config_dirs:
        list_files = os.listdir(item)
        input_files += [ item + "/" + i for i in list_files ] #append directory name to files

    return input_files
    
def get_available_configs(file_list):
    '''Take a list[] of files and check if they are configs. parse valid configs into a list and return it
    object is filename, title, description, enabled'''
    
    return_object = []
    delimeter = ":"
    for file in file_list:

        if is_valid_config(file) != True:
            warn_line = "Not a Valid File: %s" % (file)
            warn(warn_line)
            continue
        try:
            file_obj   = open(file,"r")
            file_lines = file_obj.readlines()
            file_obj.close()
        except:
            warn_msg = "Could Not Read File: %s" % (file)
            warn(warn_msg)
            continue
        
        for line in file_lines:
            meta_line = None
            # Check if there is a metadata, and the metadata is correct enough to load(i.e. correct length)
            for line in file_lines:
                if line.startswith("#@META"):
                    meta_line = line.split(delimeter)
                else:
                    continue
            if meta_line == None:
                warn_line = "Missing Metadata, File: %s" % (file)
                warn(warn_line)
                continue
            else:
                # replace #@META slug with the filename, and add None for enabled
                meta_line[0] = file
                meta_line.append( is_enabled(file) ) # Check if this is symlinked
               # Now add the object to the list.
               return_object.append(meta_line)
            
        # Now return
        return(return_obj)

def is_vald_config(filename):
    '''Check if file is a valid config'''
    #starts as False
    # If the file does not end with .conf it will not load by wireplumber, so its false    
    if filename.endswith(".conf") == False:
        return False
    if os.path_exists(filename)
    # Can we read the file
    try:
        file_obj   = open(filename,"r")
        file_lines = file_obj.readlines()
        file_obj.close()
    except:
        return False

    for line in file_lines:
        meta_line = None
        # Scan lines for the metaline
        for line in file_lines:
            if line.startswith("#@META"):
                meta_line = line.split(delimeter)
                # See if there are three fields
                if len(meta_line) != 3:
                    return False
            else:
                return False
        # Check if the metaline has been set.
        if meta_line == None:
            return False
        else:
            # If we get this far, this is a valid config
            return True

def is_enabled(filename):
    '''Check if file is enabled, i.e. symlink'd to user wireplumber dir, returns True/False'''
    
    filename_basename  = os.path_basename(filename)
    symlink_filename   = "%s/%s" % (default_var.user_config_dir,filename_basename)
     
    if os.path.islink( symlink_filename ):
        return False
    elif os.readlink( symlink_filename ) != filename:
        return False
    else:
        return True
    

def load_available_configs():
    '''Load Available Configs'''
    config_files  = list_config_files()
    config_object = get_available_configs(config_files)
    return(config_object)
    
