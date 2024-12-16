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
-- Table structure for table `table_slids`
--

DROP TABLE IF EXISTS `table_slids`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `table_slids` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `slid_title` varchar(100) NOT NULL,
  `slid_color` varchar(18) NOT NULL,
  `slid_url` varchar(255) NOT NULL,
  `slid_image` varchar(100) DEFAULT NULL,
  `slid_video` varchar(100) DEFAULT NULL,
  `slid_type` varchar(100) NOT NULL,
  `slid_start_date_time` datetime(6) NOT NULL,
  `slid_end_date_time` datetime(6) NOT NULL,
  `slid_register_date` datetime(6) NOT NULL,
  `slid_is_active` tinyint(1) NOT NULL,
  `is_translated_content` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `table_slids`
--

LOCK TABLES `table_slids` WRITE;
/*!40000 ALTER TABLE `table_slids` DISABLE KEYS */;
INSERT INTO `table_slids` VALUES (1,'فودینو را در اینستاگرام دنبال کنید.','#FFFFFFFF','https://sorenshamlou.ir','images/main/slider/imgfa_ir__5ff1d33f75fdc_1.jpg','','2','2023-07-27 13:26:57.000000','2023-08-31 14:26:49.000000','2023-07-27 14:20:54.654460',1,1),(2,'فودینو بهترین تارنما برای شما','#FFFFFFFF','https://sorenshamlou.ir','images/main/slider/Junk-Food-More-Harm-and-Lesser-Well-being.jpeg','','2','2023-07-27 15:24:31.000000','2023-08-31 16:25:00.000000','2023-07-27 16:25:07.882108',1,1);
/*!40000 ALTER TABLE `table_slids` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-08-05 16:47:47
