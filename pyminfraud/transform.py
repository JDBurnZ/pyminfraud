# coding: utf-8

import hashlib

"""           .s`               +`            +:
.My`           dm-            .hh           .hM.
 mMN/          oMMo          /NM+          /NMN
 sMMMh.        .MMMd.      `yMMM.        `yMMMy
 -MMMMN+.       dMMMN+::::/mMMMd       ./mMMMM+
  NMMMMMMMmhs+:.oMMMMMMMMMMMMMMo ./oymMMMMMMMM.
  yMMMMMMMMMMMMM:MMMMMMMMMMMMMM.dMMMMMMMMMMMMm
  :MMMMMmmMMMMMM+dMMMMm++sMMMMm-MMMMMMNdMMMMMs
   NMMMMdo///+shyoMMMMM- dMMMMs+hyo///+sNMMMM:
   yMMMMMMMMMmhs/-MMMMMh/MMMMM-+ydmMMMMMMMMMM`
   /MMMMMmNMMMMMM+dMMMMMMMMMMN-MMMMMMNmMMMMMh
   `MMMMMmyssoshmh/MMMMMMMMMMosmhssssymMMMMMo
    sMMMMMMMMMNdyo:-dMMMMMMN/-+sdNMMMMMMMMMm.
     oMMMMMMMMMMMMMN/sMMMMh/dMMMMMMMMMMMMMd`
    -`+MMMMm:/shNMMMMh+NNosMMMMNdysoNMMMMy.:
    .m./MMMMN-   :MMMMNooNMMMMy   .mMMMMs.m-
     mN-:NMMMMms/`oMMMMMMMMMMh -omMMMMM+-NN
     sMN:-NMMMMMMMdNMMMMMMMMNymMMMMMMM/:NMy
     :MMM/.mMMMMMMMMMMMMMMMMMMMMMMMMN-/MMM+
	NMMM+`dMMMMMMMMMMMMMMMMMMMMMMm.+MMMM.
	yMMMMs`hMMMMMMMMMMMMMMMMMMMMd.sMMMMN
	/MMMMMy`yMMMMMMMMMMMMMMMMMMh`yMMMMMy
	`MMMMMMh`sMMMMMMMMMMMMMMMMy`hMMMMMM/
	 dMMMMMMd.+MMMMMMMMMMMMMMo`dMMMMMMM.
	 oMMMMMMMm./MMMMMMMMMMMM+.mMMMMMMMm
	 .dMMMMMMMN-:NMMMMMMMMN:.mMMMMMMMMs
	   `/smMMMMM/-NMMMMMMN--NMMMMMNy/.
		 .+hNMM+.mMMMMm.:MMMNh+.
		    `:sdo`hMMd`/Nh+-
			  `` sy"""

def md5(value):
	return hashlib.md5(value.encode('utf-8')).hexdigest()

def bin(value):
	return value[0:6]
