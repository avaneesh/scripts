#!/bin/bash

function process_readme_line_old () {
    line=$1
    if [[ $file_mode == "device" ]]; then
        # We are in DEVICE part, look for start of EXTRA part
        if [[ $line == *PREPLACE_EXTRA* ]]; then
            decho "Changing file mode to extra"
            file_mode="extra"
            # First adjust prevous line from older file and add it to new file
            cat $device_part_file | tail -n 1  >> $extra_part_file
            cat $device_part_file | head -n -1 > tempreplace.$$
            mv tempreplace.$$ $device_part_file
            # Now echo current line
            echo $line >> $extra_part_file
        else
            echo $line >> $device_part_file
        fi
    else
        echo $line >> $extra_part_file
        # We are already in EXTRA part
    fi
}

function process_readme_line_new () {
    line=$1
    decho "curr_file_mode_index=$curr_file_mode_index, "
    curr_file_name=$base_readme_filename.$$.${all_file_modes[$curr_file_mode_index]}.part
    prev_file_name=$curr_file_name
    decho "Using file: $curr_file_name"
        # We are in DEVICE part, look for start of EXTRA part
        if [[ $line == *${next_file_grep_pattern_for_modes[$curr_file_mode_index]}* ]]; then
            ((++curr_file_mode_index))
            decho "Changing file mode to ${all_file_modes[$curr_file_mode_index]}"
            curr_file_name=$base_readme_filename.$$.${all_file_modes[$curr_file_mode_index]}.part
            # First adjust previous line from older file and add it to new file
            cat $prev_file_name | tail -n 1  >> $curr_file_name
            cat $prev_file_name | head -n -1 > tempreplace.$$
            mv tempreplace.$$ $prev_file_name
            # Now echo current line
            echo $line >> $curr_file_name
        else
            echo $line >> $curr_file_name
        fi
}


function get_replacement_value () {
    hval=`hget rules_hash_table $1`
    if [[ $hval == DYNAMIC_VAR_* ]]; then
        hval=${hval#DYNAMIC_VAR_}
        #decho "will try to dref $hval.."
        eval fval=\${$hval}
    else
        fval=$hval
    fi
    #decho "Derived value is $fval"
    echo $fval
}

function put_replacement_value () {
    ((++rule_num))
    decho "Adding rule number $rule_num: $1"
    all_rules[$rule_num]=$1
    hput rules_hash_table $1 $2
}

function replace_this_in_file () {
    string_to_replace=$1
    fyle=$2
    replace_with=$(get_replacement_value $string_to_replace)
    v2echo "Replacing $string_to_replace with $replace_with"
    sed -i "s|$string_to_replace|$replace_with|g" $fyle
}

function apply_all_transformations () {
    decho "Applying all Exising rules: ${#all_rules[@]}"
    fyle=$1
    for curr_rule in ${all_rules[@]}
    do
        replace_this_in_file $curr_rule $fyle
    done
}
