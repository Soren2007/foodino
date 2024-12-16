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
-- Table structure for table `comments_comment`
--

DROP TABLE IF EXISTS `comments_comment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `comments_comment` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `comment_text` longtext NOT NULL,
  `register_date` datetime(6) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `approving_user_id` bigint DEFAULT NULL,
  `blog_id` bigint DEFAULT NULL,
  `comment_parent_id` bigint DEFAULT NULL,
  `commenting_user_id` bigint NOT NULL,
  `food_id` bigint DEFAULT NULL,
  `recipes_id` bigint DEFAULT NULL,
  `is_translated_content` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `comments_comment_approving_user_id_691e0694_fk_table_cus` (`approving_user_id`),
  KEY `comments_comment_blog_id_7b898599_fk_table_articles_id` (`blog_id`),
  KEY `comments_comment_comment_parent_id_f00e92d5_fk_comments_` (`comment_parent_id`),
  KEY `comments_comment_commenting_user_id_6af91ff3_fk_table_cus` (`commenting_user_id`),
  KEY `comments_comment_food_id_ee16bab6_fk_table_food_id` (`food_id`),
  KEY `comments_comment_recipes_id_5795ba47_fk_table_food_recipes_id` (`recipes_id`),
  CONSTRAINT `comments_comment_approving_user_id_691e0694_fk_table_cus` FOREIGN KEY (`approving_user_id`) REFERENCES `table_custom_user` (`id`),
  CONSTRAINT `comments_comment_blog_id_7b898599_fk_table_articles_id` FOREIGN KEY (`blog_id`) REFERENCES `table_articles` (`id`),
  CONSTRAINT `comments_comment_comment_parent_id_f00e92d5_fk_comments_` FOREIGN KEY (`comment_parent_id`) REFERENCES `comments_comment` (`id`),
  CONSTRAINT `comments_comment_commenting_user_id_6af91ff3_fk_table_cus` FOREIGN KEY (`commenting_user_id`) REFERENCES `table_custom_user` (`id`),
  CONSTRAINT `comments_comment_food_id_ee16bab6_fk_table_food_id` FOREIGN KEY (`food_id`) REFERENCES `table_food` (`id`),
  CONSTRAINT `comments_comment_recipes_id_5795ba47_fk_table_food_recipes_id` FOREIGN KEY (`recipes_id`) REFERENCES `table_food_recipes` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comments_comment`
--

LOCK TABLES `comments_comment` WRITE;
/*!40000 ALTER TABLE `comments_comment` DISABLE KEYS */;
INSERT INTO `comments_comment` VALUES (1,'بسیار عالی.','2023-07-28 10:09:01.911275',1,NULL,NULL,NULL,1,NULL,2,1),(2,'سلام.','2023-08-02 17:05:01.266141',1,NULL,NULL,NULL,1,11,NULL,1),(3,'وقتتون بخیر','2023-08-02 17:06:08.035752',1,NULL,NULL,2,1,11,NULL,1);
/*!40000 ALTER TABLE `comments_comment` ENABLE KEYS */;
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
