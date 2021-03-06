# FAÇA UM PROGRAMA EM PYTHON QUE ABRA E RPRODUZA O ÁUDIO DE UM ARQUIVO MP3

import playsound
import time
import threading

man = '''\033[33m
............DN............Z7........................................................................
............NI7...........?,I$..........................=$Z7??88....................................
............DZ8M,.........:,,,I.......................~NZI????????..................................
............=MMMD.......=M+=,,,,:....................?$??$$=??I??I?I................................
..............MMO8.....,DI+=,,,,?:..................?M?O?N?+OZ7N?I??................................
.............,+=I$...,N$+I++~,,,:+..................88$87?IO$Z8M$D7?7...............................
..Z+?.........MMM877II+?I$7I++Z?,:=.................7MMMM$778D8$MMZN??..............................
..?:~I+=....~?MM~~?I7?II$$7I77:7,,O...............I$NNZ8MMOOMMMMMMMM?7..............................
..,,+NM8II$7II8MI:+???+?ZZODI?=I,,8=..............8NMN7$77ZZI7ZZ$NMD??..............................
..,,IMMDO877I?$MM8+?II?+7OZ7D8II,,Z~..............NMODM$778DOZZOMMODZOO.............................
..~,IMNNOD7III7OMM:+II77DDDMDDZ+,,Z~..............MNZM8$7ZNNNNZZMMNMZNN.............................
..I,:ZMD8OIIIIII$M7+DMM$.....=MD,~8..............:M8ZMNZ$$NNDOZZNMMMMMO.............................
..=D:~MZ$OZZI7I?+$OM?+$M........$I..................7OMMM??I7ZOMMMMMM$..............................
....I+7$Z8O8OO??D:.:MMMMM~............................7NMMNMMMMMMMMZ................................
....~,:+8ZO8ODDD....7MZMMI............................DDO8ZZNMNZ8MNMMMMD,...........................
.....?,,:?Z7$M........MM=7....................IMMNDM7$MD$$$ZZOZZMMMMNMMMDNZNMMDODNN$................
......+,,:+$N.........7MOO=.................:8DNM8ZN7ZZ$Z7OZMOZZ8NMZ8O$IMM8O$Z$$Z$ZNMN..............
.......+,,:~7..........D+=~?.,...........ZN88DDZMM8OZZ$7DZ777ZZZNMNMD8ODMMM8Z$777ZZOMD8=............
..........I78.........8=?Z8OOO=.......=M7?7$NMMDMMM8MOI??7==?I$D77MMMDMMZZMM88Z=~+7ZZ8Z?:...........
......................7Z$I7778~......:Z+=IZ8ZZ8M7777$MI77I~=?7MMO$Z$$MNZZZZZNNN7=~IZZZZ7D...........
.....................?O7I7$77$?.....,M+=Z$ZZ$7I$OMNDDN8ZZ$~+7ZDDMMMOMM?7$ZZZZZN8$777Z$ZZNZ..........
.....................,MMI?Z$8MDO....7O?7Z7?=????M8MMZZMMZZMIMOION8ZM+~~?ZZZZZZMMZZ$Z$$ZZM87?8.......
......................8$8$$$IZMM....=D7Z$7=~~+??$N7$I7DNMMMMN7I777MI~:I7$ZZZZZNMNN8OZZZZ8MZZ?$......
......................DZ787$8MMM.....O88$7+~~=??7ZM$777$77O777I77OI==?I7$ZZZZZMM8Z$$ZZZZ$7ZZ$7=.....
......................=OO8O8MM7+7.$M7?7$M$?+=~??7$M8I7NMMM8M77$$MN+?77$$ZZZZONMMO7=~?77$+IZZZZO$....
.......................IONND$M7I$~8I~++IDMZ$8NOIZ$M8$NMMMMMNMM7ZM877$8D8ZZZOMMMM8?~~~=+==7ZZZZ8M....
........................NDMN$88?IDI=~~+?Z8MMN8OOODMNMMNM$8MNND7$MMZ8DDMMMMMMM8DMMM=:=+=~~?ZZZZ$M....
........................MMMMZ$NM+ID7??I7ZZMMMMZZZZM88MMMMMMMMM$7MZZ7$ZZZ8MDIZZZZMMMMMM$Z777ZZZZ$=...
........................8DMMN8MM8?OMN8$$ZZMMMDZ$Z88O7ZZMMMMM$7$ZNI7III$ZMMMMOZZ8N,..ZN8NDOZOZZZ7=...
..........................DNMMN8M7IZZZNOO8MMOZI7DMO$7$7$ZO8O$$$$DM$$ZZ7O88MO88NM....INZ7==?$ZZMZZ...
...........................OMMNO7M+?D8Z8MMO8MMNM7$77ZZDMNMMM8O77IZNMZ$Z8MNMDDNN:..N7I7ZZZZZZMMMMM:..
............................MM$$7$$+?DZZMMMMMMMN$7$Z$Z8????IMM$77$O8MM8DNMMMMD...$7$8ZZ8Z88MMMDNM7..
............................MMZOZ$MD?IOZMMD?MMMMMM87N8?==?++7OMO7$$OMMMMMMMM~...=N8ZZZZZZZZ8N8MM....
............................=MMMMMIM$I8NM7..+MMMMMMM$77$ZO8OZZDMMM8MMMMMMMMM=Z8ZII?I$ZO8ZZO8M8......
..............................DMMMNO8?$D,....:MMMMMMMDZZI78DN88DNMMMMMMMMMMM$?=?7$ZZZZ8NMMMM........
................................:DMMMM?I=.....?M77ZZI7?+???++7$ZZZMMMMMMMMD7??$ZZZZZNM8DMZ..........
.....................................,8?O7....MM7?7OMN$ZZZ88OZZO8NMMMMMM8DOZZN88MMNN8?..............
......................................O7?Z...=NN8D8DDNM88NNNMMNNMMDN8ONMOOZZZ8MMMO..................
.......................................DI7?.~M$$$Z$7$ONNOZ$$Z$$ZZ$$$8$MMDOOZZON,....................
........................................DDZ$8N87MODD$NM$$$88O7M$$O$ZNMONNOZ8MD......................
........................................OM8DMO7$MMMNOM8Z8ZN8O78MNO$$$ZNMMMNM........................
..........................................MMMMMMOO$$$DNMMNDZ$7$$88NMMMMMMMMN........................
..........................................=MMMMMNNMMD$ZONMMN8ZZOMMMMMMMMMMM.........................
..........................................:MMMMMNMNDNNMMMMNOOMMMMMMMMMMNZMD.........................
..........................................Z7MNMMMMMDNNDNNNMNNMMMMMMMD7D$Z7M~........................
........................................$88M=+?7MMMMMDDNNNMMMMMMMMZ=+??O$ZIN........................
........................................ZINI?II77ZMMMMMMNNMNMMMMNDI?~?7?ZZ7?7.......................
.......................................877$?7ID=?IIOMMMMMMNMMMD$7787+?7777ZI8=......................
......................................N$78$ZDO~~777?ZMMMMMMMMM$7II$ZZ7Z7Z?Z$=8......................
......................................8+$8ZZZ+~?7$I?I78MMMMMMMZ$7I?$ZOZ$I?ZZ?I......................
.....................................,7+7DZ7=~?7Z$?+$Z$DMMMMNM8Z$I+?$ZOD~=$ZI?:.....................
.....................................Z7=?OOI~:I7Z$??8$7Z?...NI8M$7???IZN7I$Z7II.....................
.....................................Z7??7NI~~77ZZ?DZZ7N....NN$D$7??~+7ZZ?7$$77.....................
.....................................D$7?$O?~~7ZZ$IDZZMD....:M88$7??~=7$7I$$Z7M,....................
.....................................$7I7Z7?~=7$ZZZNMM~.......NMD$??~~77$$$ZZ7M,....................
.....................................~$$7Z$?+?7ZZZ8MMO.........:MOI?~=7$ZZZZZ$M.....................
......................................Z7$ZZ$?I7ZZZMM=...........D87I=?$ZZZZZZN8.....................
......................................DD$ZZ$$$ZZZZMM.............O$7?7ZZZZM88M:.....................
......................................,MMOZZ$$ZZZZMO.............7Z$$ZZZZOMMMM......................
........................................M8ZOZZZZOMM?.............,NZ$ZZZ$8ZNMM......................
........................................MOZOZ88DMMN...............DMD8O8N8ZZMN......................
.......................................=87$ZMMMMM87................8MMMMO$ZZ8M......................
.......................................O7+7$8MMMZN:.................MMMMI+$ZZ8=.....................
......................................ND?+$Z77ZZ8M..................:MMM8?+7ZMNN....................
.....................................:O8NZZZDNZ7N.....................MMMMOZOMNNM=..................
.....................................?OZNZZOMD78.......................ZNN8ZMM88Z8,.................
.....................................$$ZMDZZZ$M=........................DMO8MMZ$OZOM................
....................................ZZZ8MNZZZ8M=........................8NMZ7ZZ$MZZ88...............
....................................$?77O8ZZNNMM........................ZZMD$ZZZM888M$..............
...................................?77D7$ZZZ8ZMM........................$ZZ8ZZZ8DZMMNM..............
................................,Z8$7$777$ZZOOMM........................M8ZOMNOZ8MZDNM~.............
................................8O?=????IZZ8OO8?Z7......................MMZZ77777I77~~MN............
................................DM+??????N++OOI7$8......................M$+++=++?++?I?OZ............
................................I$ZDOOOZMOI?OM78N+.....................?MM?I??+?8?+?NZMD............
.................................IMMNMMMMNMDMDMM$N.....................~8ZDOD7IDOMO7MMMD............
..................................=MMMMMMNNMM$$..........................~MMMMMNMMMMMM8.............
...................................DMMMMDDMMND..............................MMMDNMNMMMZ.............
...................................DMMN8MMMMM8..............................MMMMN8MMMM7.............
...................................DMMMMNMMMI................................IMMNMDNMM~.............
...................................,MMMMNNMM..................................MMMMMNMN..............
....................................MMMMMMMD..................................,MMMMMMM..............
....................................NMMMDMMM...................................NNNNDMM..............
....................................8MNNNMMM..................................~MMMMMMM:.............
....................................NMMMNMMM?.................................NMMMNNMMD.............
..................................MMMMMMNNNDM~................................MMMMMMMNMM7...........
...............................?MMMMMMMNMMMMM?................................MMMMMMMMMMO$..........
............................OMMMMMMMMMMMMMMMN.................................MMMMNNMMMMD8..........
.........................7MMMMMMMMMMMM$=.......................................7MMMM8Z7I............
.........................:MMMMMMMD=.................................................................
....................................................................................................
'''

def draw():
    for ch in man:
        time.sleep(0.036307624)
        print(ch, end='', flush=True)


threading.Thread(target=draw).start()
playsound.playsound('ex021.mp3')
