'''
sys6_list = ["ece","ecs","etw","elx","eoh","elr","ecc","ecp","eci","ecv","ecx","ecw","ecy","ecr","ecq","eck","eum","ecz","elo","eln","ese","eso","esm","esl","eko","ekf","eab","eih","ena","elu","eun","elw","ell","elc","eld","elf","ecol","ecoi","ecoj","efe","stm","seo","sev","sey","sem","sej","seb","sef","setu","setc","seen","senr","spt","sek","sei","seh","shb","senh","seeh","see","senn","sew","sea","sens","sed","sel","sega","seec","sene","senc","ses","sbv","ype","ypk","ypa","ypn","ypm","ypp","ypg","ypz","ypt","ypd","ypx","yph","ypw","ypj","ypv","ypl","yps","ypo","ypi","ypy","ypb","ypq","ypu","ypr","ypc","ypf","yen","yep","yey","yel","yew","yet","yee","ysi","yal","yfr","yin","ykr","yro","yak","eca","patr","pato","pct","pcc","pcv","pwa","pec","eta","epy","epr","eam","eay","ebi","erj","plu","pay","ptt","enc","eno","eclo","eec","enl","ecla","eclc","eclg","ecle","ecln","ecli","eclx","ecly","eclz","eas","eau","eae","ear","enr","esa","csk","csz","csi","csj","ccon","ctu","kpn","kpu","kpm","kpp","kpk","kph","kpz","kpv","kpw","kpy","kpg","kpc","kpq","kpt","kpe","kpo","kpr","kpj","kpi","kpa","kps","kpx","kpb","kpne","kpnu","kva","kvd","kvq","kox","koe","kok","kom","kmi","spe","smaf","smw","smar","smac","serf","sers","sfw","sfo","pmr","pmib","ete","etc","edw","edl","ddc","ddd","dze","dzc","xbo","xbv","xne","xnm","xdo","xpo","pam","plf","paj","paq","pva","pao","kln","pant","panp","rah","raq","raa","psi","ebt","ron","cnt","cem","ced","pge","hav","ksa","kin","ebf","aap","xoo","xom","xop","xoy","xor","xoz","xtn","vch","vcf","vce","vcj","vco","vcm","vci","vcl","vcq","vcs","vcx","vcz","vvu","vvy","vpa","vpb","vpk","vpf","vph","vha","vca","vag","vsp","vex","vfu","vni","van","lag","vau","vcy","vct","vtu","vfi","vfm","awd","ppr","pae","paev","paei","pau","pap","pag","paf","pnc","paeb","pdk","psg","prp","paer","paem","pael","paes","paeu","paeg","paec","paeo","ppu","ppf","ppg","ppw","ppt","ppi","ppx","ppuh","ppun","ppud","pfv","pmon","pmot","pmos","ppj","pst","psb","psyr","psp","pci","pfl","pprc","ppro","pfo","pfs","pfe","pfc","pfw","pfb","pff","ppz","pman","ptv","pen","pmy","pmk","psc","psj","psh","pstu","pstt","pbm","pba","pbc","ppuu","pdr","pre","psv","psk","pch","pcz","pcp","psw","ppv","pses","psem","psec","avn","avl","avd","sfr","sbb","swd","psm","maq","mhc","mad","mari","psy","mvs","ttu","saga","mmt","mah","tvi","hch","csa","hel","ham","adi","mmw","mme","mpc","tol","tor","oai","gsn","aha","ahj","ahi","tau","gap","fpp","salv","cvi","pse","rsl","rsn","rsm","rse","rpf","reu","reh","rme","cti","cbw","bma","bmv","bml","bmn","bmal","bmae","bmaq","bmai","bmaf","bmaz","bmab","bps","bpm","bpl","bpd","bpr","bpse","bpsm","bpsu","bpsd","bpz","bpk","bpsh","bpsa","bpso","bte","btq","btj","btz","btd","btv","bthe","bthm","btha","bthl","bok","boc","but","bvi","bve","bur","bcn","bch","bcm","bcj","bcen","bcew","bceo","bam","bac","bmu","bmk","bmul","bct","bced","bdl","bpyr","bcon","bxe","bxb","bph","bpy","bgl","bgp","bgu","bug","bge","bgf","bgd","bgo","byi","buk","bpx","buo","bue","bul","bub","bfn","bbr","bbm","bbh","bbx","bpt","axy","axo","axn","axs","tea","teg","tas","tat","put","amim","aav","aaa","dac","del","vap","vpe","vpd","hse","cfu","care","lch","rge","azo","aza","azi","dar","ant","arc","pca","des","mxa","mfu","msd","age","scl","scu","ccro","samy","mlo","mci","sfd","rec","rei","rep","rga","azc","rsp","rsh","rsk","pde","psf","amv","azl","ali","tmo","nde"]
sys4_list = ["ecf", "elx", "ecq", "eum", "ecoj", "ecoh", "shb", "senh", "seeh", "sew", "sea", "sed", "ypm", "yps", "ypo", "ypi", "yfr", "sbc", "eca", "patr", "pato", "pec", "eta", "ecle", "ecln", "ecli", "eclz", "ecla", "eclc", "ear", "esa", "cui", "cmw", "ctu", "kpu", "kpm", "kpp", "kph", "kpv", "kpw", "kpg", "kpt", "kpe", "kpj", "kpx", "kpnu", "kox", "kok", "cko", "cro", "cfd", "cama", "pmr", "etr", "hde", "ddd", "dze", "ddc", "dzc", "pant", "panp", "raq", "raa", "ced", "ksa", "aat", "aao", "xfa", "xfn", "xff", "xfl", "xfs", "xcc", "xcb", "xca", "xcp", "xcv", "xac", "xci", "xct", "xcu", "xcn", "xcw", "xcr", "xcm", "xcf", "xcj", "xfu", "xao", "xal", "sml", "smt", "buj", "smz", "sacz", "psd", "lab", "lcp", "lgu", "dji", "vha", "vca", "vtu", "vfi", "ppr", "pau", "pap", "paes", "paeu", "ppx", "pfv", "pmon", "pmot", "ppj", "psyr", "psp", "pfc", "pfn", "pmk", "psr", "psj", "pstu", "pdr", "ppse", "pcz", "pses", "psem", "acx", "abaz", "sbn", "shn", "mad", "lpn", "lph", "lpo", "lpu", "lpm", "lpf", "lpp", "lpc", "lpa", "llo", "lok", "tmc", "mec", "cza", "tmb", "tgr", "hna", "adi", "kki", "rso", "rsm", "rse", "rpi", "reu", "rme", "bpr", "but", "bvi", "bve", "bcn", "bch", "bcm", "bcj", "bcen", "bam", "bmu", "bmj", "bmk", "bced", "bgd", "bgo", "byi", "buk", "bpla", "bxe", "bxb", "bph", "bpx", "bpy", "prb", "pox", "pfg", "bpt", "axy", "teq", "tea", "put", "aka", "afa", "pna", "aav", "ajs", "dia", "ack", "vei", "dac", "vap", "vpd", "ctes", "adn", "adk", "mpt", "care", "lch", "tin", "thi", "bbag", "net", "nit", "eba", "rbu", "mei", "hps", "hpg", "hpp", "hex", "hes", "wsu", "cjj", "cjn", "cji", "cjs", "cjen", "cfv", "cfx", "cfz", "cha", "cla", "ccc", "ccq", "ccf", "ccy", "ccoi", "ccof", "cpel", "dsa", "dhy", "dps", "acp", "rpr", "rpo", "rpw", "rpz", "rpg", "rps", "rpv", "rpq", "rpl", "rpn", "rty", "rtt", "rtb", "rcm", "rcc", "rbe", "rbo", "rco", "rfe", "rak", "rri", "rrj", "rra", "rrc", "rrh", "rrb", "rrn", "rrp", "rrm", "rrr", "rms", "rmi", "rpk", "raf", "rhe", "rja", "rsv", "rsw", "rph", "rau", "rmo", "rpp", "rre", "ram", "rmc", "ots", "ott", "wol", "wri", "wen", "wed", "wpi", "wbm", "woo", "wcl", "ama", "amf", "amw", "amp", "acn", "aph", "apy", "apd", "apha", "eru", "erw", "erg", "ecn", "ech", "echa", "echj", "echl", "echs", "echv", "echw", "echp", "emr", "ehh", "nse", "nri", "nhm", "mmn", "caq", "eaa", "rbt", "mlo", "mci", "mop", "mam", "mes", "pla", "sme", "smk", "smq", "smx", "smi", "smeg", "smel", "smer", "smd", "rhi", "sfh", "sfd", "ead", "atu", "ara", "atf", "avi", "agr", "ret", "rec", "rel", "rei", "rep", "rle", "rlt", "rlg", "rlb", "rlu", "rtr", "rir", "rhl", "rga", "ngl", "bme", "bmel", "bmi", "bmz", "bmg", "bmw", "bmee", "bmf", "bmb", "bmc", "baa", "babo", "babr", "babt", "babb", "babu", "babs", "babc", "bms", "bsi", "bsf", "bsui", "bsup", "bsuv", "bsuc", "bmt", "bsz", "bsv", "bov", "bcs", "bsk", "bol", "bcar", "bmr", "bpp", "bpv", "bcet", "bcee", "oan", "oah", "bja", "bjp", "bbt", "aol", "rpa", "rpc", "rpe", "rpx", "nha", "oca", "ocg", "oco", "bhe", "bhn", "bhs", "bqu", "bqr", "btr", "btx", "bgr", "bcd", "baus", "bvn", "banc", "xau", "azc", "mrd", "mpo", "chel", "hdt", "rva", "phl", "deq", "msc", "cak", "cse", "chq", "pzu", "brd", "aex", "sit", "rsq", "rde", "pde", "pami", "dsh", "kvu", "kvl", "pga", "pgd", "cid", "malg", "con", "hba", "zmn", "nar", "npp", "npn", "sal", "sphk", "sphp", "smag", "swi", "sphm", "sphi", "ssan", "sjp", "sch", "ssy", "syb", "cij", "aay", "cna", "goh", "acr", "amv", "gdi", "gdj", "gxy", "gxl", "rpm", "tmo", "txi", "pbr", "pgv", "acu", "acz", "afi", "sri", "tsu", "fnc", "fnt", "fne", "ipo", "lba", "smf", "phm", "paa", "nio"]

set6 = set(sys6_list)
set4 = set(sys4_list)

only_4_sys = set4.difference(set6)
print (only_4_sys)
'''