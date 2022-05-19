import sys # hna  ta importiwe  la valize system
sys.path.append('./scripts') 
import global_config
import int_seg_config
import ospf_config

exec('global_config')
exec('int_seg_config')
exec('ospf_config')
