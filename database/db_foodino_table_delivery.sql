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
-- Table structure for table `table_delivery`
--

DROP TABLE IF EXISTS `table_delivery`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `table_delivery` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `plaque` varchar(10) NOT NULL,
  `chassis_number` varchar(32) NOT NULL,
  `profile_form` varchar(100) NOT NULL,
  `ID_card_image` varchar(100) NOT NULL,
  `register_date` datetime(6) NOT NULL,
  `is_sending_the_order` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_translated_content` tinyint(1) NOT NULL,
  `vehicle_type_id` bigint NOT NULL,
  `user_id` bigint NOT NULL,
  `is_accepted` tinyint(1) NOT NULL,
  `branch_id` bigint DEFAULT NULL,
  `your_last_activity` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `VehicleType_id` (`vehicle_type_id`),
  KEY `table_delivery_user_id_f1a58274_fk_table_custom_user_id` (`user_id`),
  KEY `table_delivery_branch_id_0e3d02e7_fk_table_branches_id` (`branch_id`),
  CONSTRAINT `table_delivery_branch_id_0e3d02e7_fk_table_branches_id` FOREIGN KEY (`branch_id`) REFERENCES `table_branches` (`id`),
  CONSTRAINT `table_delivery_user_id_f1a58274_fk_table_custom_user_id` FOREIGN KEY (`user_id`) REFERENCES `table_custom_user` (`id`),
  CONSTRAINT `table_delivery_vehicle_type_id_1990cd26_fk_table_vehicle_type_id` FOREIGN KEY (`vehicle_type_id`) REFERENCES `table_vehicle_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `table_delivery`
--

LOCK TABLES `table_delivery` WRITE;
/*!40000 ALTER TABLE `table_delivery` DISABLE KEYS */;
INSERT INTO `table_delivery` VALUES (1,'223345','1233124235','files/delivery/profile_form/53نمونه_سوال_دوره_آشنایی_با_اندیشه_و_سیره_امام_خمینی_ره_استان_بوشهر.pdf','images/delivery/ID_card_image/IMG_8884.JPG','2023-08-04 14:18:41.889217',0,1,0,2,1,1,1,'2023-08-04 14:18:41.889217');
/*!40000 ALTER TABLE `table_delivery` ENABLE KEYS */;
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
