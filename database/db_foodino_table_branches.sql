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
-- Table structure for table `table_branches`
--

DROP TABLE IF EXISTS `table_branches`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `table_branches` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `branch_name` varchar(180) NOT NULL,
  `branch_number` int NOT NULL,
  `branch_capacity` int NOT NULL,
  `branch_number_of_tables` int NOT NULL,
  `branch_address` longtext NOT NULL,
  `branch_google_map_link` varchar(200) DEFAULT NULL,
  `branch_3d_map_link` varchar(200) DEFAULT NULL,
  `is_active` tinyint(1) NOT NULL,
  `branch_city_id` bigint NOT NULL,
  `branch_country_id` bigint NOT NULL,
  `branch_manager_id` bigint NOT NULL,
  `branch_state_id` bigint NOT NULL,
  `is_translated_content` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `table_branches_branch_city_id_5116d930_fk_table_city_id` (`branch_city_id`),
  KEY `table_branches_branch_country_id_fa39c3ce_fk_table_country_id` (`branch_country_id`),
  KEY `table_branches_branch_manager_id_15664887_fk_table_cus` (`branch_manager_id`),
  KEY `table_branches_branch_state_id_6d91bf53_fk_table_state_id` (`branch_state_id`),
  CONSTRAINT `table_branches_branch_city_id_5116d930_fk_table_city_id` FOREIGN KEY (`branch_city_id`) REFERENCES `table_city` (`id`),
  CONSTRAINT `table_branches_branch_country_id_fa39c3ce_fk_table_country_id` FOREIGN KEY (`branch_country_id`) REFERENCES `table_country` (`id`),
  CONSTRAINT `table_branches_branch_manager_id_15664887_fk_table_cus` FOREIGN KEY (`branch_manager_id`) REFERENCES `table_custom_user` (`id`),
  CONSTRAINT `table_branches_branch_state_id_6d91bf53_fk_table_state_id` FOREIGN KEY (`branch_state_id`) REFERENCES `table_state` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `table_branches`
--

LOCK TABLES `table_branches` WRITE;
/*!40000 ALTER TABLE `table_branches` DISABLE KEYS */;
INSERT INTO `table_branches` VALUES (1,'فودینو',23,112,29,'کرج','https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2880.8811751787443!2d50.96680102038257!3d35.85684374159258!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3f8dbf95ef45f011%3A0x722a04e54eba9b','https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2880.8811751787443!2d50.96680102038257!3d35.85684374159258!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3f8dbf95ef45f011%3A0x722a04e54eba9b',1,936,6,1,2,1);
/*!40000 ALTER TABLE `table_branches` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-08-05 16:47:48
