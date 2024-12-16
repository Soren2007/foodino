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
-- Table structure for table `table_my_environment`
--

DROP TABLE IF EXISTS `table_my_environment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `table_my_environment` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `number_dishes` int unsigned NOT NULL,
  `points_unit` int unsigned NOT NULL,
  `robot_takes_id` bigint NOT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `table_my_environment_robot_takes_id_485832c3_fk_table_rob` (`robot_takes_id`),
  KEY `table_my_environment_user_id_7c6f0ddd_fk_table_custom_user_id` (`user_id`),
  CONSTRAINT `table_my_environment_robot_takes_id_485832c3_fk_table_rob` FOREIGN KEY (`robot_takes_id`) REFERENCES `table_robot_takes_containers` (`id`),
  CONSTRAINT `table_my_environment_user_id_7c6f0ddd_fk_table_custom_user_id` FOREIGN KEY (`user_id`) REFERENCES `table_custom_user` (`id`),
  CONSTRAINT `table_my_environment_chk_1` CHECK ((`number_dishes` >= 0)),
  CONSTRAINT `table_my_environment_chk_2` CHECK ((`points_unit` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `table_my_environment`
--

LOCK TABLES `table_my_environment` WRITE;
/*!40000 ALTER TABLE `table_my_environment` DISABLE KEYS */;
/*!40000 ALTER TABLE `table_my_environment` ENABLE KEYS */;
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
