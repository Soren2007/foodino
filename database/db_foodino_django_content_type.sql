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
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=68 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (57,'account','emailaddress'),(58,'account','emailconfirmation'),(23,'accounts','city'),(21,'accounts','country'),(25,'accounts','customer'),(24,'accounts','customuser'),(22,'accounts','state'),(45,'ad','ad'),(1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(9,'blog','article'),(7,'blog','author'),(8,'blog','keyword'),(38,'branch','branch'),(63,'chat_gpt','chatgpt'),(34,'comments','comment'),(4,'contenttypes','contenttype'),(67,'delivery','delivery'),(66,'delivery','vehicletype'),(29,'discounts','coupon'),(30,'discounts','discountbasket'),(31,'discounts','discountbasketdetail'),(50,'Email','email'),(40,'event','event'),(41,'event','footer_event'),(42,'event','top_menu_event'),(37,'favorites','favorite'),(36,'favorites','favorite_blog'),(10,'food','food'),(11,'food','foodgroup'),(17,'food','foodstufftype'),(12,'food','meal'),(16,'food','myrecipes'),(15,'food','recipes'),(14,'food','stuff'),(13,'food','stuffgroup'),(47,'gift','gift'),(49,'gift','lottery'),(48,'gift','wheel_of_luck'),(43,'language','language'),(44,'language','languagefont'),(62,'main','frequently_asked_question'),(6,'main','slid'),(20,'message','chatroom'),(18,'message','message'),(19,'message','userchatroom'),(46,'mukbang','mukbang'),(55,'my_environment','my_environment'),(54,'my_environment','robot_takes_containers'),(26,'orders','order'),(28,'orders','orderdetails'),(65,'orders','orderdetailssubscription'),(64,'orders','orderstatus'),(27,'orders','paymenttype'),(33,'payments','currency'),(32,'payments','payment'),(39,'reservation','reservation'),(35,'scores','scoring'),(5,'sessions','session'),(56,'sites','site'),(59,'socialaccount','socialaccount'),(60,'socialaccount','socialapp'),(61,'socialaccount','socialtoken'),(51,'subscription','promise'),(52,'subscription','subscription'),(53,'subscription','subscriptionuser');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
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
