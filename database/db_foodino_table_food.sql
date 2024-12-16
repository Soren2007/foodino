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
-- Table structure for table `table_food`
--

DROP TABLE IF EXISTS `table_food`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `table_food` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `food_name` varchar(60) NOT NULL,
  `food_slug` varchar(120) NOT NULL,
  `food_image` varchar(100) NOT NULL,
  `food_price` int NOT NULL,
  `food_time` varchar(3) NOT NULL,
  `food_wight` varchar(10) NOT NULL,
  `food_calories` varchar(10) NOT NULL,
  `food_description` longtext NOT NULL,
  `food_is_active` tinyint(1) NOT NULL,
  `register_date` datetime(6) NOT NULL,
  `food_sales_number` int unsigned NOT NULL,
  `food_views` int unsigned NOT NULL,
  `profit` int unsigned NOT NULL,
  `is_auto_compile_price` tinyint(1) NOT NULL,
  `food_group_id` bigint NOT NULL,
  `food_recipes_id` bigint NOT NULL,
  `is_translated_content` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `table_food_food_group_id_50656dab_fk_table_food_group_id` (`food_group_id`),
  KEY `table_food_food_recipes_id_ceced91f_fk_table_food_recipes_id` (`food_recipes_id`),
  KEY `table_food_food_slug_5bf191b1` (`food_slug`),
  CONSTRAINT `table_food_food_group_id_50656dab_fk_table_food_group_id` FOREIGN KEY (`food_group_id`) REFERENCES `table_food_group` (`id`),
  CONSTRAINT `table_food_food_recipes_id_ceced91f_fk_table_food_recipes_id` FOREIGN KEY (`food_recipes_id`) REFERENCES `table_food_recipes` (`id`),
  CONSTRAINT `table_food_chk_1` CHECK ((`food_sales_number` >= 0)),
  CONSTRAINT `table_food_chk_2` CHECK ((`food_views` >= 0)),
  CONSTRAINT `table_food_chk_3` CHECK ((`profit` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `table_food`
--

LOCK TABLES `table_food` WRITE;
/*!40000 ALTER TABLE `table_food` DISABLE KEYS */;
INSERT INTO `table_food` VALUES (9,'پیتزا مخلوط','mix-pizza','images/food/food/pitza-makhlout.jpg',344697,'25','1000','1400','پیتزا مخلوط به عنوان محبوب ترین پیتزا در سراسر جهان شناخته می شود که با مواد بسیار متنوعی طبخ می شود',1,'2023-07-28 10:02:56.355004',0,11,25000,1,1,2,1),(10,'پیتزا قارچ و گوشت','biscuit-dessert','images/food/food/pitza-gharch-goosht.jpg',208900,'25','1000','1400','یتزا قارچ و گوشت یکی از انواع پیتزاهای خوشمزه بین المللی است که با مواد متنوعی تهیه می شود',1,'2023-07-28 10:19:26.508783',0,6,25000,1,1,3,1),(11,'شیر برنج','rice-milk','images/food/food/shir-berenj.jpg',100000,'25','1000','1000','شیر برنج یکی از دسرهای سنتی و خوشمزه ایرانی است که امروزه بیشتر به عنوان یک غذای کامل سرو می شود. شیر برنج را به سلیقه خود می توانید به صورت ساده یا مجلسی درست کنیم، برای مجلسی تر شدن شیر برنج می توانیم در تهیه آن از خامه صبحانه و پودر مغزیجات استفاده کنیم،',1,'2023-07-28 10:41:41.985302',23,16,20000,0,2,4,1);
/*!40000 ALTER TABLE `table_food` ENABLE KEYS */;
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
