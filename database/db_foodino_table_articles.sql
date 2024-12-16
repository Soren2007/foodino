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
-- Table structure for table `table_articles`
--

DROP TABLE IF EXISTS `table_articles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `table_articles` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `article_title` varchar(60) NOT NULL,
  `article_slug` varchar(200) NOT NULL,
  `article_short_url` varchar(200) DEFAULT NULL,
  `article_main_image` varchar(100) NOT NULL,
  `article_summary_text` longtext,
  `article_main_text` longtext NOT NULL,
  `article_register_date` date NOT NULL,
  `article_publish_date` date NOT NULL,
  `article_update_date` datetime(6) NOT NULL,
  `article_read_time` int NOT NULL,
  `article_is_active` tinyint(1) NOT NULL,
  `article_file` varchar(100) DEFAULT NULL,
  `article_visits` smallint unsigned NOT NULL,
  `article_group` varchar(200) NOT NULL,
  `article_likes` bigint unsigned NOT NULL,
  `article_dislikes` bigint unsigned NOT NULL,
  `is_translated_content` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `table_articles_article_slug_fc2a4861` (`article_slug`),
  CONSTRAINT `table_articles_chk_1` CHECK ((`article_visits` >= 0)),
  CONSTRAINT `table_articles_chk_2` CHECK ((`article_likes` >= 0)),
  CONSTRAINT `table_articles_chk_3` CHECK ((`article_dislikes` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `table_articles`
--

LOCK TABLES `table_articles` WRITE;
/*!40000 ALTER TABLE `table_articles` DISABLE KEYS */;
INSERT INTO `table_articles` VALUES (1,'هلو برای سرماخوردگی','how-to-build-ferdows-garden','http://127.0.0.1:8000/blog/1','images/blog/article/khavas-holoo-sarma-khoredegi.jpg','در نگاه اول، هلو با پوست کرک‌دار و خوش‌عطر خود، میوه‌ای معمولی به نظر می‌رسد، اما خواص فوق‌العاده‌ای دارد که برای حفاظت از سلامتی بدن در فصل سرما یا برای افرادی که دارای سیستم ایمنی ضعیفی هستند بیش از پیش ارزشمند می‌شود.','<h3><span style=\'color:#e67e22\'><span style=\'font-size:20px\'>ویتامین C هلو: ارتقا دهنده&zwnj;ی قدرت ایمنی بدن در برابر بیماری&zwnj;ها</span></span></h3><p>هلو حاوی مقادیر قابل توجهی از ویتامین C است که بدن را در برابر بیماری&zwnj;های ویروسی و باکتریایی محافظت می&zwnj;کند. ویتامین C نیز موجب می&zwnj;شود تا بدن بتواند آهن را بیشتر جذب کند. در فصل سرما، افزایش مصرف هلو به تقویت سیستم ایمنی بدن کمک خواهد کرد. بالا بردن میزان ویتامین C در بدن با مصرف هلو، یک روش طبیعی و خوشمزه برای مقابله با سرماخوردگی است.</p><p>&nbsp;</p><p>&nbsp;</p><h3><span style=\'color:#e67e22\'><span style=\'font-size:20px\'>خواص دیگر هلو: منبع غنی از اسید اسکوربیک و روی</span></span></h3><p>هلو بر خلاف ظاهر معمولی خود، میوه&zwnj;ای است که پر از اسید اسکوربیک و روی است. این دو ماده، در حفظ عملکرد طبیعی بدن و تقویت سیستم ایمنی بدن بسیار مفید هستند. بر اساس تحقیقات انجام شده، وجود ویتامین C و روی در هلو می&zwnj;تواند به بهبودی جراحت&zwnj;ها کمک کند. همچنین، به دلیل وجود آنتی&zwnj;اکسیدان&zwnj;ها در هلو، این میوه می&zwnj;تواند در پیشگیری و درمان عفونت&zwnj;ها و بیماری&zwnj;هایی مثل سرماخوردگی مؤثر باشد.</p><p>&nbsp;</p><h3><span style=\'color:#e67e22\'><span style=\'font-size:20px\'>ویتامین C هلو: یک سپر محکم در برابر عفونت&zwnj;های ریوی</span></span></h3><p>هلو، یک منبع عالی از ویتامین C است که به عنوان یک آنتی&zwnj;اکسیدان قوی عمل می&zwnj;کند و در مقابله با عفونت&zwnj;های ریوی بدن، یک میوه قابل اعتماد است. ویتامین C نقش مهمی در تقویت سیستم ایمنی بدن و در مقابله با عفونت&zwnj;های مختلف، خصوصاً عفونت&zwnj;های ریوی دارد. این ماده ضروری می&zwnj;تواند در کاهش شدت و مدت زمانی علائمی مثل سرفه و تنگی نفس موثر باشد. بنابراین، با افزایش مصرف هلو می&zwnj;توانید به درمان و پیشگیری از سرماخوردگی و عفونت&zwnj;های ریوی کمک کنید.</p><p>&nbsp;</p><p>&nbsp;</p><h3><span style=\'color:#e67e22\'><span style=\'font-size:20px\'>هلو، چگونه باید خرید و نگهداری شود؟</span></span></h3><p>هنگام خرید هلو، به بوی شیرین آن توجه کنید. هر چه هلو بوی شیرین&zwnj;تری داشته باشد، یعنی بیشتر رسیده است. هلوهایی که نرم هستند نشان&zwnj;دهنده&zwnj;ی رسیدگی آن&zwnj;هاست. هلوهای سفت را می&zwnj;توان برای چندین روز در هوای بیرون از یخچال نگه داشت تا برسند و نرم شوند. اما وقتی برسند و مصرف نشوند، به&zwnj;تدریج محتوای ویتامین&zwnj; C خود را از دست می&zwnj;دهند.</p><p>&nbsp;</p><h3><span style=\'color:#e67e22\'><span style=\'font-size:20px\'>خلاصه و نتیجه&zwnj;گیری</span></span></h3><p>در نهایت، با دانستن خواص هلو برای سرماخوردگی، می&zwnj;توانیم بهتر از بدنمان در فصل سرما محافظت کنیم. هلو، با خواص تقویت کننده سیستم ایمنی بدن، میوه&zwnj;ای است که می&zwnj;تواند به ما کمک کند تا با خوبی از سرماخوردگی و بیماری&zwnj;های دیگر جلوگیری کنیم. پس با خرید هلوهای تازه و رسیده و افزایش مصرف آن در رژیم غذایی خود، سلامتی خود را در فصل سرما تقویت کنید. در ادامه شما را به مطالعه مقاله ✅&nbsp;<a href=\'https://chishi.ir/1022-khavas-holoo/\'><strong>تمام خواص و مضرات هلو</strong></a>&nbsp;دعوت می&zwnj;کنیم.</p>','2023-07-28','2023-07-28','2023-07-28 10:59:20.559764',15,1,'',57,'آموزشی',1,0,1),(2,'هلو برای سرماخوردگی','how-to-build-ferdows-garden-2','http://127.0.0.1:8000/blog/2','images/blog/article/khavas-gol-niloufar.jpg','در نگاه اول، هلو با پوست کرک‌دار و خوش‌عطر خود، میوه‌ای معمولی به نظر می‌رسد، اما خواص فوق‌العاده‌ای دارد که برای حفاظت از سلامتی بدن در فصل سرما یا برای افرادی که دارای سیستم ایمنی ضعیفی هستند بیش از پیش ارزشمند می‌شود.','<h3>ویتامین C هلو: ارتقا دهنده&zwnj;ی قدرت ایمنی بدن در برابر بیماری&zwnj;ها</h3><p>هلو حاوی مقادیر قابل توجهی از ویتامین C است که بدن را در برابر بیماری&zwnj;های ویروسی و باکتریایی محافظت می&zwnj;کند. ویتامین C نیز موجب می&zwnj;شود تا بدن بتواند آهن را بیشتر جذب کند. در فصل سرما، افزایش مصرف هلو به تقویت سیستم ایمنی بدن کمک خواهد کرد. بالا بردن میزان ویتامین C در بدن با مصرف هلو، یک روش طبیعی و خوشمزه برای مقابله با سرماخوردگی است.</p><p>&nbsp;</p><p>&nbsp;</p><h3>خواص دیگر هلو: منبع غنی از اسید اسکوربیک و روی</h3><p>هلو بر خلاف ظاهر معمولی خود، میوه&zwnj;ای است که پر از اسید اسکوربیک و روی است. این دو ماده، در حفظ عملکرد طبیعی بدن و تقویت سیستم ایمنی بدن بسیار مفید هستند. بر اساس تحقیقات انجام شده، وجود ویتامین C و روی در هلو می&zwnj;تواند به بهبودی جراحت&zwnj;ها کمک کند. همچنین، به دلیل وجود آنتی&zwnj;اکسیدان&zwnj;ها در هلو، این میوه می&zwnj;تواند در پیشگیری و درمان عفونت&zwnj;ها و بیماری&zwnj;هایی مثل سرماخوردگی مؤثر باشد.</p><p>&nbsp;</p><h3>ویتامین C هلو: یک سپر محکم در برابر عفونت&zwnj;های ریوی</h3><p>هلو، یک منبع عالی از ویتامین C است که به عنوان یک آنتی&zwnj;اکسیدان قوی عمل می&zwnj;کند و در مقابله با عفونت&zwnj;های ریوی بدن، یک میوه قابل اعتماد است. ویتامین C نقش مهمی در تقویت سیستم ایمنی بدن و در مقابله با عفونت&zwnj;های مختلف، خصوصاً عفونت&zwnj;های ریوی دارد. این ماده ضروری می&zwnj;تواند در کاهش شدت و مدت زمانی علائمی مثل سرفه و تنگی نفس موثر باشد. بنابراین، با افزایش مصرف هلو می&zwnj;توانید به درمان و پیشگیری از سرماخوردگی و عفونت&zwnj;های ریوی کمک کنید.</p><p>&nbsp;</p><p>&nbsp;</p><h3>هلو، چگونه باید خرید و نگهداری شود؟</h3><p>هنگام خرید هلو، به بوی شیرین آن توجه کنید. هر چه هلو بوی شیرین&zwnj;تری داشته باشد، یعنی بیشتر رسیده است. هلوهایی که نرم هستند نشان&zwnj;دهنده&zwnj;ی رسیدگی آن&zwnj;هاست. هلوهای سفت را می&zwnj;توان برای چندین روز در هوای بیرون از یخچال نگه داشت تا برسند و نرم شوند. اما وقتی برسند و مصرف نشوند، به&zwnj;تدریج محتوای ویتامین&zwnj; C خود را از دست می&zwnj;دهند.</p><p>&nbsp;</p><h3>خلاصه و نتیجه&zwnj;گیری</h3><p>در نهایت، با دانستن خواص هلو برای سرماخوردگی، می&zwnj;توانیم بهتر از بدنمان در فصل سرما محافظت کنیم. هلو، با خواص تقویت کننده سیستم ایمنی بدن، میوه&zwnj;ای است که می&zwnj;تواند به ما کمک کند تا با خوبی از سرماخوردگی و بیماری&zwnj;های دیگر جلوگیری کنیم. پس با خرید هلوهای تازه و رسیده و افزایش مصرف آن در رژیم غذایی خود، سلامتی خود را در فصل سرما تقویت کنید. در ادامه شما را به مطالعه مقاله ✅&nbsp;<a href=\'https://chishi.ir/1022-khavas-holoo/\'><strong>تمام خواص و مضرات هلو</strong></a>&nbsp;دعوت می&zwnj;کنیم.</p>','2023-07-30','2023-07-30','2023-07-30 14:31:18.012311',15,1,'',7,'آموزشی',2,0,1);
/*!40000 ALTER TABLE `table_articles` ENABLE KEYS */;
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
