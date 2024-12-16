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
-- Table structure for table `table_food_food_stuff_types`
--

DROP TABLE IF EXISTS `table_food_food_stuff_types`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `table_food_food_stuff_types` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `food_id` bigint NOT NULL,
  `foodstufftype_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `table_food_food_stuff_ty_food_id_foodstufftype_id_8a4aa6a8_uniq` (`food_id`,`foodstufftype_id`),
  KEY `table_food_food_stuf_foodstufftype_id_e7c4d674_fk_table_foo` (`foodstufftype_id`),
  CONSTRAINT `table_food_food_stuf_foodstufftype_id_e7c4d674_fk_table_foo` FOREIGN KEY (`foodstufftype_id`) REFERENCES `table_food_stuff_type` (`id`),
  CONSTRAINT `table_food_food_stuff_types_food_id_f872d9a7_fk_table_food_id` FOREIGN KEY (`food_id`) REFERENCES `table_food` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `table_food_food_stuff_types`
--

LOCK TABLES `table_food_food_stuff_types` WRITE;
/*!40000 ALTER TABLE `table_food_food_stuff_types` DISABLE KEYS */;
INSERT INTO `table_food_food_stuff_types` VALUES (1,9,1),(2,9,2),(3,10,1),(4,10,2),(5,11,3);
/*!40000 ALTER TABLE `table_food_food_stuff_types` ENABLE KEYS */;
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
