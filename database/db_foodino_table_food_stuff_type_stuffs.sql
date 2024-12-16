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
-- Table structure for table `table_food_stuff_type_stuffs`
--

DROP TABLE IF EXISTS `table_food_stuff_type_stuffs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `table_food_stuff_type_stuffs` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `foodstufftype_id` bigint NOT NULL,
  `stuff_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `table_food_stuff_type_st_foodstufftype_id_stuff_i_47723474_uniq` (`foodstufftype_id`,`stuff_id`),
  KEY `table_food_stuff_type_stuffs_stuff_id_d35816fe_fk_table_stuff_id` (`stuff_id`),
  CONSTRAINT `table_food_stuff_typ_foodstufftype_id_e46a8b75_fk_table_foo` FOREIGN KEY (`foodstufftype_id`) REFERENCES `table_food_stuff_type` (`id`),
  CONSTRAINT `table_food_stuff_type_stuffs_stuff_id_d35816fe_fk_table_stuff_id` FOREIGN KEY (`stuff_id`) REFERENCES `table_stuff` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=76 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `table_food_stuff_type_stuffs`
--

LOCK TABLES `table_food_stuff_type_stuffs` WRITE;
/*!40000 ALTER TABLE `table_food_stuff_type_stuffs` DISABLE KEYS */;
INSERT INTO `table_food_stuff_type_stuffs` VALUES (4,1,8623),(7,1,8823),(8,1,8827),(9,1,8829),(10,1,8830),(1,1,8832),(2,1,8842),(3,1,8845),(5,1,8848),(6,1,8852),(16,2,8977),(18,2,8982),(14,2,8983),(11,2,8992),(17,2,9014),(12,2,9029),(13,2,9033),(15,2,9037),(19,3,8579),(20,3,8586),(21,3,8587),(22,3,8588),(23,3,8590),(24,3,8591),(25,3,8594),(26,3,8595),(27,3,8596),(28,3,8597),(29,3,8598),(30,3,8601),(31,3,8603),(32,3,8605),(33,3,8606),(34,3,8611),(35,3,8612),(36,3,8613),(37,3,8615),(38,3,8618),(39,3,8620),(40,3,8622),(41,3,8628),(42,3,8629),(43,3,8632),(44,3,8636),(45,3,8638),(46,3,8641),(47,3,8643),(48,3,8645),(49,3,8646),(50,3,8648),(51,3,8650),(52,3,8651),(53,3,8652),(54,3,8653),(55,3,8655),(56,3,8659),(57,3,8660),(58,3,8662),(59,3,8663),(60,3,8666),(61,3,8667),(62,3,8668),(63,3,8669),(64,3,8672),(65,3,8674),(66,3,8675),(67,3,8677),(68,3,8678),(69,3,8680),(70,3,8684),(71,3,8685),(72,3,8688),(73,3,8691),(74,3,8694),(75,3,8695);
/*!40000 ALTER TABLE `table_food_stuff_type_stuffs` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-08-05 16:47:58
