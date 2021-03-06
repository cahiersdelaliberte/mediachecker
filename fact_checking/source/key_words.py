# Listes des mots à rechercher dans les articles.
# Elles sont composées de couples ("thème", "mot clef").

# éléments figurant dans le fichier
# https://docs.google.com/spreadsheets/d/12ElwEojNy9w7mYtwlERt_YcHwtcfAja3EhSrYWVu_TI/edit#gid=0
spreadsheet_words = [("emploi","chômage"),
("emploi","chômeurs"),
("emploi","chômeur"),
("emploi","emploi"),
("emploi","travail"),
("emploi","diplômé"),
("emploi","diplômés"),
("emploi","jeune diplômé"),
("emploi","jeunes diplômés"),
("emploi","PIB"),
("emploi","PNB"),
("activité","croissance"),
("activité","industrie"),
("activité","concurrence"),
("activité","marchés"),
("activité","marché"),
("activité","entreprise"),
("budget","budget"),
("budget","déficit"),
("budget","dette"),
("budget","équilibre"),
("budget","solde"),
("budget","dépenses"),
("budget","recettes"),
("fiscalité","taxe"),
("fiscalité","fiscalité"),
("fiscalité","impôt"),
("fiscalité","TVA"),
("fiscalité","impôt sur les sociétés"),
("sécurité sociale","sécurité sociale"),
("sécurité sociale","cotisation"),
("sécurité sociale","charge"),
("commerce international","commerce international"),
("commerce international","importations"),
("commerce international","exportations"),
("commerce international","balance"),
("commerce international","balance commerciale"),
("commerce international","balance courante"),
("commerce international","balance des changes"),
("commerce international","réserves de changes"),
("politique monétaire","politique monétaire"),
("politique monétaire","inflation"),
("politique monétaire","taux directeur"),
("politique monétaire","banque centrale"),
("élection","circonscription"),
("élection","élections"),
("élection","élection"),
("élection","vote"),
("élection","scrutin"),
("élection","résultat électoral"),
("élection","programme électoral"),
("élection","bulletin de vote"),
("élection","bureau de vote"),
("élection","élections municipales"),
("contestation","contestation"),
("contestation","manifestation"),
("contestation","manifestant"),
("organisation locale","municipalités"),
("organisation locale","maire"),
("organisation locale","région"),
("organisation locale","gouvernorat"),
("organisation locale","gouverneur")]


#liste des députés scrappée au 01/08/2019 > liste_deputes.csv
deputes = [
    ("ARP 2014", "Abdelkader Ben Dhifallah"),
    ("ARP 2014", "Mohamed Nejib Torjmane"),
    ("ARP 2014", "Mongi Rahoui"),
    ("ARP 2014", "Abderraouf Chebbi"),
    ("ARP 2014", "Mohamed Jalel Ghedira"),
    ("ARP 2014", "Mohamed Ali Bedoui"),
    ("ARP 2014", "Hssine Yahyaoui"),
    ("ARP 2014", "Latifa Habachi"),
    ("ARP 2014", "Hela Omrane"),
    ("ARP 2014", "Noureddine Mrabti"),
    ("ARP 2014", "Jilani Hammami"),
    ("ARP 2014", "Monia Brahim"),
    ("ARP 2014", "Dalila Babba"),
    ("ARP 2014", "Ons Hattab"),
    ("ARP 2014", "Salah Bargaoui"),
    ("ARP 2014", "Samia Abbou"),
    ("ARP 2014", "Houda Slim"),
    ("ARP 2014", "Noura Amri"),
    ("ARP 2014", "Lotfi Ali"),
    ("ARP 2014", "Ridha Charfeddine"),
    ("ARP 2014", "Issam Matoussi"),
    ("ARP 2014", "Nozha Biaoui"),
    ("ARP 2014", "Ramzi Ben Fraj"),
    ("ARP 2014", "Sabrine Goubantini"),
    ("ARP 2014", "Aroua Ben Abbas"),
    ("ARP 2014", "Ahmed Seddik"),
    ("ARP 2014", "Mohamed Mohsen Soudani"),
    ("ARP 2014", "Hayet Omri"),
    ("ARP 2014", "Noureddine Bhiri"),
    ("ARP 2014", "Leila Hamrouni"),
    ("ARP 2014", "Mohamed Hedi Gueddich"),
    ("ARP 2014", "Kamel Dhaouadi"),
    ("ARP 2014", "Lamia Dridi"),
    ("ARP 2014", "Maher Madhioub"),
    ("ARP 2014", "Fathi Ayadi"),
    ("ARP 2014", "Safia Khalfi"),
    ("ARP 2014", "Hedi Ben Braham"),
    ("ARP 2014", "Mohamed Ghannem"),
    ("ARP 2014", "Karima  Taggaz"),
    ("ARP 2014", "Ammar Amroussia"),
    ("ARP 2014", "Lamia Mlayah"),
    ("ARP 2014", "Sahbi Atig"),
    ("ARP 2014", "Karim Helali"),
    ("ARP 2014", "Radhia Toumi"),
    ("ARP 2014", "Sameh Bouhaouel"),
    ("ARP 2014", "Hssan Amri"),
    ("ARP 2014", "Abdelfattah Mourou"),
    ("ARP 2014", "Walid Jalled"),
    ("ARP 2014", "Leila Zahaf"),
    ("ARP 2014", "Imed Khemiri"),
    ("ARP 2014", "Abderrazak Chraiet"),
    ("ARP 2014", "Jihen Aouichi"),
    ("ARP 2014", "Soulef Ksantini"),
    ("ARP 2014", "Ibtihej Ben Helal"),
    ("ARP 2014", "Ismail Ben Mahmoud"),
    ("ARP 2014", "Mohamed Ennaceur Jbira"),
    ("ARP 2014", "Moncef Sellami"),
    ("ARP 2014", "Yamina Zoghlami"),
    ("ARP 2014", "Mourad Hamaidi"),
    ("ARP 2014", "Ali Bennour"),
    ("ARP 2014", "Ameur Laraiedh"),
    ("ARP 2014", "Noureddine Ben Achour"),
    ("ARP 2014", "Ibrahim Ben Said"),
    ("ARP 2014", "Zied Lakhdhar"),
    ("ARP 2014", "Hela Hammi"),
    ("ARP 2014", "Ferida Laabidi"),
    ("ARP 2014", "Tarek Barrak"),
    ("ARP 2014", "Leila Oueslati"),
    ("ARP 2014", "Imed Daimi"),
    ("ARP 2014", "Haykel Belgacem"),
    ("ARP 2014", "Mohamed Ramzi Khmiss"),
    ("ARP 2014", "Amira Zoukari"),
    ("ARP 2014", "Houcine Jaziri"),
    ("ARP 2014", "Mohamed Troudi"),
    ("ARP 2014", "Faycel Tebini"),
    ("ARP 2014", "Heger Ben Cheikh Ahmed"),
    ("ARP 2014", "Ali Belakhoua"),
    ("ARP 2014", "Lilia Younes Ksibi"),
    ("ARP 2014", "Mohamed El Hamdi"),
    ("ARP 2014", "Mounir Hamdi"),
    ("ARP 2014", "Souhail Alouini"),
    ("ARP 2014", "Ali Laraiedh"),
    ("ARP 2014", "Heger Laaroussi"),
    ("ARP 2014", "Sabri Dekhil"),
    ("ARP 2014", "Mohamed Lakhdhar Lajili"),
    ("ARP 2014", "Sana Mersni"),
    ("ARP 2014", "Maroua Bouazzi"),
    ("ARP 2014", "Dorra Yaacoubi"),
    ("ARP 2014", "El Khansa Ben Harrath"),
    ("ARP 2014", "Brahim Nacef"),
    ("ARP 2014", "Asma Abou Hana"),
    ("ARP 2014", "Mohamed Zrig"),
    ("ARP 2014", "Leila Ouled Ali"),
    ("ARP 2014", "Sahbi Ben Fraj"),
    ("ARP 2014", "Nizar Amami"),
    ("ARP 2014", "Zeineb Brahmi"),
    ("ARP 2014", "Mohamed Abdellaoui"),
    ("ARP 2014", "Khemais Ksila"),
    ("ARP 2014", "Marouan Falfel"),
    ("ARP 2014", "Nesrine Laamari"),
    ("ARP 2014", "Houssem Bounenni"),
    ("ARP 2014", "Abderraouf El May"),
    ("ARP 2014", "Ibtissem Jebabli"),
    ("ARP 2014", "Mohamed Amine Kahloul"),
    ("ARP 2014", "Mahmoud Gouiaa"),
    ("ARP 2014", "Olfa Jouini"),
    ("ARP 2014", "Bechir Ellazzem"),
    ("ARP 2014", "Jamila Debbech"),
    ("ARP 2014", "Houda Tekaya"),
    ("ARP 2014", "Nadia Zangar"),
    ("ARP 2014", "Faouzia Ben Fodha"),
    ("ARP 2014", "Ahmed Mechergui"),
    ("ARP 2014", "Mohamed Saidane"),
    ("ARP 2014", "Hassouna Nasfi"),
    ("ARP 2014", "Sana Salhi"),
    ("ARP 2014", "Mbarka Aouania "),
    ("ARP 2014", "Adnane Hajji"),
    ("ARP 2014", "Lamia Gharbi"),
    ("ARP 2014", "Youssef Jouini"),
    ("ARP 2014", "Abdelouahab Ouerfelli"),
    ("ARP 2014", "Moez Belhaj Rhouma"),
    ("ARP 2014", "Taoufik Ouali"),
    ("ARP 2014", "Ghazi Chaouachi"),
    ("ARP 2014", "Mohamed Kamel Besbes"),
    ("ARP 2014", "Zouhair Rejbi"),
    ("ARP 2014", "Sami Fetnassi"),
    ("ARP 2014", "Zohra Idriss"),
    ("ARP 2014", "Lajmi Lourimi"),
    ("ARP 2014", "Jihene Abadi"),
    ("ARP 2014", "Kamel Harraghi"),
    ("ARP 2014", "Oussama Al Sghaier"),
    ("ARP 2014", "Ahmed Saidi"),
    ("ARP 2014", "Mustapha Ben Ahmed"),
    ("ARP 2014", "Mohamed Anouar Adhar"),
    ("ARP 2014", "Ikram Moulahi"),
    ("ARP 2014", "Nawel Tayech"),
    ("ARP 2014", "Zouhair Maghzaoui"),
    ("ARP 2014", "Badreddine Abdelkefi"),
    ("ARP 2014", "Hmed Khaskhoussi"),
    ("ARP 2014", "Walid Banneni"),
    ("ARP 2014", "Imen Ben Mhamed"),
    ("ARP 2014", "Noomane El Euch"),
    ("ARP 2014", "Ahmed Ameri"),
    ("ARP 2014", "Fathi Chamkhi"),
    ("ARP 2014", "Abdelmoumen Belanes"),
    ("ARP 2014", "Kalthoum Badreddine"),
    ("ARP 2014", "Habib Khedher"),
    ("ARP 2014", "Meriem Boujbel"),
    ("ARP 2014", "Souad Zaouali"),
    ("ARP 2014", "Najia Ben Abdelhafidh"),
    ("ARP 2014", "Abdelaziz Kotti"),
    ("ARP 2014", "Bechir Khelifi"),
    ("ARP 2014", "Taieb Medni"),
    ("ARP 2014", "Olfa Soukri"),
    ("ARP 2014", "Nadhir Ben Ammou"),
    ("ARP 2014", "Mohamed Fadhel Ben Omrane"),
    ("ARP 2014", "Sameh Dammak"),
    ("ARP 2014", "Amal Souid"),
    ("ARP 2014", "Bechir Ben Amor"),
    ("ARP 2014", "Rabha Ben Hassine"),
    ("ARP 2014", "Yassine Ayari"),
    ("ARP 2014", "Ali Ben Salem"),
    ("ARP 2014", "Samir Dilou"),
    ("ARP 2014", "Mohamed Mahjoub"),
    ("ARP 2014", "Mahmoud Kahri"),
    ("ARP 2014", "Chafik Ayadi"),
    ("ARP 2014", "Ridha Dellai"),
    ("ARP 2014", "Meherzia Laabidi"),
    ("ARP 2014", "Chaker Ayadi"),
    ("ARP 2014", "Ridha Zghondi"),
    ("ARP 2014", "Abir Abdelli"),
    ("ARP 2014", "Wafa Makhlouf"),
    ("ARP 2014", "Belgacem Dkhili"),
    ("ARP 2014", "Taoufik Jemli"),
    ("ARP 2014", "Jamila Jouini"),
    ("ARP 2014", "Fatma Mseddi"),
    ("ARP 2014", "Mohamed Ben Salem"),
    ("ARP 2014", "Mondher Belhaj Ali"),
    ("ARP 2014", "Neji Jmal"),
    ("ARP 2014", "Mabrouk Hrizi"),
    ("ARP 2014", "Souad Bayouli"),
    ("ARP 2014", "Naceur Channoufi"),
    ("ARP 2014", "Chahida Fraj"),
    ("ARP 2014", "Hedi Soula"),
    ("ARP 2014", "Abdennaceur Chouikh"),
    ("ARP 2014", "Lotfi Nabli"),
    ("ARP 2014", "Najla Saadaoui"),
    ("ARP 2014", "Mongi Harbaoui"),
    ("ARP 2014", "Faycel Khelifa"),
    ("ARP 2014", "Imed Ouled Jebril"),
    ("ARP 2014", "Mohamed Frikha"),
    ("ARP 2014", "Chakib Bani"),
    ("ARP 2014", "Riadh Jaidane"),
    ("ARP 2014", "Leila ِChettaoui Bougatef"),
    ("ARP 2014", "Naoufel Jammali"),
    ("ARP 2014", "Tahar Fdhil"),
    ("ARP 2014", "Khawla Ben Aicha"),
    ("ARP 2014", "Tarek Fetiti"),
    ("ARP 2014", "Mohamed Ben Souf"),
    ("ARP 2014", "Mohamed Rachdi Bouguerra"),
    ("ARP 2014", "Wafa Attia"),
    ("ARP 2014", "Heger Bouzemmi"),
    ("ARP 2014", "Rim Mahjoub"),
    ("ARP 2014", "Hager Triki"),
    ("ARP 2014", "Mohamed Sidhom"),
    ("ARP 2014", "Bochra Belhaj Hamida"),
    ("ARP 2014", "Emna Ben Hmayed"),
    ("ARP 2014", "Abdellatif Mekki"),
    ("ARP 2014", "Hafedh Zouari"),
    ("ARP 2014", "Lakhdhar Belhouchat"),
    ("ARP 2014", "Slim Besbes"),
    ("ARP 2014", "Rim Thairi"),
    ("ARP 2014", "Aymen Aloui"),
    ("ARP 2014", "Sofien Toubel"),
    ("ARP 2014", "Salem Labiadh"),
    ("ARP 2014", "Mahbouba Ben Dhifallah")
]

candidats_presidentielles_2019 = [
    ('présidentielles 2019', 'Mohamed Abbou'),
    ('présidentielles 2019', 'Said Aidi'), ('présidentielles 2019', 'Saïd Aydi'),
    ('présidentielles 2019', 'Hatem Boulabiar'),
    ('présidentielles 2019', 'Abid Briki'),
    ('présidentielles 2019', 'Youssef Chahed'),
    ('présidentielles 2019', 'Salma Elloumi'), ('présidentielles 2019', 'Selma Elloumi'),
    ('présidentielles 2019', 'Elyes Fakhfakh'), ('présidentielles 2019', 'Elyès Fakhfakh'),
    ('présidentielles 2019', 'Hachmi Hamdi'), ('présidentielles 2019', 'Hechmi Hamdi'),
    ('présidentielles 2019', 'Hamma Hammami'),
    ('présidentielles 2019', 'Neji Jalloul'),
    ('présidentielles 2019', 'Hammadi Jbeli'), ('présidentielles 2019', 'Hamadi Jebali'),
    ('présidentielles 2019', 'Mahdi Jomaa'), ('présidentielles 2019', 'Mehdi Jomaâ'),
    ('présidentielles 2019', 'Nabil Karoui'),
    ('présidentielles 2019', 'Seifeddine Makhlouf'),
    ('présidentielles 2019', 'Omar Mansour'),
    ('présidentielles 2019', 'Mohsen Marzouk'),
    ('présidentielles 2019', 'Moncef Marzouki'),
    ('présidentielles 2019', 'Abdelfattah Mourou'),
    ('présidentielles 2019', 'Abir Moussi'),
    ('présidentielles 2019', 'Mohamed Lotfi Mraihi'), ('présidentielles 2019', 'Mohamed Lotfi Mraïhi'),
    ('présidentielles 2019', 'Mohamed Sghaier Nouri'), ('présidentielles 2019', 'Mohamed Nouri'),
    ('présidentielles 2019', 'Mongi Rahoui'),
    ('présidentielles 2019', 'Slim Riahi'),
    ('présidentielles 2019', 'Safi Said'), ('présidentielles 2019', 'Safi Saïd'),
    ('présidentielles 2019', 'Kais Saied'), ('présidentielles 2019', 'Kais Saïed'),
    ('présidentielles 2019', 'Abdelkarim Zbidi')
]

key_words_list = [
    ('élection', 'circonscription'),
    ('élection', 'liste'),
    ('ISIE 2019', 'Nabil Baffoun'),
    ('présidence', 'Mohamed Ennaceur')
    ] + spreadsheet_words + deputes + candidats_presidentielles_2019
