import re, os, sys

if len(sys.argv) < 2:
    print 'Error: provide readme file name'
    sys.exit()

my_loc='/'.join(sys.argv[0].split('/')[:-1])
readme_file_name="README_"+sys.argv[1]
if len(sys.argv) > 2:
    session_name=sys.argv[2]
else:
    session_name='_'.join(readme_file_name.split('_')[1:])

tmux_script_name="tmux_sess.sh"

parse_state_list=['NOTHING_USEFUL', 'LOOKING_WIN_GUARD_1', 'LOOKING_WIN_GUARD_2', 'LOOKING_WIN_NAME', 'LOOKING_WIN_COMMANDS']
current_parse_state='LOOKING_WIN_GUARD_1'

try:
    readme_file=open(readme_file_name)
except:
    print 'Could not open file:', readme_file_name
    sys.exit()

with open(my_loc+'/tmux_generator_template.txt') as f:
    tmux_script_template = f.read()

# arg: window number, window name
tmux_window_template="tmux new-window -t %s:%s -n '%s'"
# arg: command
tmux_cmd_template="tmux send-keys '%s' 'C-m'"
# arg: weight
tmux_split_template="tmux split-window -p %s"

# export own window_number so other scripts can use it
tmux_cmd_curr_window="tmux send-keys 'export _TMUX_CURR_WINDOW=%s' 'C-m'"

windows_list = []
window_lines = []
window_number=1
unused_window_skip_it=False
for l in readme_file:
    l=l.rstrip('\n')
    if re.findall("^===", l):
        if current_parse_state == 'NOTHING_USEFUL':
            print 'ERROR: parsing error 1'
        elif current_parse_state == 'LOOKING_WIN_GUARD_1':
            current_parse_state = 'LOOKING_WIN_NAME'
        elif current_parse_state == 'LOOKING_WIN_GUARD_2':
            # Got window name
            current_parse_state = 'LOOKING_WIN_COMMANDS'
        elif current_parse_state == 'LOOKING_WIN_NAME':
            print 'ERROR: parsing error 2'
            exit 
        elif current_parse_state == 'LOOKING_WIN_COMMANDS':
            # Done with previous window details, get next one

            if unused_window_skip_it:
                print 'Skipping unused window'
            else:
                current_window_details = '\n'.join(window_lines)
                windows_list.append(current_window_details)
            current_parse_state = 'LOOKING_WIN_NAME'
            print '-------- done with window', window_number
    elif re.findall("^WINDOW", l):
        if current_parse_state == 'LOOKING_WIN_NAME':
            window_name = l.split(' ')[1]
            print 'Got window name --', window_name
            window_lines = []
            cmd=tmux_window_template % (session_name, window_number, window_name)
            window_lines.append(cmd)
            if re.findall("UNUSED", l):
                unused_window_skip_it=True
            else:
                 unused_window_skip_it=False
                 cmd=tmux_cmd_curr_window%window_number
                 window_lines.append(cmd)
                 window_number += 1

            current_parse_state = 'LOOKING_WIN_GUARD_2'
        else:
            print 'ERROR: parsing error 3'
    else:
         print 'Got command -', l
         if l:
            if re.findall("^##", l):
                print 'Ignoring readme comment', l
            else:
                cmd=tmux_cmd_template%l
                window_lines.append(cmd)


# Done last window details, add it
if unused_window_skip_it:
    print 'Skipping unused window'
else:
    current_window_details = '\n'.join(window_lines)
    windows_list.append(current_window_details)
current_parse_state = 'LOOKING_WIN_NAME'
print '-------- done with window', window_number


windows_details = '\n'.join(windows_list)
out_script=tmux_script_template % (session_name, windows_details, session_name, session_name)

with open(tmux_script_name, 'w') as f:
    f.write(out_script)

# Start it now..
os.system('/bin/bash '+tmux_script_name)
