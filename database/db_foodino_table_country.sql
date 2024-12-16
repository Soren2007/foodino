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
-- Table structure for table `table_country`
--

DROP TABLE IF EXISTS `table_country`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `table_country` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(250) NOT NULL,
  `photo_of_the_flag` varchar(100) DEFAULT NULL,
  `telephone_code` varchar(50) DEFAULT NULL,
  `is_translated_content` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=234 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `table_country`
--

LOCK TABLES `table_country` WRITE;
/*!40000 ALTER TABLE `table_country` DISABLE KEYS */;
INSERT INTO `table_country` VALUES (1,'آذربایجان','images/account/country/NaN.png','۹۹۴',1),(2,'افغانستان','images/account/country/NaN.png','۹۳',1),(3,'ارمنستان','images/account/country/NaN.png','+98',1),(4,'امارات متحده عربی','images/account/country/NaN.png','+98',1),(5,'اردن','images/account/country/NaN.png','۹۶۲',1),(6,'ایران','images/account/country/NaN.png','۹۸',1),(7,'بنگلادش','images/account/country/NaN.png','۸۸۰',1),(8,'بوتان','images/account/country/NaN.png','۲۶۷',1),(9,'برونئی','images/account/country/NaN.png','+98',1),(10,'کامبوج','images/account/country/NaN.png','۸۵۵',1),(11,'چین','images/account/country/NaN.png','۸۶',1),(12,'قبرس','images/account/country/NaN.png','۳۵۷',1),(13,'گرجستان','images/account/country/NaN.png','۹۵۵',1),(14,'هند','images/account/country/NaN.png','۹۱',1),(15,'اندونزی','images/account/country/NaN.png','۶۲',1),(16,'عراق','images/account/country/NaN.png','۹۶۴',1),(17,'ژاپن','images/account/country/NaN.png','۸۱',1),(18,'قزاقستان','images/account/country/NaN.png','+98',1),(19,'کویت','images/account/country/NaN.png','۹۶۵',1),(20,'قرقیزستان','images/account/country/NaN.png','۷۳۳۱',1),(21,'لائوس','images/account/country/NaN.png','۸۵۶',1),(22,'لبنان','images/account/country/NaN.png','۹۶۱',1),(23,'مالزی','images/account/country/NaN.png','۶۰',1),(24,'مالدیو','images/account/country/NaN.png','۹۶۰',1),(25,'مغولستان','images/account/country/NaN.png','۹۷۶',1),(26,'میانمار (برمه)','images/account/country/NaN.png','+98',1),(27,'نپال','images/account/country/NaN.png','۹۷۷',1),(28,'کره شمالی','images/account/country/NaN.png','۸۵۰',1),(29,'عمان','images/account/country/NaN.png','۹۶۸',1),(30,'پاکستان','images/account/country/NaN.png','۹۲',1),(31,'فلسطین','images/account/country/NaN.png','+98',1),(32,'فیلیپین','images/account/country/NaN.png','۶۳',1),(33,'قطر','images/account/country/NaN.png','۹۷۴',1),(34,'روسیه','images/account/country/NaN.png','۷۰۹۵',1),(35,'عربستان سعودی','images/account/country/NaN.png','+98',1),(36,'سنگاپور','images/account/country/NaN.png','+98',1),(37,'کره جنوبی','images/account/country/NaN.png','۸۲',1),(38,'سریلانکا','images/account/country/NaN.png','۹۴',1),(39,'سوریه','images/account/country/NaN.png','۹۶۳',1),(40,'تایوان','images/account/country/NaN.png','۸۸۶',1),(41,'تاجیکستان','images/account/country/NaN.png','۹۹۲',1),(42,'تایلند','images/account/country/NaN.png','۶۶',1),(43,'تیمور شرقی','images/account/country/NaN.png','+98',1),(44,'ترکیه','images/account/country/NaN.png','۹۰',1),(45,'ترکمنستان','images/account/country/NaN.png','۷۳۶۳',1),(46,'ازبکستان','images/account/country/NaN.png','۷۳۷۱',1),(47,'ویتنام','images/account/country/NaN.png','۸۴',1),(48,'یمن','images/account/country/NaN.png','+98',1),(49,'الجزایر','images/account/country/NaN.png','۲۱۳',1),(50,'آنگولا','images/account/country/NaN.png','۲۴۴',1),(51,'بنین','images/account/country/NaN.png','۲۲۹',1),(52,'بوتسوانا','images/account/country/NaN.png','+98',1),(53,'بورکینافاسو','images/account/country/NaN.png','+98',1),(54,'بروندی','images/account/country/NaN.png','+98',1),(55,'کیپ ورد','images/account/country/NaN.png','+98',1),(56,'کامرون','images/account/country/NaN.png','۲۳۷',1),(57,'جمهوری آفریقای مرکزی','images/account/country/NaN.png','+98',1),(58,'چاد','images/account/country/NaN.png','۲۳۷',1),(59,'مجمع‌الجزایر قمر','images/account/country/NaN.png','+98',1),(60,'جمهوری دموکراتیک کنگو','images/account/country/NaN.png','+98',1),(61,'جمهوری کنگو','images/account/country/NaN.png','+98',1),(62,'ساحل عاج','images/account/country/NaN.png','۲۲۵',1),(63,'جیبوتی','images/account/country/NaN.png','+98',1),(64,'مصر','images/account/country/NaN.png','۲۰',1),(65,'گینه استوایی','images/account/country/NaN.png','۲۴۰',1),(66,'اریتره','images/account/country/NaN.png','۲۹۱',1),(67,'اتیوپی','images/account/country/NaN.png','۲۵۱',1),(68,'گابن','images/account/country/NaN.png','+98',1),(69,'گامبیا','images/account/country/NaN.png','۲۲۰',1),(70,'غنا','images/account/country/NaN.png','۲۳۳',1),(71,'گینه','images/account/country/NaN.png','۲۲۴',1),(72,'گینه بیسائو','images/account/country/NaN.png','۲۴۵',1),(73,'کنیا','images/account/country/NaN.png','۲۵۴',1),(74,'لسوتو','images/account/country/NaN.png','۲۶۶',1),(75,'لیبریا','images/account/country/NaN.png','۲۳۱',1),(76,'لیبی','images/account/country/NaN.png','۲۱۸',1),(77,'ماداگاسکار','images/account/country/NaN.png','+98',1),(78,'مالاوی','images/account/country/NaN.png','۲۶۵',1),(79,'مالی','images/account/country/NaN.png','۲۲۳',1),(80,'موریتانی','images/account/country/NaN.png','۲۲۲',1),(81,'موریس','images/account/country/NaN.png','۲۳۰',1),(82,'مراکش','images/account/country/NaN.png','۲۱۲',1),(83,'موزامبیک','images/account/country/NaN.png','۲۵۸',1),(84,'نامیبیا','images/account/country/NaN.png','۲۶۴',1),(85,'نیجر','images/account/country/NaN.png','۲۲۷',1),(86,'نیجریه','images/account/country/NaN.png','+98',1),(87,'رواندا','images/account/country/NaN.png','+98',1),(88,'سائوتومه و پرینسیپ','images/account/country/NaN.png','+98',1),(89,'سنگال','images/account/country/NaN.png','۲۲۱',1),(90,'سیشل','images/account/country/NaN.png','۱۴۸',1),(91,'سیرالئون','images/account/country/NaN.png','+98',1),(92,'سومالی','images/account/country/NaN.png','۲۵۲',1),(93,'آفریقای جنوبی','images/account/country/NaN.png','۲۷',1),(94,'سودان جنوبی','images/account/country/NaN.png','+98',1),(95,'سوازیلند','images/account/country/NaN.png','+98',1),(96,'تانزانیا','images/account/country/NaN.png','۲۵۵',1),(97,'توگو','images/account/country/NaN.png','+98',1),(98,'تونس','images/account/country/NaN.png','۲۱۶',1),(99,'اوگاندا','images/account/country/NaN.png','۲۵',1),(100,'زامبیا','images/account/country/NaN.png','۲۶۰',1),(101,'زیمبابوه','images/account/country/NaN.png','۲۶۳',1),(102,'آلبانی','images/account/country/NaN.png','۳۵۵',1),(103,'آندورا','images/account/country/NaN.png','+98',1),(104,'اتریش','images/account/country/NaN.png','۴۳',1),(105,'بلاروس','images/account/country/NaN.png','۳۷۵',1),(106,'بلژیک','images/account/country/NaN.png','۳۲',1),(107,'بوسنی و هرزگوین','images/account/country/NaN.png','۳۸۷',1),(108,'بلغارستان','images/account/country/NaN.png','۳۵۹',1),(109,'کرواسی','images/account/country/NaN.png','۳۸۵',1),(110,'دانمارک','images/account/country/NaN.png','۴۵',1),(111,'استونی','images/account/country/NaN.png','۳۷۲',1),(112,'فنلاند','images/account/country/NaN.png','۳۵۸',1),(113,'فرانسه','images/account/country/NaN.png','۳۳',1),(114,'آلمان','images/account/country/NaN.png','۴۹',1),(115,'یونان','images/account/country/NaN.png','۳۰',1),(116,'مجارستان','images/account/country/NaN.png','۳۶',1),(117,'ایسلند','images/account/country/NaN.png','۳۵۴',1),(118,'ایتالیا','images/account/country/NaN.png','۳۹',1),(119,'کوزوو','images/account/country/NaN.png','+98',1),(120,'لتونی','images/account/country/NaN.png','+98',1),(121,'لیختن اشتاین','images/account/country/NaN.png','+98',1),(122,'لیتوانی','images/account/country/NaN.png','+98',1),(123,'لوکزامبورگ','images/account/country/NaN.png','۳۵۲',1),(124,'مقدونیه','images/account/country/NaN.png','۳۸۹',1),(125,'مالت','images/account/country/NaN.png','۳۵۶',1),(126,'مولداوی','images/account/country/NaN.png','+98',1),(127,'موناکو','images/account/country/NaN.png','+98',1),(128,'مونته نگرو','images/account/country/NaN.png','+98',1),(129,'هلند','images/account/country/NaN.png','۳۱',1),(130,'نروژ','images/account/country/NaN.png','۴۷',1),(131,'لهستان','images/account/country/NaN.png','۴۸',1),(132,'پرتغال','images/account/country/NaN.png','۳۵۱',1),(133,'رومانی','images/account/country/NaN.png','۴۰',1),(134,'سان مارینو','images/account/country/NaN.png','+98',1),(135,'صربستان','images/account/country/NaN.png','+98',1),(136,'اسلواکی','images/account/country/NaN.png','+98',1),(137,'اسوونی','images/account/country/NaN.png','+98',1),(138,'اسپانیا','images/account/country/NaN.png','۳۴',1),(139,'سوئد','images/account/country/NaN.png','۴۶',1),(140,'سوئیس','images/account/country/NaN.png','۴۱',1),(141,'اوکراین','images/account/country/NaN.png','۳۸۰',1),(142,'بریتانیا','images/account/country/NaN.png','+98',1),(143,'واتیکان','images/account/country/NaN.png','۳۹',1),(144,'آنتیگوا و باربودا','images/account/country/NaN.png','+98',1),(145,'باهاماس','images/account/country/NaN.png','+98',1),(146,'باربادوس','images/account/country/NaN.png','۱۸۰۹۴',1),(147,'بلیز','images/account/country/NaN.png','+98',1),(148,'کانادا','images/account/country/NaN.png','۱',1),(149,'کاستاریکا','images/account/country/NaN.png','۵۰۶',1),(150,'کوبا','images/account/country/NaN.png','۵۳',1),(151,'دومینیکا','images/account/country/NaN.png','۱۷۶۷',1),(152,'جمهوری دومینیکن','images/account/country/NaN.png','+98',1),(153,'السالوادور','images/account/country/NaN.png','۵۰۳',1),(154,'گرنادا','images/account/country/NaN.png','۱۴۷۳',1),(155,'گواتمالا','images/account/country/NaN.png','۵۰۲',1),(156,'هائیتی','images/account/country/NaN.png','+98',1),(157,'هندوراس','images/account/country/NaN.png','۵۰۴',1),(158,'جامائیکا','images/account/country/NaN.png','۱۸۰۹۹',1),(159,'مکزیک','images/account/country/NaN.png','۵۲',1),(160,'نیکاراگوئه','images/account/country/NaN.png','۵۰۵',1),(161,'پاناما','images/account/country/NaN.png','۵۰۷',1),(162,'سنت کیتس و نویس','images/account/country/NaN.png','+98',1),(163,'سنت لوسیا','images/account/country/NaN.png','۱۷۵۸',1),(164,'سنت وینسنت و گرنادینها','images/account/country/NaN.png','+98',1),(165,'ترینیداد و توباگو','images/account/country/NaN.png','+98',1),(166,'ایالات متحده امریکا','images/account/country/NaN.png','+98',1),(167,'آرژانتین','images/account/country/NaN.png','۵۴',1),(168,'بولیوی','images/account/country/NaN.png','۵۹۱',1),(169,'برزیل','images/account/country/NaN.png','۵۵',1),(170,'شیلی','images/account/country/NaN.png','۵۶',1),(171,'کلمبیا','images/account/country/NaN.png','۵۷',1),(172,'اکوادور','images/account/country/NaN.png','۵۹۳',1),(173,'گیانا','images/account/country/NaN.png','+98',1),(174,'پاراگوئه','images/account/country/NaN.png','۵۹۵',1),(175,'پرو','images/account/country/NaN.png','۵۱',1),(176,'سورینام','images/account/country/NaN.png','۵۹۷',1),(177,'اوروگوئه','images/account/country/NaN.png','+98',1),(178,'ونزوئلا','images/account/country/NaN.png','۵۸',1),(179,'استرالیا','images/account/country/NaN.png','+98',1),(180,'فیجی','images/account/country/NaN.png','۶۷۹',1),(181,'کیریباتی','images/account/country/NaN.png','+98',1),(182,'جزایر مارشال','images/account/country/NaN.png','+98',1),(183,'میکرونزی','images/account/country/NaN.png','+98',1),(184,'نائورو','images/account/country/NaN.png','+98',1),(185,'نیوزلند','images/account/country/NaN.png','+98',1),(186,'پالائو','images/account/country/NaN.png','+98',1),(187,'پاپوآ گینه نو','images/account/country/NaN.png','+98',1),(188,'ساموآ','images/account/country/NaN.png','+98',1),(189,'جزایر سلیمان','images/account/country/NaN.png','+98',1),(190,'تونگا','images/account/country/NaN.png','۶۷۶',1),(191,'تووالو','images/account/country/NaN.png','+98',1),(192,'وانواتو','images/account/country/NaN.png','+98',1),(193,'آفریقای مرکزی','images/account/country/NaN.png','۲۳۶',1),(194,'آمریکا','images/account/country/NaN.png','۱',1),(195,' ارمنستان','images/account/country/NaN.png','۳۷۴',1),(196,'اروگوئه','images/account/country/NaN.png','۵۹۸',1),(197,' استرالیا','images/account/country/NaN.png','۶۱',1),(198,'اطریش','images/account/country/NaN.png','۴۳',1),(199,' امارات','images/account/country/NaN.png','۹۷۱',1),(200,' انگلستان','images/account/country/NaN.png','۴۴',1),(201,'ایرلند','images/account/country/NaN.png','۳۵۳',1),(202,'باهاما','images/account/country/NaN.png','۱۸۰۹۳',1),(203,'بحرین','images/account/country/NaN.png','۹۷۳',1),(204,'بروئنی','images/account/country/NaN.png','۶۷۳',1),(205,'پنال','images/account/country/NaN.png','۹۵',1),(206,'ترینیداد','images/account/country/NaN.png','۱۸۶۸',1),(207,'جزایر قناری','images/account/country/NaN.png','۳۵۹',1),(208,'جزایرمارشال','images/account/country/NaN.png','۶۹۲',1),(209,'چک','images/account/country/NaN.png','۴۲',1),(210,'دومینیکن','images/account/country/NaN.png','۱۸۰۹ , ۱۸۲۹ , ۱۸۴۹',1),(211,'رو آندا','images/account/country/NaN.png','۲۵۰',1),(212,'زئیر','images/account/country/NaN.png','۲۴۳',1),(213,'زلاند نو','images/account/country/NaN.png','۶۴',1),(214,'ساموآ آمریکا','images/account/country/NaN.png','۶۸۴',1),(215,'ساموا غربی','images/account/country/NaN.png','۶۸۵',1),(216,'سنت وینسنت','images/account/country/NaN.png','۱۷۸۴',1),(217,'سنت کیتس','images/account/country/NaN.png','۱۸۶۹',1),(218,'سنگاپو','images/account/country/NaN.png','۶۵',1),(219,'سودان','images/account/country/NaN.png','۲۴۹',1),(220,'صربستان و مونته نگرو','images/account/country/NaN.png','۳۸۱',1),(221,'عربستان','images/account/country/NaN.png','۹۶۶',1),(222,'کنگو','images/account/country/NaN.png','۲۴۲',1),(223,'کومور','images/account/country/NaN.png','۲۶۹',1),(224,'گابون','images/account/country/NaN.png','۲۴۱',1),(225,'گوام','images/account/country/NaN.png','۶۷۱',1),(226,'میانمار','images/account/country/NaN.png','۹۵',1),(227,'نائورا','images/account/country/NaN.png','۶۷۴',1),(228,'نگارا پرونئی دارالسلام','images/account/country/NaN.png','۲۶۷',1),(229,'هائی تی','images/account/country/NaN.png','۵۰۹',1),(230,'هنگ کنگ','images/account/country/NaN.png','۷۵۲',1),(231,'یمن جنوبی','images/account/country/NaN.png','۹۶۹',1),(232,'یمن شمالی','images/account/country/NaN.png','۹۶۷',1),(233,'یوگسلاوی','images/account/country/NaN.png','۳۸۱',1);
/*!40000 ALTER TABLE `table_country` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-08-05 16:47:57
