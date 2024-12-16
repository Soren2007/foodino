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
-- Table structure for table `table_mukbangs`
--

DROP TABLE IF EXISTS `table_mukbangs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `table_mukbangs` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `like` bigint unsigned NOT NULL,
  `dislike` bigint unsigned NOT NULL,
  `views` bigint unsigned NOT NULL,
  `share_number` bigint unsigned NOT NULL,
  `video` varchar(100) NOT NULL,
  `poster_image` varchar(100) NOT NULL,
  `description` longtext NOT NULL,
  `register_date` date NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `user_id` bigint NOT NULL,
  `is_translated_content` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `table_mukbangs_user_id_56ac351b_fk_table_custom_user_id` (`user_id`),
  CONSTRAINT `table_mukbangs_user_id_56ac351b_fk_table_custom_user_id` FOREIGN KEY (`user_id`) REFERENCES `table_custom_user` (`id`),
  CONSTRAINT `table_mukbangs_chk_1` CHECK ((`like` >= 0)),
  CONSTRAINT `table_mukbangs_chk_2` CHECK ((`dislike` >= 0)),
  CONSTRAINT `table_mukbangs_chk_3` CHECK ((`views` >= 0)),
  CONSTRAINT `table_mukbangs_chk_4` CHECK ((`share_number` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `table_mukbangs`
--

LOCK TABLES `table_mukbangs` WRITE;
/*!40000 ALTER TABLE `table_mukbangs` DISABLE KEYS */;
INSERT INTO `table_mukbangs` VALUES (1,0,0,0,0,'videos/Mukbang/videos/c74f6f03433babbad5b8eefeaa2ce6aa14951066-720p.mp4','images/Mukbang/poster_image/download_1.jpeg','تست','2023-08-05',0,1,1);
/*!40000 ALTER TABLE `table_mukbangs` ENABLE KEYS */;
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
