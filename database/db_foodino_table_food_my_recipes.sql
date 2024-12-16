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
-- Table structure for table `table_food_my_recipes`
--

DROP TABLE IF EXISTS `table_food_my_recipes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `table_food_my_recipes` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `recipes_name` varchar(160) NOT NULL,
  `recipes_price` int unsigned NOT NULL,
  `recipes_register_date` date NOT NULL,
  `recipes_food_id` bigint NOT NULL,
  `recipes_user_id` bigint NOT NULL,
  `is_translated_content` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `table_food_my_recipes_recipes_food_id_4d951617_fk_table_food_id` (`recipes_food_id`),
  KEY `table_food_my_recipe_recipes_user_id_e1ce8f9b_fk_table_cus` (`recipes_user_id`),
  CONSTRAINT `table_food_my_recipe_recipes_user_id_e1ce8f9b_fk_table_cus` FOREIGN KEY (`recipes_user_id`) REFERENCES `table_custom_user` (`id`),
  CONSTRAINT `table_food_my_recipes_recipes_food_id_4d951617_fk_table_food_id` FOREIGN KEY (`recipes_food_id`) REFERENCES `table_food` (`id`),
  CONSTRAINT `table_food_my_recipes_chk_1` CHECK ((`recipes_price` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `table_food_my_recipes`
--

LOCK TABLES `table_food_my_recipes` WRITE;
/*!40000 ALTER TABLE `table_food_my_recipes` DISABLE KEYS */;
INSERT INTO `table_food_my_recipes` VALUES (1,'دستور غذایی من',1375900,'2023-07-28',11,1,0),(2,'دستور من',752070,'2023-07-31',11,1,0),(3,'test',126750,'2023-08-05',9,1,0),(4,'قرمه سبزی',23,'2023-08-05',11,2,1);
/*!40000 ALTER TABLE `table_food_my_recipes` ENABLE KEYS */;
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
