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
-- Table structure for table `table_robot_takes_containers`
--

DROP TABLE IF EXISTS `table_robot_takes_containers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `table_robot_takes_containers` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `model` varchar(150) NOT NULL,
  `google_map_location_link` longtext,
  `city_location_id` bigint NOT NULL,
  `country_location_id` bigint NOT NULL,
  `state_location_id` bigint NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `table_robot_takes_co_city_location_id_6c047657_fk_table_cit` (`city_location_id`),
  KEY `table_robot_takes_co_country_location_id_81bc7229_fk_table_cou` (`country_location_id`),
  KEY `table_robot_takes_co_state_location_id_83354714_fk_table_sta` (`state_location_id`),
  CONSTRAINT `table_robot_takes_co_city_location_id_6c047657_fk_table_cit` FOREIGN KEY (`city_location_id`) REFERENCES `table_city` (`id`),
  CONSTRAINT `table_robot_takes_co_country_location_id_81bc7229_fk_table_cou` FOREIGN KEY (`country_location_id`) REFERENCES `table_country` (`id`),
  CONSTRAINT `table_robot_takes_co_state_location_id_83354714_fk_table_sta` FOREIGN KEY (`state_location_id`) REFERENCES `table_state` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `table_robot_takes_containers`
--

LOCK TABLES `table_robot_takes_containers` WRITE;
/*!40000 ALTER TABLE `table_robot_takes_containers` DISABLE KEYS */;
INSERT INTO `table_robot_takes_containers` VALUES (1,'mxs-2334-4','https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4075.8204852721724!2d50.55821621449997!3d35.82495070283052!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3f8d044b7d68a23d%3A0x32c317247ca6f4c1!2z2LPZh9uM2YTbjNmHIC0g2KfZhNio2LHYsiwgS291cm9zaCwgQWxib3J6IFByb3ZpbmNlLCBJcmFu!5e0!3m2!1sen!2sus!4v1691154390413!5m2!1sen!2sus',936,6,2,1),(2,'asde-ws-1234','https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d606.6110221228864!2d51.513495619096254!3d35.728299374055965!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3f8e1d1cf6cc935f%3A0x81ba6cee9aff39eb!2sTehranpars%2C%20District%208%2C%20Tehran%2C%20Tehran%20Province%2C%20Iran!5e0!3m2!1sen!2sus!4v1691155718310!5m2!1sen!2sus',2607,6,3,1);
/*!40000 ALTER TABLE `table_robot_takes_containers` ENABLE KEYS */;
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
