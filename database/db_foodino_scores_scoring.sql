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
-- Table structure for table `scores_scoring`
--

DROP TABLE IF EXISTS `scores_scoring`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `scores_scoring` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `register_date` datetime(6) NOT NULL,
  `score` smallint unsigned NOT NULL,
  `food_id` bigint NOT NULL,
  `scoring_user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `scores_scoring_food_id_b46d6a35_fk_table_food_id` (`food_id`),
  KEY `scores_scoring_scoring_user_id_654b656e_fk_table_custom_user_id` (`scoring_user_id`),
  CONSTRAINT `scores_scoring_food_id_b46d6a35_fk_table_food_id` FOREIGN KEY (`food_id`) REFERENCES `table_food` (`id`),
  CONSTRAINT `scores_scoring_scoring_user_id_654b656e_fk_table_custom_user_id` FOREIGN KEY (`scoring_user_id`) REFERENCES `table_custom_user` (`id`),
  CONSTRAINT `scores_scoring_chk_1` CHECK ((`score` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `scores_scoring`
--

LOCK TABLES `scores_scoring` WRITE;
/*!40000 ALTER TABLE `scores_scoring` DISABLE KEYS */;
/*!40000 ALTER TABLE `scores_scoring` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-08-05 16:47:50
