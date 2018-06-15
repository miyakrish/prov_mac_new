import subprocess

def mac_keys_remap(map=True):
    keys_to_remap = ['0x70000002B', '0x7000000E0', '0x7000000E4']
    key_none = '0x700000000'
    remap_command = "hidutil property --set '{\"UserKeyMapping\":[{\"HIDKeyboardModifierMappingSrc\":'%s',\"HIDKeyboardModifierMappingDst\":'%s'}]}'"
    if map:
        for key in keys_to_remap:
            remapproc= subprocess.Popen(remap_command % (key, key_none),
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             shell=True)
            stdout, stderr = remapproc.communicate()
            print (stdout)
    else:
        for key in keys_to_remap:
            remapproc= subprocess.Popen(remap_command % (key, key),
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             shell=True)
            stdout, stderr = remapproc.communicate()
            print (stdout)

mac_keys_remap()
