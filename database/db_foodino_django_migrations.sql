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
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=106 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'gift','0001_initial','2023-07-30 01:22:04.159906'),(2,'contenttypes','0001_initial','2023-07-30 01:22:04.207435'),(3,'contenttypes','0002_remove_content_type_name','2023-07-30 01:22:04.303838'),(4,'auth','0001_initial','2023-07-30 01:22:04.644351'),(5,'auth','0002_alter_permission_name_max_length','2023-07-30 01:22:04.714886'),(6,'auth','0003_alter_user_email_max_length','2023-07-30 01:22:04.726897'),(7,'auth','0004_alter_user_username_opts','2023-07-30 01:22:04.734882'),(8,'auth','0005_alter_user_last_login_null','2023-07-30 01:22:04.743965'),(9,'auth','0006_require_contenttypes_0002','2023-07-30 01:22:04.747895'),(10,'auth','0007_alter_validators_add_error_messages','2023-07-30 01:22:04.756892'),(11,'auth','0008_alter_user_username_max_length','2023-07-30 01:22:04.767097'),(12,'auth','0009_alter_user_last_name_max_length','2023-07-30 01:22:04.777212'),(13,'auth','0010_alter_group_name_max_length','2023-07-30 01:22:04.813808'),(14,'auth','0011_update_proxy_permissions','2023-07-30 01:22:04.826818'),(15,'auth','0012_alter_user_first_name_max_length','2023-07-30 01:22:04.837806'),(16,'accounts','0001_initial','2023-07-30 01:22:06.089294'),(17,'Email','0001_initial','2023-07-30 01:22:06.114300'),(18,'Email','0002_initial','2023-07-30 01:22:06.395894'),(19,'account','0001_initial','2023-07-30 01:22:06.618928'),(20,'account','0002_email_max_length','2023-07-30 01:22:06.661921'),(21,'ad','0001_initial','2023-07-30 01:22:06.726437'),(22,'admin','0001_initial','2023-07-30 01:22:06.891506'),(23,'admin','0002_logentry_remove_auto_add','2023-07-30 01:22:06.916498'),(24,'admin','0003_logentry_add_action_flag_choices','2023-07-30 01:22:06.935569'),(25,'blog','0001_initial','2023-07-30 01:22:07.395357'),(26,'branch','0001_initial','2023-07-30 01:22:07.795331'),(27,'message','0001_initial','2023-07-30 01:22:08.240795'),(28,'chat_gpt','0001_initial','2023-07-30 01:22:08.343951'),(29,'food','0001_initial','2023-07-30 01:22:10.664474'),(30,'comments','0001_initial','2023-07-30 01:22:11.211949'),(31,'discounts','0001_initial','2023-07-30 01:22:11.521411'),(32,'event','0001_initial','2023-07-30 01:22:11.616445'),(33,'favorites','0001_initial','2023-07-30 01:22:11.991884'),(34,'language','0001_initial','2023-07-30 01:22:12.121913'),(35,'main','0001_initial','2023-07-30 01:22:12.203406'),(36,'mukbang','0001_initial','2023-07-30 01:22:12.466984'),(37,'my_environment','0001_initial','2023-07-30 01:22:12.999423'),(38,'orders','0001_initial','2023-07-30 01:22:14.014293'),(39,'reservation','0001_initial','2023-07-30 01:22:14.350474'),(40,'payments','0001_initial','2023-07-30 01:22:14.843258'),(41,'scores','0001_initial','2023-07-30 01:22:15.032143'),(42,'sessions','0001_initial','2023-07-30 01:22:15.076150'),(43,'sites','0001_initial','2023-07-30 01:22:15.106702'),(44,'sites','0002_alter_domain_unique','2023-07-30 01:22:15.138701'),(45,'socialaccount','0001_initial','2023-07-30 01:22:15.955297'),(46,'socialaccount','0002_token_max_lengths','2023-07-30 01:22:16.077039'),(47,'socialaccount','0003_extra_data_default_dict','2023-07-30 01:22:16.114548'),(48,'subscription','0001_initial','2023-07-30 01:22:17.019456'),(49,'accounts','0002_alter_customer_city','2023-07-30 10:10:19.712917'),(50,'ad','0002_alter_ad_ad_is_active','2023-07-30 10:10:19.725336'),(51,'message','0002_message_mobile_number_alter_message_email','2023-07-30 10:10:19.931541'),(52,'orders','0002_alter_order_status','2023-07-30 10:10:20.295068'),(53,'accounts','0003_customuser_current_order_customuser_delivered_order_and_more','2023-08-01 23:28:23.493356'),(54,'subscription','0002_subscriptionuser_subscription','2023-08-03 19:44:25.619857'),(55,'orders','0003_orderdetails_register_date_time_and_more','2023-08-03 19:44:25.957681'),(56,'accounts','0004_alter_customer_city','2023-08-03 21:40:44.146210'),(57,'ad','0003_alter_ad_ad_is_active','2023-08-03 21:40:44.165281'),(58,'delivery','0001_initial','2023-08-03 21:40:44.848543'),(59,'accounts','0005_alter_customer_city','2023-08-03 21:45:56.990388'),(60,'ad','0004_alter_ad_ad_is_active','2023-08-03 21:45:57.008023'),(61,'delivery','0002_rename_vehicletype_delivery_vehicle_type','2023-08-03 21:45:57.343588'),(62,'accounts','0006_alter_customer_city','2023-08-03 21:48:04.839465'),(63,'ad','0005_alter_ad_ad_is_active','2023-08-03 21:48:04.856136'),(64,'delivery','0003_remove_delivery_the_orders_he_ro_she_has_won_and_more','2023-08-03 21:48:05.428816'),(65,'accounts','0007_alter_customer_city','2023-08-03 23:02:05.550606'),(66,'ad','0006_alter_ad_ad_is_active','2023-08-03 23:02:05.588414'),(67,'delivery','0004_delivery_is_accepted','2023-08-03 23:02:05.767242'),(68,'accounts','0008_customuser_is_delivery_alter_customer_city','2023-08-03 23:08:46.782750'),(69,'ad','0007_alter_ad_ad_is_active','2023-08-03 23:08:46.796042'),(70,'accounts','0009_alter_customer_city','2023-08-04 02:06:13.675416'),(71,'ad','0008_alter_ad_ad_is_active','2023-08-04 02:06:13.706854'),(72,'delivery','0005_remove_delivery_the_orders_he_ro_she_has_won','2023-08-04 02:06:13.864261'),(73,'orders','0004_order_delivery','2023-08-04 02:06:14.062604'),(74,'accounts','0010_alter_customer_city','2023-08-04 02:13:27.496333'),(75,'ad','0009_alter_ad_ad_is_active','2023-08-04 02:13:27.511350'),(76,'orders','0005_remove_orderdetails_register_date_time','2023-08-04 02:13:27.679280'),(77,'accounts','0011_alter_customer_city','2023-08-04 02:20:44.058593'),(78,'ad','0010_alter_ad_ad_is_active','2023-08-04 02:20:44.071801'),(79,'orders','0006_alter_order_delivery','2023-08-04 02:20:44.420218'),(80,'accounts','0012_alter_customer_city','2023-08-04 02:30:22.560926'),(81,'ad','0011_alter_ad_ad_is_active','2023-08-04 02:30:22.580514'),(82,'delivery','0006_delivery_branch','2023-08-04 02:30:22.780434'),(83,'accounts','0013_customuser_city_customuser_state_alter_customer_city','2023-08-04 11:08:37.685034'),(84,'ad','0012_alter_ad_ad_is_active','2023-08-04 11:08:37.696759'),(85,'ad','0013_alter_ad_ad_is_active','2023-08-04 11:23:21.452526'),(86,'ad','0014_alter_ad_ad_is_active','2023-08-04 11:23:21.466511'),(87,'ad','0015_alter_ad_ad_is_active','2023-08-04 11:23:21.476587'),(88,'accounts','0014_remove_customer_image_alter_customer_address_and_more','2023-08-04 12:30:43.981669'),(89,'ad','0016_alter_ad_ad_is_active','2023-08-04 12:30:43.997824'),(90,'my_environment','0002_robot_takes_containers_is_active','2023-08-04 12:30:44.089403'),(91,'ad','0017_alter_ad_ad_is_active','2023-08-04 12:42:47.938340'),(92,'my_environment','0003_alter_robot_takes_containers_google_map_location_link','2023-08-04 12:42:48.141287'),(93,'ad','0018_alter_ad_ad_is_active','2023-08-04 14:14:12.016606'),(94,'delivery','0007_delivery_your_last_activity','2023-08-04 14:14:12.324591'),(95,'ad','0019_alter_ad_ad_is_active','2023-08-04 14:27:44.814180'),(96,'orders','0007_alter_order_delivery','2023-08-04 14:27:45.244792'),(97,'accounts','0015_customer_latitude_location_and_more','2023-08-04 16:05:24.604470'),(98,'ad','0020_alter_ad_ad_is_active','2023-08-04 16:05:24.625890'),(99,'ad','0021_alter_ad_ad_is_active','2023-08-04 18:05:40.275119'),(100,'accounts','0016_alter_customer_latitude_location_and_more','2023-08-04 18:09:45.398404'),(101,'ad','0022_alter_ad_ad_is_active','2023-08-04 18:09:45.415405'),(102,'ad','0023_alter_ad_ad_is_active','2023-08-04 21:45:38.528551'),(103,'ad','0024_alter_ad_ad_is_active','2023-08-04 21:46:26.103764'),(104,'ad','0025_alter_ad_ad_is_active','2023-08-04 21:46:49.317694'),(105,'ad','0026_alter_ad_ad_is_active','2023-08-04 21:47:31.333474');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-08-05 16:47:58
