rm -r yml_files
doorstop create L1 yml_files/L1
doorstop create L2 yml_files/L2 --parent L1
doorstop create L3 yml_files/L3 --parent L2

