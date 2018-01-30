##ResultsFolder = 'C:\\Users\\MasahiroSakurai\\Documents\\SmashStuff'      # Make sure to have double backslashes file paths.
    # ResultsFolder may be left undefined if result .txt files are in the same place as the Python code
DefaultTitleMin = 2
DefaultSort = 'Low'
DefaultSortTie = 'Middle'
DefaultLines = 2
RoundLen = 2             # How many Digits to round to in ranking displays
Rounding = '.' + str(RoundLen) + 'f'
DefaultRating = 1500
DefaultRD = 350
DefaultVol = 0.06


# Tags and names go here. There should only be one tag per real name.

TagDict = { \
    'MaNg0': 'Joseph Marquez', \
    'Armada': 'Adam Lindgren', \
    'PPMD': 'Kevin Nanney', \
    'Hungrybox': 'Juan Manuel Debiedma', \
    'Leffen': 'William Hjelte', \
    'Mew2King': 'Jason Zimmerman'\
    }


# Don't touch this.

NameDict = {}
for Tag in TagDict:
    NameDict[TagDict[Tag]] = Tag

    
# Any tags with numbers in them should go here, with the actual tag, then the tag with numbers written out.
# Note that tags of the form A1 or AA1 (that is, a capital letter followed by a number or two capital letters
# followed by a number) do not always process properly, and additional coding may be needing to avoid errors.

NumFixes = [ \
    ('AndrewAjt62', 'AndrewAjtsixtytwo'), \
    ('EMP P4K | Armada', 'Armada'), \
    ('P4K EMP Armada', 'Armada'), \
    ('P4K EMP | Armada', 'Armada'), \
    ('baka4moe', 'bakafourmoe'), \
    ('Carls492', 'Carlsfourninetwo'), \
    ('Gninja64', 'Gninjasixtyfour'), \
    ('482 | JSalt', 'foureighttwo | JSalt'), \
    ('f00', 'fzerozero'), \
    ('Jake13', 'Jakethirteen'), \
    ('j00t', 'jzerozerot'), \
    ('Kiw1', 'Kiwone'), \
    ('kukunok0', 'kukunokzero'), \
    ('C9|Mango', 'MaNgzero'), \
    ('C9 Mang0', 'MaNgzero'), \
    ('C9 MaNg0', 'MaNgzero'), \
    ('C9. Mango', 'MaNgzero'), \
    ('MaNg0', 'MaNgzero'), \
    ('PL MVG EMP Mew2King', 'MewtwoKing'), \
    ('PL MVG mew2king', 'MewtwoKing'), \
    ('EMP P4K | Mew2King', 'MewtwoKing'), \
    ('P4K | EMP |Mew2King', 'MewtwoKing'), \
    ('P4K EMP | Mew2King', 'MewtwoKing'), \
    ('P4K EMP Mew2King', 'MewtwoKing'), \
    ('P4K Mew2King', 'MewtwoKing'), \
    ('CT EMP|MewtwoKing', 'MewtwoKing'), \
    ('Mew2King', 'MewtwoKing'), \
    ('M2K', 'MewtwoKing'), \
    ('Poopmaister6000', 'Poopmaistersixthousand'), \
    ('SFS KoopaTroopa895', 'SFS KoopaTroopaeightninefive'), \
    ('[62Bit] Bladewise', '[sixtytwoBit] Bladewise'), \
    ('Smasher89', 'Smashereightynine'), \
    ('S2J', 'StwoJ'), \
    ('S0ft', 'Szeroft'), \
    ('LP.RaynEX', 'temprayn'), \
    ('RaynEX', 'temprayn'), \
    ('VO1D', 'VOoneD'), \
    ('X1', 'Xone'), \
    ('Cornholio69', 'Cornholiosixtynine'), \
    ('Ycz6', 'Yczsix'), \
    ('S2 20XX','STwo TwoZeroXX'),\
    ('GamerGuitarist7', 'GamerGuitaristseven'),\
    ('101.5 "The Hammer" FM', 'OneOOnePointFive "The Hammer" FM'),\
    ('Wilds Squids 1', 'Wild Squids'),\
    ('Wilds Squids 2', 'Wild Squids Two'),\
    ('Team 10', 'Team Ten'),\
    ('2nd Breakfast','Twond Breakfast'),\
    ('We dropped out of college to pursue our Splatoon 2 ESports career (please let us win, our parents are already disappointed in us and it\'ll be even worse if we come home without a tourney win)','We dropped out of college to pursue our Splatoon Two ESports career (please let us win, our parents are already disappointed in us and it\'ll be even worse if we come home without a tourney win)'),\
    ('Empire Arcadia  (3D)', 'Empire Arcadia  (ThreeD)'),\
    ('5squa', 'Fivesqua'),\
    ('KID squad','KID Squad'),\
    ('R4Me!','RFourMe!'),\
    ('_3k Army', '_ThreeK Army'),\
    ('_4k army', '_FourK army'),\
    ('_4k Army', '_Fourk Army'),\
    ('4k army', 'Fourk army'),\
    ('4skin tim','Fourskin tim'),\
    ('TeamS4','TeamSFour'),\
    ('Team S4','Team SFour'),\
    ('X_xNoFear69_xX','X_xNoFearSixNine_xX'),\
    ('Pay 2 Win','Pay Two Win'),\
    ('Sero2 (with a gay sub)','SeroTwo (with a gay sub)'),\
    ('Esporantos 2','Esporantos two'),\
    ('Ascension Splatoon 2','Ascension Splatoon Two'),\
    ('Stay Fresh 2','Stay Fresh Two'),\
    ('7 Seas','Seven Seas'),\
    ('The 7 Sins','The Seven Sins'),\
    ('Redstarxxx33','RedstarxxxThreeThree'),\
    ('S4','SFour'),\
    ('Fantastic 4','Fantastic Four'),\
    ('Spla ver.2','Spla .verTwo'),\
    ('Shashari zen 1','Shashari zen One'),\
    ('Tottoko Hamtaro 2','Tottoko Hamtaro Two'),\
    ('HC7','HCSeven'),\
    ('4Rs','FourRs'),\
    ('pepapigs fc 2448-9971-2789','pepapigs'),\
    ('21-sai','TwoOne-sai'),\
    ('NK 21-sai','NK TwoOne-sai'),\
    ('21-sai!','TwoOne-sai!'),\
    ('Sloshing Machine 4-mai','Sloshing Machine Four-mai'),\
    ('Ryoutan 2-mai hensei','Ryoutan Two-mai hensei'),\
    ('Hissen 0-mai de kimashita','Hissen Zero-mai de kimashita'),\
    ('Hissen izaka 46','Hissen izaka FourSix'),\
    ('M4p_','MFourp_'),\
    ('Get Sloshed 2017','Get Sloshed TwoZeroOneSeven'),\
    ('6th sense','Sixth sense'),\
    ('10 Combo [Zones Cup-you]','OneZero Combo [Zones Cup-you]'),\
    ('FCT5','FCTFive'),\
    ('Triangle chikubi 2','Triangle chikubi Two'),\
    ('S1','SOne'),\
    ('Yami no 4-ninshu','Yami no Four-ninshu'),\
    ('5000-chou ale kudasai','FiveThousand-chou ale kudasai'),\
    ('Graphics card 15000 yen','Graphics card FifteenThousand yen'),\
    ('ACT-4','ACT-Four'),\
    ('2981-en','TwoNineEightOne-en'),\
    ('KMNA2','KMNATwo'),\
    ('?5D`s?','?FiveD`s?'),\
    ('[5D`s]','[FiveD`s]'),\
    ('3-saiji no gakoi','Three-saiji no gakoi'),\
    ('1.3 kuzushi-tai','One.Three kuzushi-tai'),\
    ('Byousoku 5cm','Byousoku Fivecm'),\
    ('c3*','cThree*'),\
    ('7-chan maji de kusai','Seven-chan maji de kusai'),\
    ('*72000','*SevenTwoZeroZeroZero'),\
    ('En2','EnTwo'),\
    ('Gal +1','Gal +One'),\
    ('Deatte 8.6-byou de Steak','Deatte Eight.Six-byou de Steak'),\
    ('600-zoku','SixZeroZero-zoku'),\
    ('+4Ga','+FourGa'),\
    ('P1CKOOF (?° ?? ?°)','POneCKOOF (?° ?? ?°)'),\
    ('??24-sai??','??TwoFour-sai??'),\
    ('SZ Hammerhead Bridge kara hidari mawari 5-saki','SZ Hammerhead Bridge kara hidari mawari Five-saki'),\
    ('Baller tamashii 2017','Baller tamashii TwoZeroOneSeven'),\
    ('Butterfly Dream V4','Butterfly Dream VFour'),\
    ('Eyeshield 4','Eyeshield Four'),\
    ('.4me with P','.Fourme with P'),\
    ('SBT8(Sukina bukidzukai-tai8)','SBTEight(Sukina bukidzukai-taiEight)'),\
    ('Hyrule Clan 2','Hyrule Clan Two'),\
    ('HyruleClan 2','HyruleClan Two'),\
    ('??Saikyou unchi shuudan??','Saikyou unchi shuudan'),\
    ('Asylum Killers 47','Asylum Killers FourSeven'),\
    ('Shockwave Splatoon 2','Shockwave Splatoon Two'),\
    ('Fish Bowl111','Fish BowlOneOneOne'),\
    ('h3 iranee','hThree iranee'),\
    ('Melty kiss??','Melty kiss'),\
    ('3v4 us bro','ThreevFour us bro'),\
    ('Genesis 1','Genesis One'),\
    ('3rd Coast','Threerd Coast'),\
    ('DJ Snake 90\'s','DJ Snake NineZero\'s'),\
    ('Level 36','Level ThreeSix'),\
    ('NG4','NGFour'),\
    ('Golden Star 2','Golden Star Two'),\
    ('Golden Star 1','Golden Star One'),\
    ('?LITE $QUAD 2','?LITE $QUAD Two'),\
    ('?LITE $QUAD 1','?LITE $QUAD One'),\
    ('A4','AFour'),\
    ('G2W','GTwoW'),\
    ('2dos and His Children','Twodos and His Children'),\
    ('Exposed + 2 randoms','Exposed + Two randoms'),\
    ('Nov/Dec no taikai de Best 8 o mezasu Team (kari)','Nov/Dec no taikai de Best Eight o mezasu Team (kari)'),\
    ('Squidding Good 2','Squidding Good Two'),\
    ('ßeryllium §quid 1','ßeryllium §quid One'),\
    ('ßeryllium §quid 2','ßeryllium §quid Two'),\
    ('https://youtu.be/qdPb3JNHidw','https://youtu.be/qdPbThreeJNHidw'),\
    ('Anathema 2','Anathema Two')
    ]


# Typos, full last names, changed tags, names that have tags, extra spaces, etc., go here.

ReplacementList = [ \
    ('AG | Arc', 'Arc'), \
    ('Spicy Bois', 'Hanran'),\
    ('Jouzu','Hanran'),\
    ('Wil\'s left toe', 'Hanran'),\
    ('Wil\'s right toe', 'Hanran'),\
    ('Wil\'s Left Finger','Hanran'),\
    ('HOMO_SP','Hanran'),\
    ('HanRan','Hanran'),\
    ('Monado Boiz (Hanran)','Hanran'),\
    ('Wil Fan Club','Hanran II'),\
    ('Harambe\'s Minions','Hanran II'),\
    ('We Come to Break Memories','Break Memories'),\
    ('On The Memes','On The Bounce'),\
    ('On the Memes','On The Bounce'),\
    ('Lagtorious','Notorious'),\
    ('NOtorious','Notorious'),\
    ('No?orious','Notorious'),\
    ('Lightning Shoal','Lightning Shoals'),\
    ('Lightnight Shoals','Lightning Shoals'),\
    ('Lightning Shaols','Lightning Shoals'),\
    ('Cooldown','CoolDown'),\
    ('sQUID TECH','SQUID TECH'),\
    ('Killers Wails','Killer Wails'),\
    ('Killer Wails+', 'Killer Wails'),\
    ('Spalttercolors', 'Splattercolors'),\
    ('NeBula Squids','Nebula Squids'),\
    ('Quick-Nauts','Quick Nauts'),\
    ('Star Squids Units','StarSquids'),\
    ('Asylum Killers','Asylum Killers 47'),\
    ('Asylum Killers ','Asylum Killers 47'),\
    ('Black Lamars  ','Black Lamars'),\
    ('Chaos','Chaotic Haze'),\
    ('Team NorthStar','NorthStar'),\
    ('Northstar','NorthStar'),\
    ('evolution','Evolution'),\
    ('evoltuion','Evolution'),\
    ('Evolutio','Evolution'),\
    ('Evoltuion','Evolution'),\
    ('GIFTICREW','Theta'),\
    ('?All Star Squad?','All Star Squad'),\
    ('All S+ars','All Stars'),\
    ('MoonLight ?EØ','MoonLight Neo'),\
    ('The SAVAGES','The Savages'),\
    ('Aka Sora','AKA Sora'),\
    ('AS»Alpha Squids','Alpha Squids'),\
    ('Dapple dudes','Dapple Dudes II'),\
    ('QTs','Calamari Cuties'),\
    ('QTS','Calamari Cuties'),\
    ('Qts','Calamari Cuties'),\
    ('cuties','Calamari Cuties'),\
    ('Cuties','Calamari Cuties'),\
    ('The QTS','Calamari Cuties'),\
    ('QTII','Calamari Cuties II'),\
    ('? Iridescent','Iridescent'),\
    ('~Galaxy Squids~(Gs)','Galaxy Squids'),\
    ('Slimy\'s Baddies','Chicken Sandwich'),\
    ('McDonalds Premium Butter Crispy Chicken Sandwich','Chicken Sandwich'),\
    ('McDonalds Premium Buttermilk Crispy Chicken Sandwich','Chicken Sandwich'),\
    ('McDonals Premium Buttermilk Crispy Chicken Sandwich','Chicken Sandwich'),\
    ('SFD','Squids for DAYS'),\
    ('Squid for DAYS','Squids for DAYS'),\
    ('KOMPERS','Kompers'),\
    ('Splatter u','SplatterU'),\
    ('Splatter U','SplatterU'),\
    ('MIDKNIGHT','MidKnight'),\
    ('Midknight','MidKnight'),\
    ('Komodo Yin','Komodo'),\
    ('Komodo ', 'Komodo'),\
    ('Komodo Splat','Komodo'),\
    ('KomodoSplat','Komodo'),\
    ('Komodo Yang','Komodo II'),\
    ('Two Moon','Two Moons'),\
    ('? shi','Shi'),\
    ('Unity','Team Unity'),\
    ('TeamUnity','Team Unity'),\
    ('It\'s four-fifty-four AM & I\'m the Only One Up So This Is The Name We Get','Four Fifty-Four AM'),\
    ('Xeno (Sqaure Up)','SquareUp'),\
    ('Endless Ocean','Endless Oceans'),\
    ('Endless Ocean ','Endless Oceans'),\
    ('Endless OCeans','Endless Oceans'),\
    ('Le Meme Team','Seishin'),\
    ('Serial killers','Serial Killers'),\
    ('TSF','The Splat Fam'),\
    ('TSF Plus','The Splat Fam'),\
    ('The Splat Fam Division','The Splat Fam'),\
    ('TSF Division','The Splat Fam'),\
    ('The Splat Fam Plus','The Splat Fam'),\
    ('CircleJerk','Circlejerk'),\
    ('cirlejerk','Circlejerk'),\
    ('Team Circlejerk','Circlejerk'),\
    ('Charles\' Jr.','Circlejerk'),\
    ('Franks Hotdogs and Tryouts','Franks Hotdogs'),\
    ('veganteam','TOMO'),\
    ('Evisceration','TOMO'),\
    ('Tomo','TOMO'),\
    ('tomo','TOMO'),\
    ('Bronies', 'TOMO'),\
    ('Stop Me', 'TOMO'),\
    ('TOMO_SP', 'TOMO'),\
    ('Blackberry Sorbet','TOMO'),\
    ('Elbow Drops and Peanut Pops','EDPP'),\
    ('Elbow Drops & Peanut Pops','EDPP'),\
    ('Imperial squids','Imperial Squids'),\
    ('Inkafe','Inkafé'),\
    ('i??¿nigma','Inknigma'),\
    ('i??nigma','Inknigma'),\
    ('InkNigma','Inknigma'),\
    ('White Paper!','Hakushi'),\
    ('Katsuie Fan Club','Hakushi'),\
    ('Containment Unit Meme','Hakushi'),\
    ('Army','Hakushi'),\
    ('pepapigs fc 2448-9971-2789','pepapigs'),\
    ('Name Subject to change','Name Subject to Change'),\
    ('SND','Squids Next Door'),\
    ('Rip the Dream','Rip The Dream'),\
    ('RTD','Rip The Dream'),\
    ('i?? alpha','Ink Alpha'),\
    ('i???Delta','Ink Delta'),\
    ('Ink delta','Ink Delta'),\
    ('Black Squid Ink Burgr','Black Squid Ink Burger'),\
    ('Black Squid Ink burger', 'Black Squid Ink Burger'),\
    ('Exposed','Exposed?'),\
    ('Exposed + 2 randoms','Exposed?'),\
    ('X_xNoFear69_xX','No Fear'),\
    ('Inc Yami','Yami'),\
    ('USA','Yami'),\
    ('InC Yami','Yami'),\
    ('Sero2 (with a gay sub)','Sero II'),\
    ('quantuM Kids','quantuM'),\
    ('quantuM ','quantuM'),\
    ('[qM] quantuM Kids','quantuM'),\
    ('[qM] quantuM','quantuM'),\
    ('chimera','Chimera'),\
    ('Ded like me','Dead Like Me'),\
    ('Dead Liek Me','Dead Like Me'),\
    ('Unkonwn','Unknown'),\
    ('Team Unknown','Unknown'),\
    ('Unknown?','Unknown'),\
    ('D+','Unknown??'),\
    ('Unkonwn??','Unknown??'),\
    ('Crash?B','Crash\'B'),\
    ('DT?s','DT\'s'),\
    ('DetonaTE','Dark Horse f'),\
    ('[LS] LuckyShot','Dark Horse f'),\
    ('men?s','men\'s'),\
    ('W’z','W\'z'),\
    ('Moleculer','Molecular'),\
    ('Mie-ken tsushi de Enty tsukamaemashita','Mieken tsushi de Entei tsukamaemashita!'),\
    ('NeutralColor','Neutral Color'),\
    ('it’a true wolrd.','it\'a true wolrd.'),\
    ('Hedei klimit','Heidi Klimt'),\
    ('Cure Teto Chiinu*','Cure Teto Chiinu'),\
    ('Chibi Squids Squad','Chibi Squid Squad'),\
    ('Nin?nyaku hatake','Nin\'nyaku hatake'),\
    ('Rectify Gaming','Rectify Extermination'),\
    ('RCG Extermination','Rectify Extermination'),\
    ('Extermination','Rectify Extermination'),\
    ('Exterminaion','Rectify Extermination'),\
    ('Ink OMega','Ink Omega'),\
    ('Four?s','Four\'s'),\
    ('Non?non Kids','Non\'non Kids'),\
    ('Hightide Era','The Hightide Era'),\
    ('Inkopolis Hoeroes','Inkopolis Heroes'),\
    ('Team Bapped','Team ?Banned¿'),\
    ('TeamS4','Team S4'),\
    ('NerdySquidsEverlasting','Nerdy Squids Everlasting'),\
    ('PowerPoints','PowerPoint'),\
    ('Wanwan?o','Wanwan\'o'),\
    ('Asperger?s','Asperger\'s'),\
    ('Gokijet Cup un?ei','Gokijet Cup un\'ei'),\
    ('Practical Eror','Practical Error'),\
    ('Practical Errors','Practical Error'),\
    ('Procrastinatino Squad','Procrastination Squad'),\
    ('ConQuest','Wombo Combo'),\
    ('Conquest','Wombo Combo'),\
    ('ConqQuest','Wombo Combo'),\
    (' Hayley\'s Comets','Hayley\'s Comets'),\
    ('Yappa Get Kraken Garbage','Get Kraken'),\
    ('Garbage Kan','Got Kraken'),\
    ('Finding Penguitt','Strange Approach'),\
    ('hogtod','Reverse Rebirth'),\
    ('Kaiju','Team Kaiju'),\
    ('Surface Tention','Surface Tension'),\
    ('Locdown','Lockdown'),\
    ('Yoro?onesu Yamazaki','Yoro\'onesu Yamazaki'),\
    ('Los Inklins','Los Inklings'),\
    ('Splash\'Color','Splash Color'),\
    ('Splash\'color','Splash Color'),\
    ('Squids GameKult','Squids Gamekult'),\
    ('Squids Warrios','Squids Warriors'),\
    ('NightFall X','Nightfall X'),\
    ('Team Nolive', 'Team Olive'),\
    ('MYTH', 'Myth'),\
    ('DimensionSP','Dimension'),\
    ('Dimension(SP)','Dimension'),\
    ('Bluepeach + Tryouts', 'Bluepeach'),\
    ('Rogue Firmament','Serenity FR'),\
    ('Serenity + Tryouts', 'Serenity'),\
    ('Serenity_spl','Serenity'),\
    ('serenity', 'Serenity'),\
    ('Bluepeach', 'BluePeach'),\
    ('Notorious Splatoon', 'Notorious'),\
    ('Calmaity', 'Calamity'),\
    ('Karios', 'Kairos'),\
    ('ethereal', 'Ethereal'),\
    ('Ethereal.', 'Ethereal'),\
    ('_Ethereal_','Ethereal'),\
    ('Académie Magma', 'Academie Magma'),\
    ('Calamity ', 'Calamity'),\
    ('Fresca Frode','Crème Fresh'),\
    ('Fresh Frauds','Crème Fresh'),\
    ('Creme Fresh ', 'Crème Fresh'),\
    ('Creme Fresh', 'Crème Fresh'),\
    ('Saikari', 'Saikai'),\
    ('Silver Sanction','Saikai'),\
    ('Circléjerk','Saikai'),\
    ('Yaboi\'s','Saikai'),\
    ('Silver Sanction | Saikai', 'Saikai'),\
    ('Silver Hawks ', 'Silver Hawks'),\
    ('Spanish Army Splatoon', 'Spanish Army'),\
    ('Syngery', 'Synergy'),\
    ('S?nerg?', 'Synergy'),\
    ('Synergy_splat','Synergy'),\
    ('Team-BnT', 'Team BnT'),\
    ('Team?BnT', 'Team BnT'),\
    ('AllTheWay', 'All The Way'),\
    ('Wilds Squids', 'Wild Squids'),\
    ('Wild Squids  ', 'Wild Squids'),\
    ('Wilds Squids 1', 'Wild Squids'),\
    ('Wilds Squids 2', 'Wild Squids II'),\
    ('Wilds Squids II', 'Wild Squids II'),\
    ('Windward ', 'Windward'),\
    ('Ascension Splatoon 2','Ascension'),\
    ('AscensionSP','Ascension'),\
    ('Team Ascension','Ascension'),\
    ('License to Krill ', 'License to Krill'),\
    ('High Definiton', 'High Definition'),\
    ('Aurora | AU','Aurora'),\
    ('Energyy', 'High Definition'),\
    ('ßeryllium §quid 1','ßeryllium §quid'),\
    ('ßeryllium §quid 2','ßeryllium §quid II'),\
    ('Bazanji','Portal of Gaming'),\
    ('Echo e-Sports','Portal of Gaming'),\
    ('Echo Esports','Portal of Gaming'),\
    ('InC Sorrow','InControl Sorrow'),\
    ('Etheral', 'Ethereal'),\
    ('Ethereal_Spl','Ethereal'),\
    ('Element-?','Element-R'),\
    ('eX: Equinox','Equinox'),\
    ('Fire ??reathing Rubber ??uckies','Fire Breathing Rubber Duckies'),\
    ('Franks Hotdogs','Frank\'s Hot Dogs'),\
    ('EL Firmament', 'El Firmament'),\
    ('El Firmament ', 'El Firmament'),\
    ('Les Extralamars!', 'El Firmament'),\
    ('Extralamars Firmament','El Firmament'),\
    ('EL Arctic' ,'El Arctic'),\
    ('EL Artic', 'El Arctic'),\
    ('EL arctic', 'El Arctic'),\
    ('Les Extralamars Artic', 'El Arctic'),\
    ('Les Extralamars Arctic	', 'El Arctic'),\
    ('Les Extralamars! Artic', 'El Arctic'),\
    ('EL Zéphyr','El Zephyr'),\
    ('Extralamars Zéphyr','El Zephyr'),\
    ('Squishy_Squad','Squishy Squad'),\
    ('Street?UrchinZ','Street UrchinZ'),\
    ('Team Tallarin?','Team Tallarin'),\
    ('Limitless.','Limitless'),\
    ('Lost at Sea','Lost At Sea'),\
    ('cyber Squids', 'Cyber Squids'),\
    ('Clan Army ', 'Clan Army'),\
    ('POSE TA WAAARD !!!!', 'Pose ta Waaard'),\
    ('SeMix', 'Semix'),\
    ('? cs????tisn','Corruption'),\
    ('Take Over','TakeOver!'),\
    ('TakeOver??', 'TakeOver!'),\
    ('TakeOver', 'TakeOver!'),\
    ('TakeOver ', 'TakeOver!'),\
    ('  TakeOver', 'TakeOver!'),\
    ('Bacteria', 'Hanran'),\
    ('??TSIG??L.spl','Neosignal'),\
    ('??TSIG??L','Neosignal'),\
    ('CST competitive A','CST CP'),\
    ('CST competitive', 'CST CP'),\
    ('CST Competitive','CST CP'),\
    ('CST competitive B','CST CP B'),\
    ('Geek?Squid','Geek Squid'),\
    ('Pachink', 'Pachink!'),\
    ('PARADOX ', 'PARADOX'),\
    ('EnigmaSquids', 'Primitive'),\
    ('Enigma Squids', 'Primitive'),\
    ('Deadbeat', 'SetToDestroyX'),\
    ('IK','Inked Killers'),\
    ('StDx','SetToDestroyX'),\
    ('4skin tim','SetToDestroyX'),\
    ('Heretik', 'Hérétik'),\
    ('Heretik ', 'Hérétik'),\
    ('Hérétik Shiva','Hérétik'),\
    ('bad squids', 'Clockwork'),\
    ('Clockwork ????','Clockwork'),\
    ('Monado&Friends','Monado\'&Friends'),\
    ('Tales Of', 'Tales of'),\
    ('Aio Sora Cosplay', 'Aoi Sora Cosplay'),\
    ('Aoi? ?Sora? ?Cosplay','Aoi Sora Cosplay'),\
    ('ASC Neko ','Aoi Sora Cosplay'),\
    ('ASC Neko','Aoi Sora Cosplay'),\
    ('Dash team','Dash Team'),\
    ('[E+] Funward','E+ Funward'),\
    ('Housai Squad', 'Hokusai Squad'),\
    ('Hokusai  Squad', 'Hokusai Squad'),\
    ('Nakama No Shi', 'Nakama no Shi'),\
    ('Nakami No Shi', 'Nakama no Shi'),\
    ('SilverHawks', 'Silver Hawks'),\
    ('Silverhawks', 'Silver Hawks'),\
    ('PoulpyTeam','Poulpy Team'),\
    ('Over Road ','Over Road'),\
    ('Slowpoke ','Slowpoke'),\
    ('SlowPoke','Slowpoke'),\
    ('SplankUnity','SpankUnity'),\
    ('Orks II','orKs Red'),\
    ('orKs II','orKs Red'),\
    ('Skillink II', 'orKs Red'),\
    ('SkillinK²','orKs Red'),\
    ('SkillinK II','orKs Red'),\
    ('orKs eSports II','orKs Red'),
    ('SkillinK','orKs Black'),\
    ('Skillink', 'orKs Black'),\
    ('Skillink ', 'orKs Black'),\
    ('Skillink  ', 'orKs Black'),\
    ('Skilllink', 'orKs Black'),\
    ('orKs eSports','orKs Black'),\
    ('orKs E-sport','orKs Black'),\
    ('Orks e-sport','orKs Black'),\
    ('Splat it on!','Splat It On!'),\
    ('Team Oathkeeper','Oathkeeper'),\
    ('Spicy Kraken Rolls','OnSight Gaming'),\
    ('TranslucentSpl','Translucent'),\
    ('MPTLCC','Translucent'),\
    ('MyPussyTasteLikeCocaCola','Translucent'),\
    ('vectorQry','VectorQry'),\
    ('PhantomThieves','Phantom Thieves'),\
    ('	ParaMoons','ParaMoons'),\
    ('Anti-Seiche','Anti Seiche'),\
    ('Antiseiche','Anti Seiche'),\
    ('AntiSeiche','Anti Seiche'),\
    ('Antiseiche ','Anti Seiche'),\
    ('Just For The Halibut (Cap: Marsh)','Just For The Halibut'),\
    ('_3k Army','Neptune'),\
    ('_4k army', 'Neptune'),\
    ('_4k Army', 'Neptune'),\
    ('4k army', 'Neptune'),\
    ('4k Army', 'Neptune'),\
    ('Fourk Army', 'Neptune'),\
    ('Neptune.','Neptune'),\
    ('Wolf Squid ','Wolf Squid'),\
    ('Tidal Wave (TW)','Tidal Wave'),\
    ('Tidal Wave_SP','Tidal Wave'),\
    ('S4','Team S4'),\
    ('Legac?','Legacy'),\
    ('Stay_Fresh','Stay Fresh White'),\
    ('Stay Fresh ','Stay Fresh White'),\
    ('Stay Fresh','Stay Fresh White'),\
    ('Stay Fresh II','Stay Fresh Black'),\
    ('Stay Fresh 2','Stay Fresh Black'),\
    ('?Sla?F?????','Slay Fresh White'),\
    ('Fresh_Squids','Fresh Squids'),\
    ('Stay Salty','Stay Stalty'),\
    ('stay stalty','Stay Stalty'),\
    ('Team Alpha','Team Alpha Splatoon'),\
    ('Team Sans Nom','Team sans Nom'),\
    ('Team Majesty','Majesty'),\
    ('Blue Ringed Octolings.','Blue Ringed Octolings'),\
    ('The Inkredible Crew (TIC)','The INKREDIBLE Crew'),\
    ('the inkredible crew','The INKREDIBLE Crew'),\
    ('The INKCREDIBLE Crew','The INKREDIBLE Crew'),\
    ('Inkredible Team','INKredible Team'),\
    ('INKredibleTeam','INKredible Team'),\
    ('Les tartineurs','Les Tartineurs'),\
    ('Nocturnal Team','Inglorious Bastards'),\
    ('inglorious bastards','Inglorious Bastards'),\
    ('Octo Shurilken','Knights of Queen'),\
    ('Octo Shuriken','Knights of Queen'),\
    ('LOVE','Love'),\
    ('Love Team','Love'),\
    ('NightSquid','Night Squid'),\
    ('Night Squid ','Night Squid'),\
    ('Night Squids','Night Squid'),\
    ('PX Phoenix','Phoenix'),\
    ('FireSquid','Fire Squids'),\
    ('Frères de poulpe','Frères de Poulpe'),\
    ('Game Of Team','Game of Team'),\
    ('Game of Team ','Game of Team'),\
    ('Game of Team  ','Game of Team'),\
    ('Golden Star 1','Golden Star'),\
    ('Golden Star ','Golden Star'),\
    ('Golden Star 2','Golden Star II'),\
    ('No Fear but DJ might have to stop playing mid match to answer the door and get his pizza','No Fear'),\
    ('Old Squid ','Old Squid'),\
    ('EL Poseidon', 'El Poseidon'),\
    ('EL Poséidon','El Poseidon'),\
    ('Elite $quad','Elite Squad'),\
    ('Elite-$quad','Elite Squad'),\
    ('?LITE $QUAD 2','Elite Squad II'),\
    ('?LITE $QUAD 1','Elite Squad'),\
    ('El Poséidon','El Poseidon'),\
    ('Taka', 'TAKA'),\
    ('Inifity','Infinity'),\
    ('CO', 'Infinity'),\
    ('CO Infinity','Infinity'),\
    ('Dark Team','La Dark Team'),\
    ('Dash','Dash Team'),\
    ('Zetsubo no Hono', 'Zetsubo no Hono Skykling'),\
    ('ZnH Skykling', 'Zetsubo no Hono Skykling'),\
    ('ZNH Skykling', 'Zetsubo no Hono Skykling'),\
    ('ZnH Pinkling', 'Zetsubo no Hono Pinkling'),\
    ('ZnH Greenkling', 'Zetsubo no Hono Greenkling'),\
    ('CordMellow', 'Cord Mellow'),\
    ('Dashwing', 'Dash Wing'),\
    ('Hyrule Clan  ', 'Hyrule Clan'),\
    ('Hyrule clan', 'Hyrule Clan'),\
    ('Hyrule Clan 2','Hyrule Clan II'),\
    ('HyruleClan 2','Hyrule Clan II'),\
    ('Hyrule clan II', 'Hyrule Clan II'),\
    ('ryusei Squad', 'Ryusei Squad'),\
    ('Rtax', 'RTax'),\
    ('S?ectrum','Spectrum'),\
    ('Half-Baked','Half Baked'),\
    ('HALF BAKED','Half Baked'),\
    ('? Jelly Squids','Jelly Squids'),\
    ('Okami', 'O K A M I'),\
    ('OKAMI', 'O K A M I'),\
    ('O K ? M ?', 'O K A M I'),\
    ('o k a m i', 'O K A M I'),\
    ('Yami no ma shin?ei-tai','Yami no ma shin\'ei-tai'),\
    ('WYHO?s','WYHO\'s'),\
    ('We have come to dab','Pickup.exe'),\
    ('Pickup.Exe','Pickup.exe'),\
    ('Smoke', 'FINALLY'),\
    ('SMOKE','FINALLY'),\
    ('SND|Shinka','FINALLY'),\
    ('Dugtrio and a tooth','FINALLY'),\
    ('Splat In Peace', 'Splat in Peace'),\
    ('Team lauch', 'Team Lauch'),\
    ('TL - Team Luxembourg', 'Team Luxembourg'),\
    ('Shockwave', 'ShockWave'),\
    ('Shockwave Splatoon two','ShockWave'),\
    ('Shockwave Splatoon 2','ShockWave'),\
    ('Team Phantom','Eclipse!'),\
    ('?Eclipse?','Eclipse!'),\
    ('Ecl?pse', 'Eclipse!'),\
    ('Eclipse','Eclipse!'),\
    ('buff e liter pls','buff eliter pls'),\
    ('??•IndjaCalamars','IndjaCalamars'),\
    ('Ðeep ßlues', 'Deep Blues'),\
    ('ExtinctionSP', 'Extinction'),\
    ('CLanless', 'Clanless'),\
    ('Clanless ', 'Clanless'),\
    ('ClanLess','Clanless'),\
    ('Surge team', 'Surge'),\
    ('Team BEER + Spoon', 'Team BEER'),\
    ('Seafood Sorbet!','Seafood Sorbet'),\
    ('Ne??šis', 'Nemesis'),\
    ('Nemesiš','Nemesis'),\
    ('?sƒ (?he splat ƒam)', 'The Splat Fam'),\
    ('?sƒ+ (?he splat ƒam)','The Splat Fam'),\
    ('Blue Moon.','Blue Moon'),\
    ('Illu crew', 'Illu Crew'),\
    ('?SS (Essence)', 'Essence'),\
    ('ESSENCE','Essence'),\
    ('DIVINITY TEAM A','Divinity'),\
    ('DIVINITY TEAM B','Divinity B'),\
    ('Generation Z ', 'Generation Z'),\
    ('Wing Of Pegasus', 'Wings of Pegasus'),\
    ('Wings Of Pegasus', 'Wings of Pegasus'),\
    ('Imperious AU', 'Imperious'),\
    ('Inklings Next Ðoor', 'Inklings Next Door'),\
    ('Oceanside Squids (OSS)' ,'Oceanside Squids'),\
    ('SWE - Squid Warriors Elite', 'Squid Warriors Elite'),\
    ('Phoeni?', 'Phoenix'),\
    ('Empire Arcadia  (3D)', 'Empire Arcadia'),\
    ('Uprising_SP','UPRISING'),\
    ('UPRISING_Sp','UPRISING'),\
    ('P1CKOOF (?° ?? ?°)','Pickoff'),\
    ('?ø??ø? Knights I','Køntøn Knights'),\
    ('Konton Knights l','Køntøn Knights'),\
    ('Konton Knights','Køntøn Knights'),\
    ('Eclipse Køntøn l','Køntøn Knights'),\
    ('Eclipse Konton l','Køntøn Knights'),\
    ('Eclipse Konton I','Køntøn Knights'),\
    ('Eclipse Konton','Køntøn Knights'),\
    ('Project Konton','Køntøn Knights'),\
    ('Ronin Konton','Køntøn Knights'),\
    ('Eclipse Køntøn','Køntøn Knights'),\
    ('Eclipse Køntøn II','Køntøn Knights II'),\
    ('Konton Knights II','Køntøn Knights II'),\
    ('Project Konton II','Køntøn Knights II'),\
    ('Ronin Konton ll','Køntøn Knights II'),\
    ('Ronin Konton II','Køntøn Knights II'),\
    ('Ambition.','Ambition'),\
    ('Ambition Splatoon','Ambition'),\
    ('SevenUpGamingSp','SevenUp Gaming'),\
    ('Imperious Wolves','SevenUp Gaming'),\
    ('Mistake','ReStart eSport Club'),\
    ('Restart ESC','ReStart eSport Club'),\
    ('Kosaku','Dream Evolution'),\
    ('BEt','BET'),\
    ('Dream Evolution Alpha','Dream Evolution'),\
    ('Team BoneLess','Team Boneless'),\
    ('Malicious Intentical','Malicious Intentacle'),\
    ('Octonight','Genesis'),\
    ('OctoNight','Genesis'),\
    ('Genesis 1','Genesis'),\
    ('Team The Squidly TTS','Team The Squidly'),\
    ('OmégaTeam','Omega Team'),\
    ('? Xiller','Xiller'),\
    ('Splat in Speace','Splat in Peace'),\
    ('The sheldons', 'The Sheldons'),\
    ('Crispy Soup','EnviZion'),\
    ('RRGB','EnviZion'),\
    ('EBGang', 'EnviZion'),\
    ('Secretion Splat','EnviZion'),\
    ('Team Meddux', 'Tsunami'),\
    ('Tsunami.','Tsunami'),\
    ('Tsunami™?','Tsunami'),\
    ('Visi¤n','Vision'),\
    ('Square Up', 'SquareUp'),\
    ('Inkvaders', 'InkVaders'),\
    ('Zplashout' ,'RedeMption'),\
    ('Zplash Out','RedeMption'),\
    ('Colossal Squids (CS)','Lastation'),\
    ('Collosal Squids','Lastation'),\
    ('Colossal Squids','Lastation'),\
    ('LastationSP','Lastation'),\
    ('Kaha Maori', 'Achroma'),\
    ('xite', 'Xite'),\
    ('Half and Half', 'Half & Half'),\
    ('i??S', 'Ink Epsilon'),\
    ('Better with Age', 'Better With Age'),\
    ('Ammo Knights','Upgrade'),\
    ('Leviathans LV', 'Leviathans'),\
    ('Leviathans~','Leviathans'),\
    ('Hearts ßrothers','Hearts Brothers'),\
    ('octoNight', 'OctoNight'),\
    ('MonadoO?arriors', 'Monado Warriors'),\
    ('???eard ???ois','Beard Bois'),\
    ('Team JP', 'Viper eSports'),\
    ('Team ?', 'Viper eSports'),\
    ('X','Viper eSports'),\
    ('Team X','Viper eSports'),\
    ('VipeR Team ?','Viper eSports'),\
    ('Archicosmus.','Archicosmus'),\
    ('Archicosmus Alfa','Archicosmus'),\
    ('[Celtic Networks] Deep Annihilation','Senkura'),\
    ('[Celtic Networks] | Deep Annihilation','Senkura'),\
    ('Deep Annihilation','Senkura'),\
    ('kraken ?aradise','Kraken Paradise'),\
    ('kraken paradise','Kraken Paradise'),\
    ('Last_Second','Last Second'),\
    ('Mercury (invitation pending)','Mercury'),\
    ('AlLL DOWN Kamasu ze noshinto', 'ALL DOWN Kamasu ze noshinto'),\
    ('Anthony', 'Country Carry shi ni kimashita'),\
    ('Apple Octop', 'Apple Octopi'),\
    ('Súper Inkling Bros','Super Inkling Bros'),\
    ('BW', 'Sako Manakasokubu'),\
    ('Hakushin gensoku-bu','Sako Manakasokubu'),\
    ('Sako Manakasokubu in sentakuki','Sako Manakasokubu'),\
    ('BW~bush warbler~', 'bush warbler'),\
    ('Fuautanzu', 'fountains'),\
    ('Mendoi karai iya', 'Gekikan Armor'),\
    ('Haburashizu', 'Haburashiizu'),\
    ('Geek man', 'Ikiri otaku'),
    ('Ikiriotaku','Ikiri otaku'),\
    ('Ikiri otaku to ikiranai otaku to neko to kaisen-ochi', 'Ikiri otaku'),\
    ('Ikiri otaku, hajimemashita.', 'Ikiri otaku'),\
    ('Ko arando A', 'Koaland A'),\
    ('Kumasan shoukai shisho', 'Kuma-san'),\
    ('LaLaLa koppepan', 'Okatu Kitsu w'),\
    ('Sateha doteida na teme (mei suiri)', 'Sate wa douteida na temei (mei suiri)'),\
    ('?(? ?? ?c) Ma','WakuWaku Ma'),\
    ('hshs?','hshs'),\
    ('two thonsand','two thousand'),\
    ('(´·?·`) shoukai','shoboon shoukai'),\
    ('Osechi?ko Busters','Osechi ko Busters'),\
    ('O?nko Busters','Oonko Busters'),\
    ('Co-eating?','Co-eating'),\
    ('Mmmmm ·?·?','Mmmmm'),\
    ('Wata ame (©?©?.)','Wata ame'),\
    ('Mayu Gaming w','Mayu Gaming'),\
    ('Mayu Gaming!','Mayu Gaming'),\
    ('(?_??)','mokou'),\
    ('(?,_??)','mokou II'),\
    ('Tehe pero ?','Tehe pero'),\
    ('? buntai','buntai'),\
    ('AoM?','AoM'),\
    ('btf?','btf'),\
    ('Tehe pero (?•?•?)','tehe pero'),\
    ('?Orera ga sokuseki team da?','Orera ga sokuseki team da'),\
    ('Totsugeki-tai?','Totsugeki-tai'),\
    ('? maji ?','maji'),\
    ('NoteNote','Lead to a victory'),\
    ('Lead to a victory.','Lead to a victory'),\
    ('Senpan Kids?','Senpan Kids'),\
    ('?  ?','Blank'),\
    ('??','Blank II'),\
    ('Bangtan Squids [BTS]','Bangtan Squids'),\
    ('Best Splat Inkling (BSI)','Best Splat Inkling'),\
    ('Ookami-san to yukai nakamatachi','Libalent Calamari'),\
    ('Judgement desu no ? (JM?)','Judgement desu no (JM)'),\
    ('atomy?bazooka','atomy bazooka'),\
    ('Mata no shita no ponyo ?','Mata no shita no ponyo'),\
    ('Orera wa teikousurude. Roller de ??','Orera wa teikousurude. Roller de'),\
    ('?Ryouta?','Ryouta'),\
    ('?Hattentojou?','Hattentojou'),\
    ('Royal??Unti','Royal Unti'),\
    ('? - Gum','Gum'),\
    ('?r??(*··)s','Er'),\
    ('Er?','Er'),\
    ('MM?','MM'),\
    ('Melonkuchen one-thousand-four-hundred-and-three cal (sai sakusei)','Melonkuchen one-thousand-four-hundred-and-three cal'),\
    ('Hakuna matata?///','Hakuna matata'),\
    ('LS?','Lucky Shot'),\
    ('LuckyShot?','Lucky Shot'),\
    ('Taikai sen?you Team','Taikai sen\'you Team'),\
    ('Tetsukuzu Scrapper?s','Tetsukuzu Scrapper\'s'),\
    ('?VMS','VMS'),\
    ('Ham-chanz?','Ham-chanz'),\
    ('Darkness?Nyannyan','Darkness Nyannyan'),\
    ('?CDT?','[CDT]'),\
    ('Kamyuchanz?','Kamyuchanz'),\
    ('OB???','OB'),\
    ('NINJA??!','NINJA!'),\
    ('Balse?','Balse'),\
    ('HYK (·w·)?','HYK (·w·)'),\
    ('? no P?SPOT','No P SPOT'),\
    ('iGS?','iGS'),\
    ('Bimyuu*','Bµf*(bimyuu)'),\
    ('Crayon?Orange?','Crayon Orange'),\
    ('GaMe®?s HigH','Gamers HigH'),\
    ('Teikousuru de, kobushi de??','Teikousuru de, kobushi de'),\
    ('Orera wa teikousurude?','Orera wa teikousurude'),\
    ('Hakushin Sentakki ?','Hakushin Sentakki'),\
    ('t_o_m_o HAHAHA?','t_o_m_o HAHAHA'),\
    ('SplaCS kaisenochi da yo ?','SplaCS kaisenochi da yo'),\
    ('?5D`s?','[5D`s]'),\
    ('Jack-o\'-????','Jack-o\'-Lantern'),\
    ('Mochimochi~?','Mochimochi~'),\
    ('Tomakin naide??','Tomakin naide'),\
    ('EMP†','E M P'),\
    ('EMP','E M P'),\
    ('?Zettai ryouiki?','Zettai ryouiki'),\
    ('kobushide??????','kobushide'),\
    ('?? Mikakunin ??','Mikakunin'),\
    ('Aru?Gaming III ~ kieyuku tomo, utsurikawaru jidai','Aru Gaming III'),\
    ('?TC kara no shikaku?','TC kara no shikaku'),\
    ('Asaru to ? ichigo Revolution','Asaru to ichigo Revolution'),\
    ('Mochi, kubari ni kimashita ?','Mochi, kubari ni kimashita'),\
    ('?NK?Nyoora Kids','[NK] Nyoora Kids'),\
    ('?Shikkoku no Inkbrush?','Shikkoku no Inkbrush'),\
    ('Hoshinon?SZ Cup=Block?','Hoshinon SZ Cup=Block'),\
    ('? Ninjin shirishiri ?','Ninjin shirishiri'),\
    ('Pyaa?Pyaa?Yureta naru na A','Pyaa Pyaa Yureta naru na A'),\
    ('? oretachi saikyou ?','oretachi saikyou'),\
    ('Koushien (n*´?` *n)','Koushien (n*´w` *n)'),\
    ('Ge? shabushabu','Ge shabushabu'),\
    ('SSu(Small Sha us)','SSu'),\
    ('Ne Bu Soku ( ˘o˘ ) .zZ','Ne Bu Soku'),\
    ('Magical?Mint Night','Magical Mint Night'),\
    ('v.?Sr.?','[Sr.]'),\
    ('bery?splash','bery splash'),\
    ('Odango ?????','Odango'),\
    ('EG?','EG'),\
    ('s ?!','s yu!'),\
    ('Zonsute daisuki ?','Zonsute daisuki'),\
    ('Aiueoon (?,_??)','Aiueoon'),\
    ('Rapid Blaster?','Rapid Blaster'),\
    ('Mega*?','Mega*'),\
    ]
