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
-- Table structure for table `table_custom_user`
--

DROP TABLE IF EXISTS `table_custom_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `table_custom_user` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `mobile_number` varchar(11) DEFAULT NULL,
  `username` varchar(20) DEFAULT NULL,
  `name` varchar(50) NOT NULL,
  `family` varchar(50) NOT NULL,
  `profile` varchar(100) DEFAULT NULL,
  `email` varchar(200) NOT NULL,
  `gender` varchar(50) DEFAULT NULL,
  `address` longtext NOT NULL,
  `birth_date` date DEFAULT NULL,
  `score` int NOT NULL,
  `national_code` varchar(11) DEFAULT NULL,
  `postal_code` varchar(10) DEFAULT NULL,
  `register_date` date NOT NULL,
  `is_complete_information` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `active_code` varchar(100) DEFAULT NULL,
  `is_admin` tinyint(1) NOT NULL,
  `is_support` tinyint(1) NOT NULL,
  `is_serviceman` tinyint(1) NOT NULL,
  `country_id` bigint DEFAULT NULL,
  `is_translated_content` tinyint(1) NOT NULL,
  `current_order` int unsigned NOT NULL,
  `delivered_order` int unsigned NOT NULL,
  `returned_order` int unsigned NOT NULL,
  `is_delivery` tinyint(1) NOT NULL,
  `city_id` bigint DEFAULT NULL,
  `state_id` bigint DEFAULT NULL,
  `latitude_location` varchar(15) DEFAULT NULL,
  `longitude_location` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `mobile_number` (`mobile_number`),
  UNIQUE KEY `username` (`username`),
  KEY `table_custom_user_country_id_4c307a4a_fk_table_country_id` (`country_id`),
  KEY `table_custom_user_city_id_88ca2371_fk_table_city_id` (`city_id`),
  KEY `table_custom_user_state_id_6ed94350_fk_table_state_id` (`state_id`),
  CONSTRAINT `table_custom_user_city_id_88ca2371_fk_table_city_id` FOREIGN KEY (`city_id`) REFERENCES `table_city` (`id`),
  CONSTRAINT `table_custom_user_country_id_4c307a4a_fk_table_country_id` FOREIGN KEY (`country_id`) REFERENCES `table_country` (`id`),
  CONSTRAINT `table_custom_user_state_id_6ed94350_fk_table_state_id` FOREIGN KEY (`state_id`) REFERENCES `table_state` (`id`),
  CONSTRAINT `table_custom_user_chk_1` CHECK ((`current_order` >= 0)),
  CONSTRAINT `table_custom_user_chk_2` CHECK ((`delivered_order` >= 0)),
  CONSTRAINT `table_custom_user_chk_3` CHECK ((`returned_order` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `table_custom_user`
--

LOCK TABLES `table_custom_user` WRITE;
/*!40000 ALTER TABLE `table_custom_user` DISABLE KEYS */;
INSERT INTO `table_custom_user` VALUES (1,'pbkdf2_sha256$320000$ba3Csp2YwWSlfWVl6a6CNV$zR3Z7yT689nd+a0yDb8CGzQRTm9Fi5z7iPbl4oQW0X4=','2023-08-05 07:09:19.747195',1,'09932062665',NULL,'سورن','شاملو','images/account/profile/IMG_8884.JPG','SorenShamloo.Programmer@gmail.com','False','کرج،  شهرک وحدت، خیابان ششم شرقی، گذر اول، پلاک 102،واحد ۱','2023-09-08',20,'None','None','2023-07-25',1,1,NULL,1,1,1,6,1,0,0,0,1,2604,1,'35.754871','51.0148549'),(2,'pbkdf2_sha256$320000$pO105VXNizE98HRP8x12u0$pdQ3Q6p2mRI1kswF+/cSH5iVFWMHmJJfm0kLLdcsSME=','2023-08-05 07:15:48.511219',0,'09127664810',NULL,'علی','محمدی','images/account/profile/NaN.png','SorenShamloo.Programmer@gmail.com','True','کرج،  شهرک وحدت، بلوار شهیدان بخشی، خیابان بوستان شرقی، مجتمع سرو','2023-08-05',20,'4901718452',NULL,'2023-08-05',0,1,'32042',0,0,0,6,1,0,0,0,0,936,2,NULL,NULL);
/*!40000 ALTER TABLE `table_custom_user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-08-05 16:47:51
