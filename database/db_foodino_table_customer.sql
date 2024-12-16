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
-- Table structure for table `table_customer`
--

DROP TABLE IF EXISTS `table_customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `table_customer` (
  `user_id` bigint NOT NULL,
  `phone_number` varchar(11) DEFAULT NULL,
  `address` longtext,
  `city_id` bigint DEFAULT NULL,
  `country_id` bigint DEFAULT NULL,
  `state_id` bigint DEFAULT NULL,
  `latitude_location` varchar(15) DEFAULT NULL,
  `longitude_location` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`user_id`),
  KEY `table_customer_city_id_8d627d54_fk_table_city_id` (`city_id`),
  KEY `table_customer_country_id_f7c81956_fk_table_country_id` (`country_id`),
  KEY `table_customer_state_id_70d8633f_fk_table_state_id` (`state_id`),
  CONSTRAINT `table_customer_city_id_8d627d54_fk_table_city_id` FOREIGN KEY (`city_id`) REFERENCES `table_city` (`id`),
  CONSTRAINT `table_customer_country_id_f7c81956_fk_table_country_id` FOREIGN KEY (`country_id`) REFERENCES `table_country` (`id`),
  CONSTRAINT `table_customer_state_id_70d8633f_fk_table_state_id` FOREIGN KEY (`state_id`) REFERENCES `table_state` (`id`),
  CONSTRAINT `table_customer_user_id_d7943128_fk_table_custom_user_id` FOREIGN KEY (`user_id`) REFERENCES `table_custom_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `table_customer`
--

LOCK TABLES `table_customer` WRITE;
/*!40000 ALTER TABLE `table_customer` DISABLE KEYS */;
INSERT INTO `table_customer` VALUES (1,'09932062665','کرج،  شهرک وحدت، خیابان ششم شرقی، گذر اول، پلاک 102،واحد ۱',936,6,1,NULL,NULL),(2,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `table_customer` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-08-05 16:47:49
