import sqlite3

connection = sqlite3.connect("cable_database.db")

cursor = connection.cursor()


# cursor.execute('''
# CREATE TABLE cable (
#   id integer PRIMARY KEY,
#   family_name text NOT NULL,
#   first_name text NOT NULL,
#   rca_id text NOT NULL,
#   email text,
#   cable_ID text NOT NULL
# );
# ''')


# cursor.execute('''
# INSERT INTO cable VALUES
# (1,'Abayisenga','Aime Pacifique','RCA04001NJG','abayisengaaimepacifique@gmail.com','26A1VEF'),
# (2,'Akimana','Viateur','RCA04002GNZ','akimanaviateur94@gmail.com','26G02DV'),
# (3,'Akuzwe','Sheja Edwige','RCA04003UWE','edwigeakuzwe6@gmail.com','26R0H9C'),
# (4,'Alliance','Fils Dieudonne','RCA04004WME','filallince769@gmail.com','26G0YP6'),
# (5,'Asifiwe','Marie Angele','RCA04005ZWY','amrieangele@gmail.com','26N0AYB'),
# (6,'Bagumire','Heritier','RCA04006MER','heritierbagumire367@gmail.com','26R0KDN'),
# (7,'Barasingiza','Yasmine','RCA04007NHE','ybarasingiz@gmail.com','26G044P'),
# (8,'Batete','Ange Nadette','RCA04008MEE','bateteangenadette@gmail.com','2720517'),
# (9,'Bera','Auda Beta','RCA04009UEP','audabetabera@gmail.com','27E0LAV'),
# (10,'Bigirabagabo','Braise','RCA04010HJP','bigirabagaboblaise@gmail.com','26G0GBM'),
# (11,'Bikesha','Cyuzuzo Accarie Davine','RCA04011HJV','davinecyuzuzo@gmail.com','272023N'),
# (12,'Bizimana','Louange Lidvine','RCA04012ZZJ','lidvinelouange@gmail.com','277078N'),
# (13,'Byumvuhore','Aimable','RCA04013BNW','aimablebyumvuhore@gmail.com','26905C6'),
# (14,'Cyiza','Kenny Debrice','RCA04014MVU','kennydebrice2@gmail.com','26R0AAP'),
# (15,'Duhirimana','Odile','RCA04015BLG','odileduhirimana@gmail.com','277079E'),
# (16,'Dusabe','Iradukunda Elissa','RCA04016AEN','elissadusabe@gmail.com','26ROH9L'),
# (17,'Fadhili','Josue','RCA04017BWJ','','26V00LK'),
# (18,'Ganza','Aimee Daniella','RCA04018NEL','daniellaganza30@gmail.com','26R0HBM'),
# (19,'Gitoli','Remy Claudien','RCA04019UVE','gitoliremy@gmail.com','26V0K8J'),
# (20,'Habimana','Tony Herve','RCA04020EUE','','2690BLR'),
# (21,'Hakizimana','Yves','RCA04021JRY','hkzmnyves1@gmail.com','26R0GSD'),
# (22,'Hirwa','Ghislain','RCA04022GZJ','ghislainhirwa11@gmail.com','26G0GKS'),
# (23,'Hirwa','Niyonizeye Joric Paladi','RCA04023MMA','','26G0HLK'),
# (24,'Hirwa','Rukundo Hope','RCA04024LWL','gakundohope5@gmail.com','26V01D1'),
# (25,'Ibikoraneza','Dieudonne','RCA04025JNV','dieudonneibikoraneza13@gmail.com','26P0CM2'),
# (26,'Ihirwe','Agasaro Sandra','RCA04026ZMH','sandraihirwe007@gmail.com','26P0DG8'),
# (27,'Ikirenga','Mugisha Herve','RCA04027JBH','','26A0KRV'),
# (28,'Imbabazi','Faith','RCA04028UPH','imbabazifaith007@gmail.com','26R0HA0'),
# (29,'Ineza','Ange Fleurie','RCA04029YGM','angelineza24@gmail.com','26V01CF'),
# (30,'Ineza','Bella Ariane','RCA04030YGN','inezabellaariane@gmail.com','26R01ED'),
# (31,'Ineza','Bella Blandine','RCA04031GEG','bellablandine64@gmail.com','26P0A15'),
# (32,'Ineza','Cinta Castella','RCA04032EGU','castellaine23@gmail.com','26L03VC'),
# (33,'Ineza','Gloria','RCA04033YEN','glorineza2@gmail.com','27E0LBE'),
# (34,'Ineza','Lucky Believe','RCA04034WYM','luckybelieve10@gmail.com','26R0HA2'),
# (35,'Ineza','Munyaneza Celia','RCA04035RPZ','munyanezacelia3gmail.com','26P0CA5'),
# (36,'Ineza','Nicole','RCA04036AHM','rwegoneza12@gmail.com','26R0HA5'),
# (37,'Ineza','Niyongira Bernice','RCA04037PUU','berniceneza1@gmail.com','277078P'),
# (38,'Inezaye','Mukiza Exauce Edolyne','RCA04038JVL','','26P0818'),
# (39,'Iradukunda','Bertin','RCA04039WNY','iradukundabertin082@gmail.com','26R0HAD'),
# (40,'Iranzi','Souvenir','RCA04040LHY','isouvenir345@gmail.com','27E0LBX'),
# (41,'Iratuzi','Giramata Benie','RCA04041MHR','iratuzibeniegiramata@gmail.com','26V00ME'),
# (42,'Irisa','Shimirwa Rolande','RCA04042ZHB','irisarolande125@gmail.com','26V00MN'),
# (43,'Iriza','Joella','RCA04043PAW','irizajoella2006@gmail.com','26G0P3T'),
# (44,'Iriza','Kundwa Stella Celia','RCA04044UVN','kundwairiza@gmail.com','27E0HGP'),
# (45,'Irumva','Regis Dieu Merci','RCA04045EYH','irumvaregisdmc@gmail.com','26R0GXS'),
# (46,'Isamaza','Sylvain','RCA04046JLL','isamazasylvin@gmail.com','26P0808'),
# (47,'Ishema','Blessing Gianna','RCA04047PUL','BlessingGianna7@gmail.com','27202AT'),
# (48,'Ishema','Mudahinyuka Hugues','RCA04048NZJ','huguesishema@gmail.com','2720494'),
# (49,'Ishimwe','Angela Lorie','RCA04049WMP','ishimwelorie45@gmail.com','26G045B'),
# (50,'Ishimwe','Chloe','RCA04050MVR','karlychloee12@gmail.com','26V01CC'),
# (51,'Ishimwe','Fabrice','RCA04051BVE','','2720474'),
# (52,'Ishimwe','Justin','RCA04052MZM','ishimwejustin67@gmail.com','26G0NPF'),
# (53,'Ishimwe','Mugisha Benjamin','RCA04053WZN','benjamugi20072@gmail.com','26R0HA6'),
# (54,'Isimbi','Nina Henriette','RCA04054WEY','ninahenrietterarr@gmail.com','26R0H9F'),
# (55,'Itangamahoro','Divine','RCA04055UVB','lincadivine@gmail.com',''),
# (56,'Iturushimbabazi','Peace Exaucee','RCA04056PZP','iturushimbabazipeace@gmail.com','26518KF'),
# (57,'Jabiro','Christelle','RCA04057LYZ','christejab@gmail.com','26G0G7D'),
# (58,'Kalinda','Sammy','RCA04058BLZ','','26R0H8F'),
# (59,'Karabo','Ineza Emmy Gretta','RCA04059NPA','karabogretta@gmail.com','26N0ALN'),
# (60,'Kayumba','Jean Marie Vianney','RCA04060JGN','kayumbaj88@gmail.com','27204ZA'),
# (61,'Kirezi','Audrey','RCA04061BGL','audreykirezi100@gmail.com','26V014T'),
# (62,'Mbabazi','Louange Liza','RCA04062YYB','mbabazilouangeliza@gmail.com','2770F0Z'),
# (63,'Mico','Dan','RCA04063VML','micodan369@gmail.com','26V01M2'),
# (64,'Micomyiza','Latifa','RCA04064GYE','milatifa481@gmail.com',''),
# (65,'Mucyo','Honorine','RCA04065VAE','honorinemucyo4b@gmail.com','27E0LCY'),
# (66,'Mucyo','Moses','RCA04066VLZ','mosesmanek7@gmail.com','26G0Y4M'),
# (67,'Mugabe','Jean Aime','RCA04067LJL','','26V01DA'),
# (68,'Mugisha','Akuzwe Gisele','RCA04068UWP','giselemigisha53@gmail.com','2720508'),
# (69,'Mugisha','Guy Noel','RCA04069MER','noelmugisha332@gmail.com','272020Y'),
# (70,'Mugisha','Regis','RCA04070LJU','mugisharegis72@gmail.com','26G0GRD'),
# (71,'Mugisha','Shami Innocent','RCA04071JNE','shamiinnocent123@gmail.com','26V0130'),
# (72,'Mugisha','Yves','RCA04072VUB','mugishayves189000@gmail.com','272020B'),
# (73,'Muhirwa','Verygood','RCA04073AHW','verygoodmuhirwa2@gmail.com','26R0H9X'),
# (74,'Mukarusine','Lilian','RCA04074YJJ','mukarusinelilian@gmail.com','27202CM'),
# (75,'Munyaneza','Ishimwe Peace','RCA04075UUB','peaceishimwem@gmail.com','26R0H6Z'),
# (76,'Mushonganono','Teta Sangwa Assia','RCA04076NLN','tetaassia54@gmail.com','272021S'),
# (77,'Musimenta','Gloria','RCA04077WGW','nu.gloria405@gmail.com','27E0L6E'),
# (78,'Muvunyi','Nzivugira Arsene','RCA04078BGY','arsenemuvunyi27@gmail.com','26N0AD8'),
# (79,'Mwesigye','Teta Linda','RCA04079YLW','lindamwesigye2@gmail.com','26V012L'),
# (80,'Mwungere','Elite','RCA04080UHY','','272021Y'),
# (81,'Nduwayo','Nathan','RCA04081ZMH','nduwayonathan5@gmail.com','26N0D5N'),
# (82,'Niyitegeka','Remy Tresor','RCA04082ZMA','niyitegekatresor@gmail.com','26G0GL0'),
# (83,'Nkundabagenzi','Bruce','RCA04083VZM','nbruce420@gmail.com','27EOHH3'),
# (84,'Nkurunziza','Hirwa Andy Melvin','RCA04084HAH','andymelvin56@gmail.com','26V00MN'),
# (85,'Nsengiyumva','Nicola','RCA04085NMR','fatepepe66@gmail.com','26P0CB2'),
# (86,'Nshimyumukiza','Jean De Dieu','RCA04086RVL','jeandedieu2030@gmail.com','26V00LY'),
# (87,'Numwali','Lydia','RCA04087VMA','numwalilydia2022@gmail.com','26GANXF'),
# (88,'Nyiringabo','David','RCA04088JLR','nyiringabodavid62@gmail.com','27204Z2'),
# (89,'Nzabera','Mike Peter','RCA04089VUL','nzaberamikepeter@gmail.com','26G0H7R'),
# (90,'Nzirorera','Divin','RCA04090ARV','divinnzirorera123@gmail.com','26G02V0'),
# (91,'Rudaseswa','Thierry','RCA04091YJV','','2650J3J'),
# (92,'Rukundo','Prince','RCA04092MMG','rukundoprince951@gmail.com','27E0L6V'),
# (93,'Rukundo','Siborurema Christian','RCA04093GRR','siboruremarukundoc@gmail.com','272023P'),
# (94,'Rusizana','Mutoni Belinda','RCA04094NNN','rumu.belynda@gmail.com','272022J'),
# (95,'Rutagengwa','Isimbi Marie Deborah','RCA04095MGG','isdeborah47@gmail.com','272044S'),
# (96,'Sangwa','Hirwa Sean','RCA04096PJG','kdsean11@gmail.com','27201X0'),
# (97,'Sebera','Jonas','RCA04097JYR','jonassebera@gmail.com','2650H3P'),
# (98,'Shema','Frank','RCA04098MMV','shemafrank680@gmail.com','2770F0L'),
# (99,'Shima','Lisa','RCA04099WLV','shimalisa2@gmail.com','26P0DG6'),
# (100,'Shimwa','Kirezi Nicaise','RCA04100NJW','istacaise@gmail.com','26V023S'),
# (101,'Shimwamana','Henri Tresor','RCA04101PGH','shimwamanahenritresor@gmail.com','26N0ACZ'),
# (102,'Sibomana','Edouard','RCA04102PUP','siboedouard@88gmail.com','272044S'),
# (103,'Sibomana','Elissa','RCA04103NWL','sibomanaelissa71@gmail.com','26V01CG'),
# (104,'Tuyishime','Naome','RCA04104LVW','tuyishimenaome27@gmail.com','27202AZ'),
# (105,'Tuyizere','Kevin','RCA04105WNP','tuyizerek27@gmail.com','27E0KLH'),
# (106,'Uganase','Ishimwe Arsene','RCA04106UMU','arsenuga11@gmail.com','26G0HGL'),
# (107,'Uhiriwe','Anne Leslie','RCA04107PGB','anneuhiriwe@gmail.com','26V015M'),
# (108,'Umulisa','Ornella','RCA04108UUG','lisanella509@gmail.com','26G0P43'),
# (109,'Umutoni','Kaze Joanna Michelle','RCA04109WWZ','ukjoannamichelle@gmail.com','2770BR6'),
# (110,'Umutoni','Rita','RCA04110JBB','umurita37@gmail.com','27E04SK'),
# (111,'Umwari','Denise','RCA04111MLM','denyseumwari850@gmail.com','26R0GX2'),
# (112,'Usanase','Alleluia Queen Doris','RCA04112AUB','usanasequeen@gmail.com','26V03HW'),
# (113,'Usanase','Sheja Joie Darlene','RCA04113MJH','joiedarlene02@gmail.com','27202BZ'),
# (114,'Uwajuru','Singizwa Ella','RCA04114VGW','ellapacissingizwa@gmail.com','26V01D8'),
# (115,'Uwase','Agnes','RCA04115UVZ','uwaseagnnes@gmail.com','26N0ALK'),
# (116,'Uwase','Seminega Vanessa','RCA04116ZJP','vanessauwase121@gmail.com','26G0TDK'),
# (117,'Uwimana','Remy Chiessa','RCA04117NRA','remychiesa14@gmail.com','26G02PP'),
# (118,'Uwimfura','Zam Zam','RCA04118GPV','uwimfuraz@gmail.com','2770797'),
# (119,'Uwineza','Honorine','RCA04119HLN','honorineuwineza077@gmail.com','2690CFR'),
# (120,'Uwumviyimana','Asterie','RCA04120MUR','uwasterie07@gmail.com','26G0YAR');
# ''')
# cursor.execute('DELETE FROM missing;')
# cursor.execute('''
# ALTER TABLE missing DROP COLUMN owner;
# ''')
# cursor.execute('''
# ALTER TABLE missing ADD owner text NOT NULL
# ''')
cursor.execute('''
UPDATE cable
SET cable_ID = '27E0LAV'
WHERE rca_id = 'RCA04053WZN';
''')
connection.commit()
# data = cursor.execute('SELECT * FROM cable')
# data = data.fetchall()
# for i in data:
#     print(i)
print('done...')