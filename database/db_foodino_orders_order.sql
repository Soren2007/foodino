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
-- Table structure for table `orders_order`
--

DROP TABLE IF EXISTS `orders_order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orders_order` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `register_date` datetime(6) NOT NULL,
  `update_date` datetime(6) NOT NULL,
  `is_finally` tinyint(1) NOT NULL,
  `order_code` char(32) NOT NULL,
  `qr_code_image` varchar(100) DEFAULT NULL,
  `qr_code_color` varchar(18) NOT NULL,
  `discount` int DEFAULT NULL,
  `description` longtext,
  `is_translated_content` tinyint(1) NOT NULL,
  `customer_id` bigint NOT NULL,
  `payment_id` bigint DEFAULT NULL,
  `status_id` bigint DEFAULT NULL,
  `delivery_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `order_code` (`order_code`),
  KEY `orders_order_payment_id_46928ccc_fk_orders_paymenttype_id` (`payment_id`),
  KEY `orders_order_customer_id_0b76f6a4_fk_table_customer_user_id` (`customer_id`),
  KEY `orders_order_status_id_d80abc38_fk_orders_orderstatus_id` (`status_id`),
  KEY `orders_order_delivery_id_8f6e0d69_fk_table_delivery_id` (`delivery_id`),
  CONSTRAINT `orders_order_customer_id_0b76f6a4_fk_table_customer_user_id` FOREIGN KEY (`customer_id`) REFERENCES `table_customer` (`user_id`),
  CONSTRAINT `orders_order_delivery_id_8f6e0d69_fk_table_delivery_id` FOREIGN KEY (`delivery_id`) REFERENCES `table_delivery` (`id`),
  CONSTRAINT `orders_order_payment_id_46928ccc_fk_orders_paymenttype_id` FOREIGN KEY (`payment_id`) REFERENCES `orders_paymenttype` (`id`),
  CONSTRAINT `orders_order_status_id_d80abc38_fk_orders_orderstatus_id` FOREIGN KEY (`status_id`) REFERENCES `orders_orderstatus` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=47 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders_order`
--

LOCK TABLES `orders_order` WRITE;
/*!40000 ALTER TABLE `orders_order` DISABLE KEYS */;
INSERT INTO `orders_order` VALUES (39,'2023-08-04 14:27:58.343897','2023-08-04 14:50:52.258858',0,'b0785bbf7ae5406f8eb3c7759146502c','images/order/qr_code/b0785bbf-7ae5-406f-8eb3-c7759146502c.jpg','#ff5000',0,'None',0,1,1,1,1),(40,'2023-08-04 15:33:08.950403','2023-08-04 15:33:09.045953',0,'ec6780de82f94408af771cd33069d6ef','images/order/qr_code/ec6780de-82f9-4408-af77-1cd33069d6ef.jpg','#ff5000',0,NULL,0,1,1,1,NULL),(41,'2023-08-04 16:05:42.000000','2023-08-04 18:35:06.723242',1,'0a094bb503564ab89dee203f65b1553f','images/order/qr_code/0a094bb5-0356-4ab8-9dee-203f65b1553f.jpg','#FF5000FF',0,'',0,1,1,1,NULL),(42,'2023-08-04 22:46:13.518000','2023-08-04 22:46:13.614594',0,'5bc12ca1ca7d4f14894ca3545faeab88','images/order/qr_code/5bc12ca1-ca7d-4f14-894c-a3545faeab88.jpg','#ff5000',0,NULL,0,1,1,1,NULL),(43,'2023-08-05 07:16:29.322868','2023-08-05 07:16:29.408706',0,'51f07dd004dd45b6b6eea1e865390584','images/order/qr_code/51f07dd0-04dd-45b6-b6ee-a1e865390584.jpg','#ff5000',0,NULL,0,2,1,1,NULL),(44,'2023-08-05 08:00:22.232400','2023-08-05 08:00:22.351919',0,'cae158657b954a76ad6a5ae13f3f66b2','images/order/qr_code/cae15865-7b95-4a76-ad6a-5ae13f3f66b2.jpg','#ff5000',0,NULL,0,1,1,1,NULL),(45,'2023-08-05 09:02:01.410077','2023-08-05 09:02:01.487858',0,'2687c6a65a8c49f4bc927eed66a1b4b6','images/order/qr_code/2687c6a6-5a8c-49f4-bc92-7eed66a1b4b6.jpg','#ff5000',0,NULL,0,1,1,1,NULL),(46,'2023-08-05 09:02:33.324077','2023-08-05 11:34:39.683755',0,'dc3cfee5fd9d446bb2d4876087ff6357','images/order/qr_code/dc3cfee5-fd9d-446b-b2d4-876087ff6357.jpg','#ff5000',0,'None',0,1,1,1,1);
/*!40000 ALTER TABLE `orders_order` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-08-05 16:47:54
