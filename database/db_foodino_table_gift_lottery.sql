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
-- Table structure for table `table_gift_lottery`
--

DROP TABLE IF EXISTS `table_gift_lottery`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `table_gift_lottery` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(120) NOT NULL,
  `image` varchar(100) NOT NULL,
  `description` longtext NOT NULL,
  `start_of_the_lottery` datetime(6) NOT NULL,
  `is_done` tinyint(1) NOT NULL,
  `is_start` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `user_number` int unsigned NOT NULL,
  `is_translated_content` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `table_gift_lottery_chk_1` CHECK ((`user_number` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `table_gift_lottery`
--

LOCK TABLES `table_gift_lottery` WRITE;
/*!40000 ALTER TABLE `table_gift_lottery` DISABLE KEYS */;
INSERT INTO `table_gift_lottery` VALUES (1,'روز مادر','images/gift/lottery/Lottery/روزمادر.jpg','در دنیای امروز که اکثر محبت ها و عشق ها از ذهن افراد نشات گرفته و با حساب دو دوتا چهار تا عاشق می شوند و محبت پیدا می کنند، این مادر است که عشقش را با قلبش به طور ذاتی و فطری لمس میکند.مادر که در تمام اقلیم ها و تمدن ها از جایگاه والایی برخوردار است. مادری که در اجتماع یک جامعه ی موفق می تواند نه تنها نقش سازنده ای در پرورش و تربیت کودک خود بلکه در پرورش و رشد فرهنگ جامعه نیز تاثیر گذار باشد؛ زیرا همان فرزند قرار است به همراه فرزندان دیگر با حضورشان آن جامعه را ساخته و رونق دهند.در ایران نیز برای گرامی شمردن این جایگاه والا و قدر دانی از این مقام رفیع روز ولادت حضرت صدیقه ی کبری فاطمه ی زهرا (س) را به عنوان نماد یک مادر مطهر و زن فداکار “روز مادر” نام گذاری کرده اند.','2023-07-28 09:48:56.208951',1,0,1,23,1);
/*!40000 ALTER TABLE `table_gift_lottery` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-08-05 16:47:52
