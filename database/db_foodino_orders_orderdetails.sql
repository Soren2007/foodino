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
-- Table structure for table `orders_orderdetails`
--

DROP TABLE IF EXISTS `orders_orderdetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orders_orderdetails` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `qty` bigint unsigned NOT NULL,
  `price` int NOT NULL,
  `how_to_use` varchar(120) NOT NULL,
  `food_id` bigint DEFAULT NULL,
  `my_recipes_id` bigint DEFAULT NULL,
  `order_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `orders_orderdetails_food_id_ec7e95d2_fk_table_food_id` (`food_id`),
  KEY `orders_orderdetails_my_recipes_id_f87986a1_fk_table_foo` (`my_recipes_id`),
  KEY `orders_orderdetails_order_id_d7985cfb_fk_orders_order_id` (`order_id`),
  CONSTRAINT `orders_orderdetails_food_id_ec7e95d2_fk_table_food_id` FOREIGN KEY (`food_id`) REFERENCES `table_food` (`id`),
  CONSTRAINT `orders_orderdetails_my_recipes_id_f87986a1_fk_table_foo` FOREIGN KEY (`my_recipes_id`) REFERENCES `table_food_my_recipes` (`id`),
  CONSTRAINT `orders_orderdetails_order_id_d7985cfb_fk_orders_order_id` FOREIGN KEY (`order_id`) REFERENCES `orders_order` (`id`),
  CONSTRAINT `orders_orderdetails_chk_1` CHECK ((`qty` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=67 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders_orderdetails`
--

LOCK TABLES `orders_orderdetails` WRITE;
/*!40000 ALTER TABLE `orders_orderdetails` DISABLE KEYS */;
INSERT INTO `orders_orderdetails` VALUES (58,2,344697,'1',9,NULL,39),(59,2,344697,'1',9,NULL,40),(60,2,344697,'1',9,NULL,41),(61,2,344697,'1',9,NULL,42),(62,1,208900,'2',10,NULL,43),(63,1,344697,'1',9,NULL,43),(64,2,344697,'1',9,NULL,44),(65,2,344697,'1',9,NULL,45),(66,2,344697,'1',9,NULL,46);
/*!40000 ALTER TABLE `orders_orderdetails` ENABLE KEYS */;
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
