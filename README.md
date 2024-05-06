# wireplumber-w31rd-hax
Collection of assorted workarounds and hacks for wireplumber, as well tools for enabling or disabling them

Configs can be made by taking config snipets and adding the follow metadata tag

```
#@META:Name:Long Description of what the file does
```

Programs
--------

These are tools to list, enable and disable wireplumber configs. These do not
require root, and will work on a per-account basis only. These work by sym-link
ing relavant configs to ```./config/wireplumber/wireplumber.conf.d/```.

wwh-cli.py - Command Line tool

wwh-gui.py - GUI tool(Planned)

Why
---
We are trying to make the sound on GNU, Linux and combinations thereof, work.
People shouldn't have to be able to write JSON configs to fix silly issues
upstream. We can now just ship the most popular workarounds, tricks, etc, and
then let users enable or disable them with the flick of a switch
