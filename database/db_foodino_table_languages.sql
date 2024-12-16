-- MySQL dump 10.13  Distrib 8.0.27, for Win64 (x86_64)
--
-- Host: localhost    Database: db_foodino
-- ------------------------------------------------------
-- Server version	8.0.27

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `table_languages`
--

DROP TABLE IF EXISTS `table_languages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `table_languages` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `language_code` varchar(20) NOT NULL,
  `language_name` varchar(120) NOT NULL,
  `language_directionality` varchar(120) NOT NULL,
  `language_is_active` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=541 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `table_languages`
--

LOCK TABLES `table_languages` WRITE;
/*!40000 ALTER TABLE `table_languages` DISABLE KEYS */;
INSERT INTO `table_languages` VALUES (271,'aa','Afar','ltr',0),(272,'ab','Abkhazian','ltr',0),(273,'af','Afrikaans','ltr',0),(274,'ak','Akan','ltr',0),(275,'als','Alemannic','ltr',0),(276,'am','Amharic','ltr',0),(277,'an','Aragonese','ltr',0),(278,'ang','Anglo-Saxon / Old English','ltr',0),(279,'ar','Arabic','rtl',0),(280,'arc','Aramaic','rtl',0),(281,'arz','Egyptian Arabic','rtl',0),(282,'as','Assamese','ltr',0),(283,'ast','Asturian','ltr',0),(284,'av','Avar','ltr',0),(285,'awa','Awadhi','ltr',0),(286,'ay','Aymara','ltr',0),(287,'az','Azerbaijani','ltr',0),(288,'ba','Bashkir','ltr',0),(289,'bar','Bavarian','ltr',0),(290,'bat-smg','Samogitian','ltr',0),(291,'bcl','Bikol','ltr',0),(292,'be','Belarusian','ltr',0),(293,'be-x-old','Belarusian (Taraškievica)','ltr',0),(294,'bg','Bulgarian','ltr',0),(295,'bh','Bihari','ltr',0),(296,'bi','Bislama','ltr',0),(297,'bm','Bambara','ltr',0),(298,'bn','Bengali','ltr',0),(299,'bo','Tibetan','ltr',0),(300,'bpy','Bishnupriya Manipuri','ltr',0),(301,'br','Breton','ltr',0),(302,'brx','Boro','ltr',0),(303,'bs','Bosnian','ltr',0),(304,'bug','Buginese','ltr',0),(305,'bxr','Buriat (Russia)','ltr',0),(306,'ca','Catalan','ltr',0),(307,'cdo','Min Dong Chinese','ltr',0),(308,'ce','Chechen','ltr',0),(309,'ceb','Cebuano','ltr',0),(310,'ch','Chamorro','ltr',0),(311,'cho','Choctaw','ltr',0),(312,'chr','Cherokee','ltr',0),(313,'chy','Cheyenne','ltr',0),(314,'ckb','Kurdish (Sorani)','rtl',0),(315,'co','Corsican','ltr',0),(316,'cr','Cree','ltr',0),(317,'crn','Montenegrin','ltr',0),(318,'cs','Czech','ltr',0),(319,'csb','Kashubian','ltr',0),(320,'cu','Old Church Slavonic / Old Bulgarian','ltr',0),(321,'cv','Chuvash','ltr',0),(322,'cy','Welsh','ltr',0),(323,'da','Danish','ltr',0),(324,'de','German','ltr',0),(325,'diq','Dimli','ltr',0),(326,'dsb','Lower Sorbian','ltr',0),(327,'dv','Divehi','rtl',0),(328,'dz','Dzongkha','ltr',0),(329,'ee','Ewe','ltr',0),(330,'el','Greek','ltr',0),(331,'en','English','ltr',1),(332,'eo','Esperanto','ltr',0),(333,'es','Spanish','ltr',0),(334,'et','Estonian','ltr',0),(335,'eu','Basque','ltr',0),(336,'ext','Extremaduran','ltr',0),(337,'fa','Persian','rtl',0),(338,'ff','Peul','ltr',0),(339,'fi','Finnish','ltr',0),(340,'fiu-vro','Võro','ltr',0),(341,'fj','Fijian','ltr',0),(342,'fo','Faroese','ltr',0),(343,'fr','French','ltr',0),(344,'frp','Arpitan / Franco-Provençal','ltr',0),(345,'fur','Friulian','ltr',0),(346,'fy','West Frisian','ltr',0),(347,'ga','Irish','ltr',0),(348,'gan','Gan Chinese','ltr',0),(349,'gbm','Garhwali','ltr',0),(350,'gd','Scottish Gaelic','ltr',0),(351,'gil','Gilbertese','ltr',0),(352,'gl','Galician','ltr',0),(353,'gn','Guarani','ltr',0),(354,'got','Gothic','ltr',0),(355,'gu','Gujarati','ltr',0),(356,'gv','Manx','ltr',0),(357,'ha','Hausa','rtl',0),(358,'hak','Hakka Chinese','ltr',0),(359,'haw','Hawaiian','ltr',0),(360,'he','Hebrew','rtl',0),(361,'hi','Hindi','ltr',0),(362,'ho','Hiri Motu','ltr',0),(363,'hr','Croatian','ltr',0),(364,'ht','Haitian','ltr',0),(365,'hu','Hungarian','ltr',0),(366,'hy','Armenian','ltr',0),(367,'hz','Herero','ltr',0),(368,'ia','Interlingua','ltr',0),(369,'id','Indonesian','ltr',0),(370,'ie','Interlingue','ltr',0),(371,'ig','Igbo','ltr',0),(372,'ii','Sichuan Yi','ltr',0),(373,'ik','Inupiak','ltr',0),(374,'ilo','Ilokano','ltr',0),(375,'inh','Ingush','ltr',0),(376,'io','Ido','ltr',0),(377,'is','Icelandic','ltr',0),(378,'it','Italian','ltr',0),(379,'iu','Inuktitut','ltr',0),(380,'ja','Japanese','ltr',0),(381,'jbo','Lojban','ltr',0),(382,'jv','Javanese','ltr',0),(383,'ka','Georgian','ltr',0),(384,'kg','Kongo','ltr',0),(385,'ki','Kikuyu','ltr',0),(386,'kj','Kuanyama','ltr',0),(387,'kk','Kazakh','ltr',0),(388,'kl','Greenlandic','ltr',0),(389,'km','Cambodian','ltr',0),(390,'kn','Kannada','ltr',0),(391,'khw','Khowar','rtl',0),(392,'ko','Korean','ltr',0),(393,'kr','Kanuri','ltr',0),(394,'ks','Kashmiri','rtl',0),(395,'ksh','Ripuarian','ltr',0),(396,'ku','Kurdish (Kurmanji)','ltr',0),(397,'kv','Komi','ltr',0),(398,'kw','Cornish','ltr',0),(399,'ky','Kirghiz','ltr',0),(400,'la','Latin','ltr',0),(401,'lad','Ladino / Judeo-Spanish','ltr',0),(402,'lan','Lango','ltr',0),(403,'lb','Luxembourgish','ltr',0),(404,'lg','Ganda','ltr',0),(405,'li','Limburgian','ltr',0),(406,'lij','Ligurian','ltr',0),(407,'lmo','Lombard','ltr',0),(408,'ln','Lingala','ltr',0),(409,'lo','Laotian','ltr',0),(410,'lzz','Laz','ltr',0),(411,'lt','Lithuanian','ltr',0),(412,'lv','Latvian','ltr',0),(413,'map-bms','Banyumasan','ltr',0),(414,'mg','Malagasy','ltr',0),(415,'man','Mandarin','ltr',0),(416,'mh','Marshallese','ltr',0),(417,'mi','Māori','ltr',0),(418,'min','Minangkabau','ltr',0),(419,'mk','Macedonian','ltr',0),(420,'ml','Malayalam','ltr',0),(421,'mn','Mongolian','ltr',0),(422,'mo','Moldovan','ltr',0),(423,'mr','Marathi','ltr',0),(424,'mrh','Mara','ltr',0),(425,'ms','Malay','ltr',0),(426,'mt','Maltese','ltr',0),(427,'mus','Creek / Muskogee','ltr',0),(428,'mwl','Mirandese','ltr',0),(429,'my','Burmese','ltr',0),(430,'na','Nauruan','ltr',0),(431,'nah','Nahuatl','ltr',0),(432,'nap','Neapolitan','ltr',0),(433,'nd','North Ndebele','ltr',0),(434,'nds','Low German / Low Saxon','ltr',0),(435,'nds-nl','Dutch Low Saxon','ltr',0),(436,'ne','Nepali','ltr',0),(437,'new','Newar','ltr',0),(438,'ng','Ndonga','ltr',0),(439,'nl','Dutch','ltr',0),(440,'nn','Norwegian Nynorsk','ltr',0),(441,'no','Norwegian','ltr',0),(442,'nr','South Ndebele','ltr',0),(443,'nso','Northern Sotho','ltr',0),(444,'nrm','Norman','ltr',0),(445,'nv','Navajo','ltr',0),(446,'ny','Chichewa','ltr',0),(447,'oc','Occitan','ltr',0),(448,'oj','Ojibwa','ltr',0),(449,'om','Oromo','ltr',0),(450,'or','Oriya','ltr',0),(451,'os','Ossetian / Ossetic','ltr',0),(452,'pa','Panjabi / Punjabi','ltr',0),(453,'pag','Pangasinan','ltr',0),(454,'pam','Kapampangan','ltr',0),(455,'pap','Papiamentu','ltr',0),(456,'pdc','Pennsylvania German','ltr',0),(457,'pi','Pali','ltr',0),(458,'pih','Norfolk','ltr',0),(459,'pl','Polish','ltr',0),(460,'pms','Piedmontese','ltr',0),(461,'ps','Pashto','rtl',0),(462,'pt','Portuguese','ltr',0),(463,'qu','Quechua','ltr',0),(464,'rm','Raeto Romance','ltr',0),(465,'rmy','Romani','ltr',0),(466,'rn','Kirundi','ltr',0),(467,'ro','Romanian','ltr',0),(468,'roa-rup','Aromanian','ltr',0),(469,'ru','Russian','ltr',0),(470,'rw','Rwandi','ltr',0),(471,'sa','Sanskrit','ltr',0),(472,'sc','Sardinian','ltr',0),(473,'scn','Sicilian','ltr',0),(474,'sco','Scots','ltr',0),(475,'sd','Sindhi','rtl',0),(476,'se','Northern Sami','ltr',0),(477,'sg','Sango','ltr',0),(478,'sh','Serbo-Croatian','ltr',0),(479,'si','Sinhalese','ltr',0),(480,'simple','Simple English','ltr',0),(481,'sk','Slovak','ltr',0),(482,'sl','Slovenian','ltr',0),(483,'sm','Samoan','ltr',0),(484,'sn','Shona','ltr',0),(485,'so','Somalia','ltr',0),(486,'sq','Albanian','ltr',0),(487,'sr','Serbian','ltr',0),(488,'ss','Swati','ltr',0),(489,'st','Southern Sotho','ltr',0),(490,'su','Sundanese','ltr',0),(491,'sv','Swedish','ltr',0),(492,'sw','Swahili','ltr',0),(493,'ta','Tamil','ltr',0),(494,'te','Telugu','ltr',0),(495,'tet','Tetum','ltr',0),(496,'tg','Tajik','ltr',0),(497,'th','Thai','ltr',0),(498,'ti','Tigrinya','ltr',0),(499,'tk','Turkmen','ltr',0),(500,'tl','Tagalog','ltr',0),(501,'tlh','Klingon','ltr',0),(502,'tn','Tswana','ltr',0),(503,'to','Tonga','ltr',0),(504,'tpi','Tok Pisin','ltr',0),(505,'tr','Turkish','ltr',0),(506,'ts','Tsonga','ltr',0),(507,'tt','Tatar','ltr',0),(508,'tum','Tumbuka','ltr',0),(509,'tw','Twi','ltr',0),(510,'ty','Tahitian','ltr',0),(511,'udm','Udmurt','ltr',0),(512,'ug','Uyghur','ltr',0),(513,'uk','Ukrainian','ltr',0),(514,'ur','Urdu','rtl',0),(515,'uz','Uzbek','ltr',0),(516,'uz_AF','Uzbeki Afghanistan','rtl',0),(517,'ve','Venda','ltr',0),(518,'vi','Vietnamese','ltr',0),(519,'vec','Venetian','ltr',0),(520,'vls','West Flemish','ltr',0),(521,'vo','Volapük','ltr',0),(522,'wa','Walloon','ltr',0),(523,'war','Waray / Samar-Leyte Visayan','ltr',0),(524,'wo','Wolof','ltr',0),(525,'xal','Kalmyk','ltr',0),(526,'xh','Xhosa','ltr',0),(527,'xmf','Megrelian','ltr',0),(528,'yi','Yiddish','rtl',0),(529,'yo','Yoruba','ltr',0),(530,'za','Zhuang','ltr',0),(531,'zg','Moroccan Amazigh','ltr',0),(532,'zh','Chinese','ltr',0),(533,'zh-classical','Classical Chinese','ltr',0),(534,'zh-min-nan','Minnan','ltr',0),(535,'zh-yue','Cantonese','ltr',0),(536,'zu','Zulu','ltr',0),(537,'closed-zh-tw','Traditional Chinese','ltr',0),(538,'nb','Norwegian Bokmål','ltr',0),(539,'zh-tw','Traditional Chinese','ltr',0),(540,'tokipona','tokipona','ltr',0);
/*!40000 ALTER TABLE `table_languages` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-08-05 16:47:53
