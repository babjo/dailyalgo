import itertools
import collections

class Solution(object):
	def palindromePairs(self, words):
		"""
		:type words: List[str]
		:rtype: List[List[int]]
		"""
		d = { word : idx for idx, word in enumerate(words)}

		results = []
		for idx, word in enumerate(words):
			for i in range(0, len(word)+1):
				word1, word2 = word[0:i], word[i:]
		
				if self.isPalindrome(word2):
					reversed_word1 = word1[::-1]
					if (reversed_word1 in d) and d[reversed_word1] != idx:
						results.append([idx, d[reversed_word1]])

				if self.isPalindrome(word1):
					reversed_word2 = word2[::-1]
					if (reversed_word2 in d) and d[reversed_word2] != idx and word1:
						results.append([d[reversed_word2], idx])

		return results

	def isPalindrome(self, t):
		return t[::-1] == t


print Solution().palindromePairs(["bat", "tab", "cat"])
print Solution().palindromePairs(["abcd", "dcba", "lls", "s", "sssll"])
#print Solution().palindromePairs(["eihhje","iaicac","hjfce","igbfbbebhbd","ad","bibhiibbe","bacfjiegaiibifhdjfa","bige","hhahbhjcfa","fd","bbbjdf","idfgbbicfdaji","ahi","djbcibbbjihi","iibcdebc","ijcccgdahhebci","jcbjiebefjef","gfaiahcegghbgjjhadf","hdhbjfdiddcjgejd","digfecfdgdhjf","beffabe","aaefeh","ih","bigdb","ihjeja","jebiaibeegjdcfe","cecjhghchfedajccf","hejfcdajiddacg","bjbhaabbidfabe","fhiaddiihgfcfjhaijb","cifg","gh","idf","hhabbcgehc","iagiighiegcfdibhb","ighagffcchabchjcjdi","hg","bchabcgjgdecdbbcd","cc","hibihid","efheeddi","effefgih","gidcahijjgcfchd","aaaehigebeiifahaih","daccjgajbbfhdjfcdja","aaehajdbehdggcaje","fafgbffi","eehg","iababficcfgg","aidajfegghidgie","bbbgddjbdg","gahde","bjgecf","ebbdihdbii","fcgjjaaiedijhbdjgebb","fcahabeghabedd","cechjeda","igcddjbhaibfdhbcfdj","eaj","jbhdigcfagbffibeib","ijedbahdbbibjh","gdf","iicefeg","idjceaegiefdfj","ahbahiccagicjgefaif","je","fid","jbjaeeghgh","egdajeja","jajfaadf","fcicdhigajiiffifb","ibgidhcabeiahfjb","dgijjfidc","bacaagf","ehdeiaihhag","dfedajcaahhjccj","fe","hedefdcideajbfa","edaaji","echaadjhaf","ejeicehcdbf","hbhaiagfibf","idefehdagh","eegajhgdgdajhbeehfih","aiggccddjhgibgifafda","dgacbidggcega","dffjc","fcacbddihjhddcddchic","gfhhhiaeaj","gahefhejfafbeg","dbjcjfecbefiddig","hc","cabfighdf","hahfeaiggfh","fffcf","edhdjgcefiigic","ihajbbgcfdeeigeief","gb","hcgjahd","ae","cifbbjiijjighjggeih","aabb","hcibebebihbigccibfd","hha","figija","jchhb","gfcdbij","gaefce","c","iaeeidacdgecbeigfddj","e","dceeicjgdef","gdedjebheiigbgeabig","hcbffcieieaa","ahabegeea","ebedigbgacjdhccae","ihibggcgddcgfabdfgc","ihefhaci","gibfcdfaejdbje","idfga","jfdideiebdghighhig","hj","agdcehci","d","begfhfjdfjiejcdc","hiiifgbic","hdffad","eggabhjjgiaffa","beie","jdcejcegfaffb","dbeaghihicdhhch","ijacdjehjace","iceabjdebdhihage","gjidf","cacc","ijjcahehgficehii","jdcahh","cefbccb","gehdefadigcbhjc","eifbhdf","gffcddaaagc","dcgh","dgjibh","cgbej","hieggchibcgd","ca","aaahhacigdijhfbcge","aieiacbbdigecjdeg","fgehighad","beeifcbcc","eej","eidcjf","cegj","aadgadg","ejjbfaca","ifjjb","iidcfffcfgi","ajjgdidcdbhdhdaa","ibjb","jaecgebbgdddai","bhdhgjgghfhhjji","begihba","dgghaga","ccjbfbjaeeijdjbhejh","cbehafbhab","cidafi","hbieghhihg","bdcgiacajgggeh","fjiadbjjhciaef","j","edggacbbfejebegjf","bbjfa","dijjebabfghfbb","bbcedcj","aehjcdja","cddhbgagfiieb","hejcehbjbgccbbd","cgbhcdahff","agjfj","diicicgbeafb","aeeedjjjdjchdgfahe","eajifceddbgfjifhcjed","bdfecciadadaief","hdj","cecibcdfhdacef","dbagafghaahjhfcjd","ejhcaei","jhcgbacbaddigjc","hjjecdifidhijbjighgb","hjjacdg","dfi","fbihiacihh","bghh","efgcd","jfcjgaiebdjjcffa","ihechjdghbj","eaafieehbbfjff","gdccieebfbgbag","becjfdccjbcbebiichch","becbachhbhahdieb","fdcafjjedda","icjjbif","efj","fheadj","dbcbjecaj","jjeffdhch","fbfdcdh","aajfeefhghhjhbga","dhhabdidcjbfhgfcdajf","efhh","ibj","dehiffcciaajd","jjfaaggebieejcfd","cfhagj","figabbieajcjiaiefj","djigagagbg","bcihbjjbbajhfbdic","bfdai","cjggjdffjbh","dfdgedacdhcg","ibiheccaefiefcch","jihd","jaec","bfbfjadchjjgiigcech","edfegfijcgdfhacjcd","ffba","hhciihajgebbbj","aihgcghcggbjbia","djjccdiffich","hddgbhagaafg","jae","cbaceaaedghceachg","hjjfa","hcgjafjcaihdicgajjh","ahgiebggjaf","daejeecaieceeci","jghdgfgfd","h","jahafifjdg","f","ifi","fifjiacjhdajjgej","bidd","edefbfic","acdecgjahgfcc","ij","dfedddejafeiggideib","dgj","ageaddjh","cbgceei","cigigiadhcgbbga","hbecjhb","acdhdeg","ijcceidjfjgiiid","fgfbiejfbdjjabjcabdj","gfcgdajj","hieijg","jfjabdeeaidfa","ejdchhbdeegiijajij","fdgjejjifedfbdfjid","adgfjicf","bggidghhbdjijghj","aacjghdfbeefgdhfbc","jffehjgcea","ciebh","ig","efifhjgbd","bdj","jbc","geehbhfdebf","degg","edaccj","dcidaeghihcddjiih","cja","egfjcgfgbcj","hfigfcb","gbedjddd","abbfbgahcajd","jedid","cacccejg","gejfjbfecjfba","aajfegh","iijibjifdgh","fbedighjfc","icjfjdhbabdcjh","gcejigfjhjfcjbiejc","i","ajjaigegcjfecejdahd","cij","ifaf","iajahaif","dhhgfaajfeig","egjhhggeeafjhjaiab","bjeh","ji","jgibdhjgieaeieefhcb","caibfa","aibi","iejdijbhej","efbdaehfdife","bebafghaaahigfc","eehjheh","jhibcgifc","bfibdhhibdhb","djdfeiegdecjcgcj","bagcedbaeaigb","gafjcag","gfeg","jeegbhbadhidbjica","fgbadbghhggeachih","gdbafiid","bcjdj","dbehadhghgfjidjdi","ifhefaedcjdac","hcgaga","b","fighadfjdfibfhgj","eifcjff","cjjfjcfhjjgebgeadchf","hdjecaefejiediea","eecjgbe","acidfcffaigbhihg","fjijafhbccahbijgjcg","eacbeigecdjb","ejaifghjbhcgaa","bcgfebjhiccegidg","habejifajb","hceaab","fjgidbj","hjigejf","jgehhci","eacfjcfjgdfiabgd","fbeicffedaeijifdhg","hifjacdhfchigcafcafb","cbh","bagejhibjaibajihffa","gddfecffdhabdbiab","ijbahagjcgj","bebjccbb","cggfhefibfafgaibdb","fbceacf","ccdbfbcdadbfbcfbd","a","fbhdbfei","eachgdec","ffbg","hcijfeafjhfdhee","chcefbjffbbeigh","aiga","cajbajjacddjegh","iejbidachf","fihfffhhch","dabagbbffdgbccfjbfed","jbfcjgighb","idbdfbibejebbbfchjb","bfdbjjjbadcgiahhieb","daefijicifagdffjdhb","daaicdgjaahacchj","egbddhefjhjcjgb","icdgegjcch","fffgejehebhd","ecig","haigjcccibejiebc","aafiahiaif","ecffghijaedhfji","fghbjibahcaejggh","cfa","gaichcddeaddbb","hgb","hiba","jjfejcfcgda","ihedbeihcbjfgi","ieicgehjhaefcg","dhbehfcijdid","fdeehiigbcgebejae","cjha","bhddajdcahbhdgefiic","jhbbcgcddijdfdgigeg","ejibhbabicdfeagcja","hbfga","hgfg","aigjjfabdgjj","gahjgafcdhgahf","eacbfhihhifb","jedjiijgiegabhgb","jbi","bi","bahagj","chjeigchhicjfhafj","ifiiehjfgjahfjigg","bcfcccibeefegfd","hfbbajbacfhcfhbfbiij","dejhf","jfiffjjddebc","aiadiighcch","jecjjagdicgfad","habgcc","jhbfihd","hidhbcibdbcjehadddi","bcbcgcgjfaaahhaadee","bcadddeh","ghjbjhjaedjgihj","eegciihejhghaeejjfcg","ddcigjfiicieedhahhjb","ffgdjgbhhdgjg","iihcijbbdedif","idbhbeicbafcbh","cdhdaadbhieigfbbhhi","fcigcia","ggjjbbggcacb","aceciiige","haeb","eaahfe","didjebhfbd","aeaagghed","ggjhe","fiacfacjfdggi","hfdahb","jfh","gdiigfbifjdbeijjhjci","cbhadedj","fdfccjaadehfddfhcihb","ahdiddbddifibejjiege","ebcgh","fgaffihebeaghecag","feidjefefcffiigchf","ibhbeedi","adbiffhddcdgfffagid","hjhfhbia","gegadcacciiefhbdacj","idjchf","agchhjbhjcia","idafgegahjiahcjbde","cfiibcjcechcje","eebgdjeifeej","bijfhedbhi","ag","g","iggggdejbdcibca","cdjeaeaahcha","dhgjjdcciai","hdjadbicjbgeddfgf","fjbcbjbeghcda","aegbjdiifa","fceaffjjihijebj","aigcifcfjfgheiafic","ecciaijcehcc","cahibcihifbhdideidf","idjdegg","cbgeicba","ihe","jc","jifdhga","jdjiedfggbidfibgea","dd","fafeajbeafhcdfhd","aabgbgaceeabdbiad","ighaeihihfjdcjcbj","jifgjdcaheeaghfigc","acedddibbcahfdh","fjahiajjeiicfcagcjce","eheg","idbificjffejiccbdh","hdhc","hjcibacg","eb","iacie","jbeiegaecffijig","eafgj","djgieedgfgadfjfajfic","gdhjfaidb","cedbgaicbgjjg","ah","ifjajeaggich","jgfgafaheebg","cjjhd","cfebhbigcidfaaghdh","fdc","ieig","abb"])
#print Solution().palindromePairs(["a",""])
#print Solution().palindromePairs(["hijcjdgbjbbiadhjfde","aabjfebbb","ccjihjifcedecihece","bjfadagabedijaaigaf","igeebfb","fjiegjcgbddjfadg","deeifhhff","biegcbiecfe","ahhddaccffcheeg","jfdfjjbiejdafbhf","ccdjd","gbhhfibhceagbfgg","gddjijhb","dbefiid","beifgfhaffbjigbeifa","dceejcdfd","a","gebfbccf","ccgdea","jehgiabgejiccagcce","ehhfcieaghihjcce","gciihiaddja","aefheiaehacgf","ddebdjbhdadh","jccjjfdbhaddbcefjghf","dccfdd","dggiifjecjgejafhaedg","cejgigbhhicjbcejjba","if","eebjdhhheehjbdhajb","hbiafbaghadicebfj","fhabgehacjha","iaaigafecbheagbebhi","gibfcabaaidfdbcf","cdcghacaeebahjdajbd","aadgcdhfag","iidbibhaifegadaifdh","fjjdhdjf","ffaacedbiacdbeegcbc","idebegfgh","fdhbdajafiadbbd","dgagfcgggihjeadhehj","ihafdjdeegbjbghhjhh","faeji","gfa","fiieffecgaagebifaij","bidjibb","abhehhadhcif","cgbffi","ahjbjfiibdia","ghdbdbcbdehia","hghbbigehecbdfghef","hgfc","jbebiffcdd","ecadfjhdiaj","ghchjiejfaijhfajhcc","jibjbdjebc","ic","ghhbcjefdfgfeff","ddcbieigci","ihafafhdfagbb","gbdifdeedhj","bdgaaiibhchfeffadh","ebf","i","ihfiidcifdhjjicdh","heahgahjgaejci","dgbcgjef","bahjiefeihidb","gdgafcghadh","fcgbiefaigfgdcdi","aahaijbajedidgbbja","faicihifbfhfjjaga","acedheafcbcbjcdcgg","ebbaaigccghdf","gfjjadigagb","deegghdgghdjiijfa","agaghehcfaifedebhibf","eifdfajdeddicb","bbjdihigccehc","dbbjbdfehgfagaic","bbgcdebifeijc","afibbdidaad","gj","gjidegcfgd","ig","jjfgjgffihgiacfcih","cgbf","cieghjajag","aeij","ecciaicabbeedbif","bif","eb","gdjcc","ebeifggiaicihfgdbjb","didgjggfdighd","ccjaaadadebcehbg","eaiidjijbafdagab","eahbgecegabdebfeh","bjb","jbhi","c","fcdeedjjeghfhi","ih","hfgjifjffc","ajdhbbcgg","efbifc","bjjeaedbieeffc","eibcjdb","jdffcgighejgfbfgg","fgeghgddhijhi","ggacafige","cecjjdficdabg","eifj","fbeihd","dciibh","b","hifcgj","iceea","fifieaaifcaehfhcggga","dbifdidd","jiechicgbfajiifg","hfdfbafdgiiegjig","jgd","hbehahjb","di","id","bfaajhgeabcfjed","aeaecggehi","jeiedjjhedcdici","hbhiheij","jei","jcchhea","fbhgidaiaeh","efa","bdbbgaecahhjbic","ijggebhc","icjehchdc","gdeifdc","ae","ibfedjbhgejai","ebdgdjhiccaddeajf","aj","jfifjcejd","acfdcdhhaicfgjhg","dggjig","agjcghcjfgjcc","gfjeafifgh","ghecfefedebegdgieiha","hcaic","gebbgiafahddbaagg","biiadcjifedei","h","feiagajfhaefhehaej","eecjggdbgcajefhec","hdegdidaehfi","bb","hgghcfiiehhfiahd","dcahagaajeifchb","afcacd","efdgbe","jfjidcheheiehfeggbfa","gidbbigcdhee","gbijihf","igifjceehbffccgdcj","fhecgc","gdehbaegf","edddi","jb","cjhgfabeibjbeieacdh","jgfjah","efadfffheeiejg","ffeibeiffhbgajfgffg","fccgd","fdbjj","fieajhgeheiegc","iefjjiefajiei","fejdjdjd","ahgeeh","jjf","cbcfigchadada","iacebff","ighijbiijjefgafha","ehhfdbiia","cddajdfhiga","gchdaheaigafgddgchh","ijgih","caddjdca","eiebcbcgjbggfhd","bacj","idiaci","jadff","jbhccfdadbehahd","cfjbfhica","igedjbjgddcbjffah","hfdcjbgfbajcaiaagdi","bdaef","bcjcifjigeeaibgfbc","hejiddfajcgddd","jfaiafgfejde","jdhiccaiagehidj","hehfe","dacdegdcddiahbahji","haibiiaigd","fdh","hcghjdddjhfhgieegggb","bjecabcdehfejfb","djdefed","ibjdcgihae","ahffieb","jf","ff","ggjggjhabdihjdfjecjg","jfabbidaefgahefdei","hadeeadcejfehjd","gidheefaicc","ej","dfhabffeccjcibefci","cidbdcg","hb","cgffe","acbfjeieaifacf","diaggcieaejdjigjbcea","hbbbdbihicaibd","jjhifhefcbdfhjacdabc","ggcdachdfd","dcacfgjecfc","fgcicafdgbjah","bgbchfifhfcgjah","fcejdbfhbjiagecbf","idhb","jgbjeddfjaibgegcih","jafje","hcjebb","jageafjdcgi","bbj","f","egbeg","caiacggabbadg","dic","acbgdfaedieaeaheeeg","ag","jfihifdj","ehiihgaegdafd","cbefbjihcdie","hdjaehdfeffchfgb","jhjeadaabehcefjie","idjafeedidgdca","dgfeahccjiihgaihg","hecb","dafeeg","hieficcjedgcjdagaae","ebjdfj","hcbb","igfaghfdbggjcafaaeb","bcfiaaagih","dabefhdjcjjj","hcgcicedb","gceccdibgabbdfhg","fcghfag","cfhbbcbcbiaaedjde","jhicjgciahhcaheejgde","ddd","haahehh","bceafgde","fecbgadcfcgf","cacce","hejegff","dcbgcdcfefjef","dccd","aahgiicedbfchabhbab","jefdaghhgea","jaahhjfjjejf","fechde","gjfjgagecgag","gjhhfgghfjcegdcjg","j","fedfeidecehebd","jadijbhfachfihj","cbbifbdchdjdbfedcj","jfdffcjbdd","jah","fibfchdhebgbhiccicjb","gaefaggfeeigec","ghddihbeahgiiecddf","cgeidecfgcibbdjjbdia","bhgbjaiga","eagjbhecjfi","efadfaagffec","dfhhichiacigfci","chiddabjheejaedffjej","fdbbjjff","jccicifhdidgcbeidhg","bagcjdcahadgbcjjcae","bacefgjhaegjjjebighe","iebdcdfbdfjhggeijjj","diggaffhehddcbdbdb","dccibceigejejajcbb","cigfccahehiajh","dcdcddaeaiiab","babgb","fgefhcdccad","jfhdjfhd","behiecbheajhdffhgdb","jgjifhfeiihbedghb","ijccgic","ihcheag","jaieb","jeadbfa","cibieadhedhjibgfcahh","afbdejj","fjgjgfdicji","bajdfagejj","jieddaceeg","hhcegibedabjadgfh","ajgaabbjhda","aagdjcdjbgjcegaae","d","cjddfifadefaciehbi","icajb","bafcicgggcjf","cdhjb","djccfe","jbhdcbcceadebfeji","idahjfiffaf","gcgideehdcbj","ibgcacajcagaeghdf","gigjaajjafbfheh","ijgb","gieegcbhhdaecacdgieh","bghbahaecdfbgdide","bdccaihabgjehgjeaghg","aiagbehafgijijbdag","edhb","fgjcecbdhhaiiccbia","jdd","idddgb","cbcb","igidhihabifhcgfee","cdababfihac","bjdhabfdgfhbad","edfgejaia","deccfgebedif","ea","dafbjiihjgcdabijadej","gbhecejheiieidg","jhcegjhibjcii","ddjbcgabchb","gcijdibcbbci","febbibijadefhf","edcaeabidjfacjgjjhi","fhg","jdie","ficecjfbj","hfihhjbbceae","jfiejggiadfj","fhfjhihdh","aicddh","eehccjdbjdchefef","bghbade","ijcb","idbbchbgcga","ijgbjdbdfgihbagg","ejeficfdf","ghjbgcjjbaebiiihfeh","dijegde","dgb","ef","jjc","cbbbie","adgifgegdabhdjgi","cighdhebadcegbggff","dhdia","bfefcdhddjfid","fbajejhdehcbedhbaidd","ijcg","cehajfaihdfbeaffb","cegedjebejjje","fbgidjhhccijhjca","ebageaccad","jehi","ghfcjcifdf","ffgegghecfg","dgggejbbjiaaijfbijcf","dabbdijgajed","dfcbaa","hehfgieid","fdiihhgiiaf","dadjidabfgegbai","fehd","eahddeiddcgchej","gcg","cefjjjebccbegiiabibg","ghgcfbhdffd","dcjbcbdjfgeadg","ijjc","hgegjbejiefghdchfj","hef","aceegaea","hebigcbghfdiifghfbag","feebfgcgeb","eddffchdadabhhadde","badfahbhbbgdddhdjgge","ihjgchdiehaabfgac","cehiecijjfjabjhffbia","jadfdada","dbhfg","chgedbiacca","bjcii","jabfabjjjf","g","cjcaaaacdcdifibh","ehbjai","fehcggfjcjiaiiedbf","cfbaeafdciiejej","bh","gajacadbfeggeaeh","jjjefcg","jbac","ihdcfidheajahebiiggh","ieigedcgd","icdjc","figbidjihcjhe","gccbeggdafagc","caeffbdcgjfdd","ggeaadfhgdd","difigbde","eeddjciehc","iaijbgcecfhh","icibbfecfhdhdhdehda","acfajfejdhjjdh","bjadjghecdgi","bjecibfc","jfcdc","ia","ggdhh","hdiabjbhdjafd","jcgcaegcjjbfgehh","jeigjdihdijdgde","cegahcgceh","cade","jejjbedheagiaac","fhbhihbfabgbaa","iigjiiagi","fh","jfjihebjcdeade","bcjbjahijc","aiccjfa","dd","ijggjhjd","eajd","hbggcacefjcf","ehifjcibggiafcfdf","fbhd","cfgbbf","ec","dhicegfdbcgfebf","fcfg","hcaibdfcacgfiajef","dajiahcadedjdgi","bhgegjbiabjjb","jaehacaaheageb","gjecfejajacacfda","hijhjjbdjbihfjicbda","ccih","eajfjgadefagiijdbjf","aeihhcbcejedbg","hgdhcjfidfcbadfafab","hh","beghhhdagdeihaeje","jhgfjdeebhiidbech","jhcbjhidgcfafiejeeb","ebaiggjjheieefaa","ifiagbbbibcdfhg","aig","dgbihefcjhiiheehi","jcgaieehcbgg","ejjhchgfiijgjeghd","hehcicbdhecec","aaheadhef","eefdgaebfaacgh","hheaihdifafbjffgjf","iaadg","gadcc","fddbhgaifg","ffbajaghchgbcghda","eaddhggebdgfcjhfi","bgebjbehfigjiagcbi","ibebfbeeagbdgfccfce","jabcfaife","ihehicghghdgaejj","aaehgjjfbc","dbbhibhdcgagacebc","ecdjedaihgejhgice","fbecgbigidcahhb","dghgfgieijb","dejafcfideeifbch","bibjcac","aajh","jaehgib","aeaicbgadaa","hcdgaffjhdjcdf","beaagifehhdfgbjedeh","hfacddfajj","bjhggjehhcae","bcjbgdaj","chfg","didgg","dbbddhhijfaajhfe","ac","dcfh","hahehjhhhhbfj","bebhcifdfbghf","jcgc","cdfec","edg","eeeehdfeiff","hiaibaibha","jefgijbhja","hbjgjaffchjcbdjbed","bchijibffjjf","djfjichd","icggjcaihihabaa","ahbd","ghhgjg","bejhbdjjdjfhbhhghgcd","gcgahfdbjfigjedh","abcebgejcfbjieccighf","eah","ggificcb","hhidgihbdedgecd","ebchehbchhjacjjcd","biffheficgfbbg","fibegf","dhejecjijiaggefd","adgcejjjgccfbai","iifabchibccbeidc","bfgifjfjdbbfagd","gjcbaeh","hdbgg","e","ejgfa","fbhjihfeaebdabhdah","aaadeejgceifedjeeabh","igdeg","dhehghjbebcj","biagh","acbfhegcicegdhgjee","ggjgbghchef","gjbccebijdfgd","egfbbbjih","dhc","dhdgjjbgjf","gegej","hcbeceehbgdhdfebhcda","ghaahf","caih","ij","eeefgjaf","baf","fc","ihjdhhch","cjjigig","fhdhaajhgbfhaehd","fghdfbbabahcacdfc","aaa","bfba","jbefbcbcdgjeejiegb","cbhidhiejcjgbbbfegbh","dggihihbgdide","ba","cehjajjhadbi","hhfgecgia","agbae","ifbajafhejcgeddihc","bdheeedidicheebaj","hddhab","haagaddihidbgbg","ggiijcehffbafeffch","eacegcjhdhgadhbch","ehgjjgcd","ifec","dhfjcgdjhfacjadc","dbgbibecch","gbdiicefbbdeiaba","ahch","jbggagbcaeei","ieccj","becchbgjfbibjfif","gbadchibdjhabf","cjdiaedbddbbcdghifb","bcahdadibf","ifhidjhieieid","egda","jahcaedidacgj","gdchcfejggjahac","ffifhfiaiebigfihbibe","dibiecjbgfaehfbeac","hdcbcabiha","ebabghegci","hehgafjhbdab","adbhfif","chf","abgjih","heajibdeijbbefg","ihifhcg","iiacfghcgageahjgc","gagcdjeagciffjdf","jbbffigbijfhe","jceeiiehcddfaf","biigff","chhe","cehfccjg","dcgdjgjbhcihbc","ffihcaeedahbdffdg","bjje","hbhajhfgjghib","ifehchafhfiejf","bidbee","agfhigiafdb","cchebcdfhhcg","fbd","iiajbehe","defhj","af","dcjedeajdhbefe","aacd","icebiachfd","fjgfefbaicjhb","hafjhgfcajd","fbjb","ighhggfbh","jciacdee","idcjabji","igjbedcaajhijjchgf","gihjedhihdaafgcb","ihfejageebiddec","hafhjfede","edc","fahgdcb","ebacbhe","giifigfjfcaebibb","ahaaebaegbdf","egfhfihjjc","dbfgbfacb","adjjhbac","dbgheicidfifg","gceidbacdccf","hdegh","adea","fdeaafbcga","jeddcaejaaehdfggggg","abjbhfj","hefcahbccagidj","dh","ajebfgagbbjfagihcji","cffb","dfbh","ejh","idj","efaaegiedcgcdg","addecjajbhabbbi","giecgacdihbgbdg","igggaefigfbiife","ecaa","eghjfhdaihjahb","ecddfgghbdabfjfi","dciihidci","bdgbjajgcbbfjfcci","bfeccdgb","daajcceciead","abicaffcbfci","haahgadjgbbddje","hjfgaifbhbfh","dgfcbefgghaiegeeihgb","ijjjbcjgb","bcjhfgbfjejggdg","iibhhgdhfhhfage","fbiiead","aefjahhfheebjjd","fcbbbfdfajhfed","hahgfeaf","jjfccfiec","aejbdfjjfcdgeeadf","ebgbhcihdgeijddai","aihicfjb","dfhbefcijfdhdfecde","ad","hijgjbccdfedgdibef","ebeiihhbgicea","hgfddfjgjghbg","bdbdacdh","dhgiggaffbe","fijfhfajeh","icfcjcggbgcaachjec","idbfjhefjffgchi","bhgbdh","gffdfchfai","ifihffiieie","chefhccgjcafcg","bjedjfd","beae","cbjificfaei","jefaejcie","fafbadgddaighi","ieidhjjf","ahcgehfajcbbdbcjed","jdajijiddjjheiha","geegcdf","idebdegbghjje","jddeihachbfbeehhcea","cj","da","aiajdcjfhggcjfdbc","hgdge","aghadabbicehbgccdb","efjcihcife","acibggicgfdjaab","bijfficfh","giijjbjjbjiif","ihhcbdciijihghffdf","bhee","fgajebjf","deggij","hcafgaeeijciaee","hhigjihigadefj","cifdf","dcfbd","bjfhcgbjcijbbcgjbccc","biceaeicfjgicb","fcjgdj","icbeadjjgeachahcjhja","hjhbdbhaijcijahcgjc","feicgbdeffi","chfehefedaijh","gabecfjbfciihh","gbjhdf","iefihhbc","iedhebcagbddaj","ebbfgdfeiacifchhijb","ebfhfehiabgec","jebjgbegcffdhj","afehjgiahddfidcf","haabciggihgdejceejii","haibechfjjjbigbhbabi","afh","igahiahie","bcj","dhgce","iedgjggbbjcchjajbj","ahbjadaif","ggafjgfejd","bgccdhhghedcdfgejd","iibafehjedbfadgde","hchffejfajjhi","aahbdceciigjahb","afhfaahc","afjaadadjbcf","aafh","fcbgagagbgec","hffbgjdcdhjajcfia","eahacidjedicfeb","eghdgegjcjg","bfiiaahdhiibj","cfgeh","ccbhbjeba","jahhjhgjcjdhfjcged","giifjfbhhja","jcjfigi","jdhgijchiabceddgjfcg","acddbjahbjfhbjiahigj","giijeaegidgjda","fafgegejhgdg","ahjggebfhde","hcehiahb","cibgdigghhe","hhcdcg","hejaiaffb","db","jhiedhieijceiiaj","jecedfhicbdh","ai","eijejidii","ffgiecajjcegfa","cefbdcjb","hahdeeihhcdfjid","bcdjedihhe","aiihecffegie","aegaeajbeiecdeb","jggcgdifiaiichegf","ddbdijh","ccacd","fabjbfifiiacfbfcdfjc","aibicaiidbffj","eiidfcjfcc","gabg","eicfjhgafgid","eggajdficbjaj","jbhbcgadcjhjgg","ajiahaghafccdhediea","fcaadegdcdaejdgf","fihh","bbgcdf","ejhcadjjccbjg","adgi","hgbabbfijecefi","ffbhdjgiebbajebeg","ci","igigdijbgjiihdbb","fbefghhjghfch","gfgjaaghgbiaciai","ieibbjcgb","fac","dceaahgcehjhh","fi","bdbfhejeidfjhdjcee","jbaccdgh","gahcfhic","cbcbdcihiidi","ieiaeecfbj","dfgecgdfihffiaec","egg","ihb","aegigfafdgddhfb","ebhddcc","dgagaidahg","ebgefdbchcccigheacg","ffdhbci","abi","ibad","cghbdgedceiecihggih","ihebjai","jfdgeebajhjhcfhea","ficdgebhcfgbbfe","eidcdghdegc","abhfgddc","ajf","jcbig","fgbjgegeccfgd","jifbfbgic","jdbgaai","fifafbeda","ibe","aahabgihgfbbiif","jjcicbjdg","jceeicigjagjgifacadj","fegiidiafejha","ichbbfjdbheajgcgfih","afahadggbeajjcig","iiedjdjedjccbh","jehjgidffggeceg","fbhagadd","fhbdgjibfficffg","aehhfifhddjgjhihacj","iffj","abhbgejeg","hggegidhfijbec","ifjgdddddbgg","ajididb","diddbfbhhaehbbeehc","cidfegagf","gfibgjefeeciieja","ccfbf","fb","behebeiddgjcaajhjb","cbgggi","caeid","bfg","gdcja","becjej","aiaeac","gbgafcbhhggj","dig","afgihid","gjefigjaahga","gdcd","jibifdedi","hjdgiaaadgf","fjghiigagjh","dabdacadbcjcgjbaf","bjh","cbgeebgcgajgjej","jbfhhfjicaieefdfbfif","hcjececficjicc","gafedgj","ebbhbhcjfagbeehb","ihfihfca","gfccjhdagdcccicdi","idbjjaaejha","dbcbedgdcegd","eceb","cihgficcbjifabeabj","jbjgijhefgjfefgbjji","agdefbafeccc","bbjbfcjd","becae","ch","ejbcdiibaahjhicac","aecgjacdbjhbcgb","adhhacbjjhijadgjhgja","iiahjeejhdcdbdgej","jifjdg","dehfcbc","iigiehbigghaccgc","eajggejbfaga","bfhggejgdc","jgf","eacfgai","gdgbd","abeigg","bhjbcgeafjfacffegj","ebfcjggaidfcjcegifg","cbegij","bibdjjcc","ehhagcb","gffbbcgceafeacdb","ijebgdjdagjdcjbicfhg","dhahegjhaebeiibdiea","bbfdif","jeajed","bceahbjhdhd","acibiabgadadae","cecfcbgjb","eibdhjaah","hfiifdgcggffbbdahdb","fgi","jhbjf","digfifceg","iehebh","hbbdagaijgbjjcfjjda","gbibfjeficeechbbcj","chbdbeficbbii","bcdfaaff","bbjgebe","dcdfdbeaiadba","fad","ghifddgdhbciiaab","jheh","cbeaaa","igchfdeedfjfcg","cjaijgigfiheiiidghbc","hiajdfceabi","befffijbbjaabae","cjdhihcgijihfhhdbdb","afgbebdfiiaibgfadbbf","bbaagib","cbhchade","eaf","cfdecebacfcigfibccc","dfbadijhgjig","dhj","dhjgagbcfiiff","fchcgjee","jabdhd","heaieeifdffjff","gjidbieejcjgbbdedbe","de","fjdegbiiebehffcfchhb","iiehfddddge","dgijgbihgfhddahcc","ifcffcfighdhagfcdgje","hbeafcgcigdciade","hdhfjijjfgfcecaagige","ecgbceb","igdhcjccdg","fe","ehfdghgebdjijc","hbgfcahchdadhef","dhiag","fiijdiigdh","aiehaffiaggbiah","cejdcbcceahbdafag","jifjggged","gcafcjdfhchdceij","ejjicbjbaefihhda","jhba","hhidfcbje","hbiefdbha","fdhbjgicfhfefhegide","ieccigeaifejj","ibjccbcef","gfdceabedbd","iiffhdfhbbjdjeh","bdbdjhabhc","fcdeddjgjfgbabacaej","iifgficfiegbfjfbeh","beegijhejaiacige","jddehhifcdcbfbdde","bccbbae","gfdffggbag"])