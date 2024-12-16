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
-- Table structure for table `table_chat_room`
--

DROP TABLE IF EXISTS `table_chat_room`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `table_chat_room` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `message_text` longtext NOT NULL,
  `register_date` datetime(6) NOT NULL,
  `is_seen` tinyint(1) NOT NULL,
  `message_parent_id` bigint DEFAULT NULL,
  `receiver_user_id` varchar(11) DEFAULT NULL,
  `sender_user_id` varchar(11) NOT NULL,
  `is_translated_content` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `table_chat_room_message_parent_id_c8724239_fk_table_chat_room_id` (`message_parent_id`),
  KEY `table_chat_room_receiver_user_id_79e1b4da_fk_table_use` (`receiver_user_id`),
  KEY `table_chat_room_sender_user_id_3798f64e_fk_table_use` (`sender_user_id`),
  CONSTRAINT `table_chat_room_message_parent_id_c8724239_fk_table_chat_room_id` FOREIGN KEY (`message_parent_id`) REFERENCES `table_chat_room` (`id`),
  CONSTRAINT `table_chat_room_receiver_user_id_79e1b4da_fk_table_use` FOREIGN KEY (`receiver_user_id`) REFERENCES `table_user_chat_room` (`phone_number`),
  CONSTRAINT `table_chat_room_sender_user_id_3798f64e_fk_table_use` FOREIGN KEY (`sender_user_id`) REFERENCES `table_user_chat_room` (`phone_number`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `table_chat_room`
--

LOCK TABLES `table_chat_room` WRITE;
/*!40000 ALTER TABLE `table_chat_room` DISABLE KEYS */;
INSERT INTO `table_chat_room` VALUES (14,'سلام','2023-08-02 18:19:11.517158',0,NULL,NULL,'09932062665',1),(15,'sghl','2023-08-02 18:19:33.702745',0,NULL,NULL,'09932062665',1),(16,'سلام','2023-08-02 18:35:03.506438',0,NULL,NULL,'09932062665',1),(17,'sd','2023-08-02 19:16:03.838131',0,NULL,NULL,'09932062665',1),(18,'sd','2023-08-02 19:16:09.490260',0,NULL,NULL,'09932062665',1),(19,'asd','2023-08-02 19:17:23.475094',0,NULL,NULL,'09932062665',1),(20,'asd','2023-08-02 19:17:30.773005',0,NULL,NULL,'09932062665',1),(21,'تست','2023-08-05 07:24:32.419052',0,NULL,NULL,'09123608173',1),(22,'سلام','2023-08-05 07:25:40.119439',0,21,'09123608173','09932062665',1),(23,'.','2023-08-05 07:26:23.700448',0,NULL,NULL,'09123608173',1),(24,'.','2023-08-05 11:07:34.518228',0,23,'09123608173','09932062665',1),(25,'.','2023-08-05 11:07:44.014254',0,NULL,NULL,'09123608173',1),(26,'سلام','2023-08-05 11:09:35.041516',0,NULL,NULL,'09123608173',1),(27,'تست','2023-08-05 12:27:54.289190',0,NULL,NULL,'09123608173',1),(28,'jsj','2023-08-05 12:28:10.505034',0,27,'09123608173','09932062665',1);
/*!40000 ALTER TABLE `table_chat_room` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-08-05 16:47:48
