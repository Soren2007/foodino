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
-- Table structure for table `table_food_my_recipes_recipes_stuffs`
--

DROP TABLE IF EXISTS `table_food_my_recipes_recipes_stuffs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `table_food_my_recipes_recipes_stuffs` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `myrecipes_id` bigint NOT NULL,
  `stuff_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `table_food_my_recipes_re_myrecipes_id_stuff_id_f76ff7b6_uniq` (`myrecipes_id`,`stuff_id`),
  KEY `table_food_my_recipe_stuff_id_ab1fed9e_fk_table_stu` (`stuff_id`),
  CONSTRAINT `table_food_my_recipe_myrecipes_id_208876ba_fk_table_foo` FOREIGN KEY (`myrecipes_id`) REFERENCES `table_food_my_recipes` (`id`),
  CONSTRAINT `table_food_my_recipe_stuff_id_ab1fed9e_fk_table_stu` FOREIGN KEY (`stuff_id`) REFERENCES `table_stuff` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `table_food_my_recipes_recipes_stuffs`
--

LOCK TABLES `table_food_my_recipes_recipes_stuffs` WRITE;
/*!40000 ALTER TABLE `table_food_my_recipes_recipes_stuffs` DISABLE KEYS */;
INSERT INTO `table_food_my_recipes_recipes_stuffs` VALUES (7,1,8579),(6,1,8586),(8,1,8587),(2,1,8612),(3,1,8645),(4,1,8663),(5,1,8669),(1,1,8675),(9,4,8349),(10,4,8351);
/*!40000 ALTER TABLE `table_food_my_recipes_recipes_stuffs` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-08-05 16:47:57
