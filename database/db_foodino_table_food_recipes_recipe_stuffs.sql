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
-- Table structure for table `table_food_recipes_recipe_stuffs`
--

DROP TABLE IF EXISTS `table_food_recipes_recipe_stuffs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `table_food_recipes_recipe_stuffs` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `recipes_id` bigint NOT NULL,
  `stuff_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `table_food_recipes_recip_recipes_id_stuff_id_b7f5c4c2_uniq` (`recipes_id`,`stuff_id`),
  KEY `table_food_recipes_r_stuff_id_179beac1_fk_table_stu` (`stuff_id`),
  CONSTRAINT `table_food_recipes_r_recipes_id_2625154b_fk_table_foo` FOREIGN KEY (`recipes_id`) REFERENCES `table_food_recipes` (`id`),
  CONSTRAINT `table_food_recipes_r_stuff_id_179beac1_fk_table_stu` FOREIGN KEY (`stuff_id`) REFERENCES `table_stuff` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `table_food_recipes_recipe_stuffs`
--

LOCK TABLES `table_food_recipes_recipe_stuffs` WRITE;
/*!40000 ALTER TABLE `table_food_recipes_recipe_stuffs` DISABLE KEYS */;
INSERT INTO `table_food_recipes_recipe_stuffs` VALUES (10,2,8358),(9,2,8614),(12,2,8623),(7,2,8832),(15,2,9021),(11,2,9037),(13,2,10101),(18,3,8358),(19,3,8360),(17,3,8832),(20,3,9039),(16,3,9312),(21,3,10101),(23,4,8519),(24,4,8588),(25,4,8818),(22,4,8896),(26,4,9755);
/*!40000 ALTER TABLE `table_food_recipes_recipe_stuffs` ENABLE KEYS */;
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
