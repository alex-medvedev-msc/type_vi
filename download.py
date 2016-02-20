import requests
import requests_ftp
import csv
from bs4 import BeautifulSoup
import pandas as pd
import gzip
import shutil
from time import sleep


organisms = ["ece","ecs","etw","elx","eoh","elr","ecc","ecp","eci","ecv","ecx","ecw","ecy","ecr","ecq","eck","eum","ecz","elo","eln","ese","eso","esm","esl","eko","ekf","eab","eih","ena","elu","eun","elw","ell","elc","eld","elf","ecol","ecoi","ecoj","efe","stm","seo","sev","sey","sem","sej","seb","sef","setu","setc","seen","senr","spt","sek","sei","seh","shb","senh","seeh","see","senn","sew","sea","sens","sed","sel","sega","seec","sene","senc","ses","sbv","ype","ypk","ypa","ypn","ypm","ypp","ypg","ypz","ypt","ypd","ypx","yph","ypw","ypj","ypv","ypl","yps","ypo","ypi","ypy","ypb","ypq","ypu","ypr","ypc","ypf","yen","yep","yey","yel","yew","yet","yee","ysi","yal","yfr","yin","ykr","yro","yak","eca","patr","pato","pct","pcc","pcv","pwa","pec","eta","epy","epr","eam","eay","ebi","erj","plu","pay","ptt","enc","eno","eclo","eec","enl","ecla","eclc","eclg","ecle","ecln","ecli","eclx","ecly","eclz","eas","eau","eae","ear","enr","esa","csk","csz","csi","csj","ccon","ctu","kpn","kpu","kpm","kpp","kpk","kph","kpz","kpv","kpw","kpy","kpg","kpc","kpq","kpt","kpe","kpo","kpr","kpj","kpi","kpa","kps","kpx","kpb","kpne","kpnu","kva","kvd","kvq","kox","koe","kok","kom","kmi","spe","smaf","smw","smar","smac","serf","sers","sfw","sfo","pmr","pmib","ete","etc","edw","edl","ddc","ddd","dze","dzc","xbo","xbv","xne","xnm","xdo","xpo","pam","plf","paj","paq","pva","pao","kln","pant","panp","rah","raq","raa","psi","ebt","ron","cnt","cem","ced","pge","hav","ksa","kin","ebf","aap","xoo","xom","xop","xoy","xor","xoz","xtn","vch","vcf","vce","vcj","vco","vcm","vci","vcl","vcq","vcs","vcx","vcz","vvu","vvy","vpa","vpb","vpk","vpf","vph","vha","vca","vag","vsp","vex","vfu","vni","van","lag","vau","vcy","vct","vtu","vfi","vfm","awd","ppr","pae","paev","paei","pau","pap","pag","paf","pnc","paeb","pdk","psg","prp","paer","paem","pael","paes","paeu","paeg","paec","paeo","ppu","ppf","ppg","ppw","ppt","ppi","ppx","ppuh","ppun","ppud","pfv","pmon","pmot","pmos","ppj","pst","psb","psyr","psp","pci","pfl","pprc","ppro","pfo","pfs","pfe","pfc","pfw","pfb","pff","ppz","pman","ptv","pen","pmy","pmk","psc","psj","psh","pstu","pstt","pbm","pba","pbc","ppuu","pdr","pre","psv","psk","pch","pcz","pcp","psw","ppv","pses","psem","psec","avn","avl","avd","sfr","sbb","swd","psm","maq","mhc","mad","mari","psy","mvs","ttu","saga","mmt","mah","tvi","hch","csa","hel","ham","adi","mmw","mme","mpc","tol","tor","oai","gsn","aha","ahj","ahi","tau","gap","fpp","salv","cvi","pse","rsl","rsn","rsm","rse","rpf","reu","reh","rme","cti","cbw","bma","bmv","bml","bmn","bmal","bmae","bmaq","bmai","bmaf","bmaz","bmab","bps","bpm","bpl","bpd","bpr","bpse","bpsm","bpsu","bpsd","bpz","bpk","bpsh","bpsa","bpso","bte","btq","btj","btz","btd","btv","bthe","bthm","btha","bthl","bok","boc","but","bvi","bve","bur","bcn","bch","bcm","bcj","bcen","bcew","bceo","bam","bac","bmu","bmk","bmul","bct","bced","bdl","bpyr","bcon","bxe","bxb","bph","bpy","bgl","bgp","bgu","bug","bge","bgf","bgd","bgo","byi","buk","bpx","buo","bue","bul","bub","bfn","bbr","bbm","bbh","bbx","bpt","axy","axo","axn","axs","tea","teg","tas","tat","put","amim","aav","aaa","dac","del","vap","vpe","vpd","hse","cfu","care","lch","rge","azo","aza","azi","dar","ant","arc","pca","des","mxa","mfu","msd","age","scl","scu","ccro","samy","mlo","mci","sfd","rec","rei","rep","rga","azc","rsp","rsh","rsk","pde","psf","amv","azl","ali","tmo","nde"]

def parse():
	with open("table.html") as f:
		table = f.read()
	soup = BeautifulSoup(table, 'html.parser')
	tr_s = soup.find_all("tr")
	results = {"organism" : [], "pubmed" : [], "ncbi" : []}
	for tr in tr_s:
		td_s = tr.find_all("td")
		if len(td_s) == 4:
			results["organism"].append(td_s[0].a.text)
			if td_s[2].a is None:
				href = ""
			else:
				href = td_s[2].a["href"]
			results["pubmed"].append(href)
			results["ncbi"].append(td_s[3].a["href"])
		#print(type(tr))
		#print(len(tr))
	frame = pd.DataFrame.from_dict(results)
	frame.to_csv("results.csv")
	filtered = frame[frame.organism.isin(organisms)]
	filtered.to_csv("type_vi_organisms.csv")


def unarchive():
	import os
	genomes = "C:\\Users\\ag3r\\Downloads\\genomes\\"
	extracted = "C:\\Users\\ag3r\\Downloads\\extracted\\"
	for file in os.listdir(genomes):
		with gzip.open(os.path.join(genomes, file), 'rb') as f_in:	    	
			with open(os.path.join(extracted, file.replace(".gz","")), "wb") as f_out:
			    shutil.copyfileobj(f_in, f_out)


def download():
	#url = "ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCA_000006665.1_ASM666v1/"
	frame = pd.read_csv("type_vi_organisms.csv")
	requests_ftp.monkeypatch_session()
	s = requests.Session()

	for index, row in frame.iterrows():
		if index < 150:
			continue
		response = s.list(row.ncbi)
		for line in response.text.split("\r\n"):
			if line:
				for entry in line.split(" "):
					if entry.endswith(".gbff.gz"):
						result = s.get(row.ncbi+"/"+entry)
	    #with gzip.open('/home/joe/file.txt.gz', 'wb') as f_out:
	    #    shutil.copyfileobj(f_in, f_out)					
						with open("C:\\Users\\ag3r\\Downloads\\genomes\\"+entry, "wb") as output:
							output.write(result.content)
						print("%s organism %s downloaded" %(index,row.organism))
						sleep(5)


def main():
	unarchive()
	

if __name__ == '__main__':
	main()