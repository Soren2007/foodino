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
-- Table structure for table `table_food_recipes`
--

DROP TABLE IF EXISTS `table_food_recipes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `table_food_recipes` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `recipe_image` varchar(100) NOT NULL,
  `recipe_slug` varchar(120) NOT NULL,
  `recipe` longtext NOT NULL,
  `recipe_name` varchar(60) NOT NULL,
  `recipe_views` int unsigned NOT NULL,
  `recipe_video` varchar(100) DEFAULT NULL,
  `recipe_register_date` date NOT NULL,
  `recipe_publish_date` date NOT NULL,
  `recipe_update_date` datetime(6) NOT NULL,
  `recipe_is_active` tinyint(1) NOT NULL,
  `recipe_dislikes` bigint unsigned NOT NULL,
  `recipe_likes` bigint unsigned NOT NULL,
  `recipe_summary_text` longtext NOT NULL DEFAULT (_utf8mb3'sdsdsdsd'),
  `recipe_file` varchar(100) DEFAULT NULL,
  `recipe_short_url` varchar(200) DEFAULT NULL,
  `is_translated_content` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `table_food_recipes_recipe_slug_796ab4db` (`recipe_slug`),
  CONSTRAINT `table_food_recipes_chk_1` CHECK ((`recipe_views` >= 0)),
  CONSTRAINT `table_food_recipes_chk_2` CHECK ((`recipe_dislikes` >= 0)),
  CONSTRAINT `table_food_recipes_chk_3` CHECK ((`recipe_likes` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `table_food_recipes`
--

LOCK TABLES `table_food_recipes` WRITE;
/*!40000 ALTER TABLE `table_food_recipes` DISABLE KEYS */;
INSERT INTO `table_food_recipes` VALUES (2,'images/food/recipes/pitza-makhlout.jpg','mix-pizza','<h3><span style=\'font-size:20px\'><span style=\'color:#e67e22\'>مرحله اول</span></span></h3><p>اول از همه باید توجه داشته باشید که&nbsp;<strong><a href=\'https://chishi.ir/1261-pitza-makhlout/\'>پیتزا مخلوط ایتالیایی</a></strong>&nbsp;و اصل با کالباس ساده و سوسیس تهیه می شود و دارای گوشت چرخ کرده نیست. اما در صورت تمایل می توانید به جای استفاده از سوسیس و کالباس از گوشت هم استفاده کنید.</p><p>&nbsp;</p><p>&nbsp;</p><h3><span style=\'font-size:20px\'><span style=\'color:#e67e22\'>مرحله دوم</span></span></h3><p>مرحله اول پخت پیتزا آماده کردن خمیر پیتزا می باشد، می توانید خمیر پیتزا را به صورت آماده از فروشگاه ها تهیه کنید. البته توصیه می شود برای تهیه پیتزا از خمیر پیتزای خانگی استفاده شود، چون طعم و کیفیت خیلی بهتری دارد.</p><p>&nbsp;</p><p>&nbsp;</p><h3><span style=\'font-size:20px\'><span style=\'color:#e67e22\'>مرحله سوم</span></span></h3><p>ابتدا خمیرهای پیتزا را داخل ظرف لبه دار پخت پیتزا قرار می دهیم به صورتی که لبه های خمیر از ظرف خارج شود و خمیر حالت گودی پیدا کند، سپس روی هر خمیر ۱ قاشق غذاخوری سس کچاپ یا سس پیتزای خانگی می زنیم.</p><p>&nbsp;</p><p>&nbsp;</p><h3><span style=\'font-size:20px\'><span style=\'color:#e67e22\'>مرحله چهارم</span></span></h3><p>حالا با پشت قاشق سس پیتزا را به صورت یکنواخت روی خمیر پیتزا پخش می کنیم. حالا با مقدار کمی پنیر پیتزا روی سس کچاپ را پوشش می دهیم. در ادامه کالباس مارتادلا را به صورت نگینی ریز خرد کرده و به دو قسمت تقسیم می کنیم.</p><p>&nbsp;</p><p>&nbsp;</p><h3><span style=\'font-size:20px\'><span style=\'color:#e67e22\'>مرحله پنجم</span></span></h3><p>سپس به صورت مساوی روی پنیر پیتزا می ریزیم و با کف دست آنرا صاف و یکنواخت می کنیم. در ادامه در صورت تمایل ابتدا سوسیس ها را به صورت حلقه ای خرد کنید، سپس انها را به صورت سرخ کرده یا خام روی کالباس بچینید.</p><p>&nbsp;</p><p>&nbsp;</p><h3><span style=\'font-size:20px\'><span style=\'color:#e67e22\'>مرحله ششم</span></span></h3><p>البته توصیه می شود سوسیس ها را با مقدار کمی روغن تفت دهید، چون به صورت سرخ شده خوشمزه تر هستند. حالا روی سوسیس ها را با پنیر پیتزا به صورت کامل پوشش می دهیم و در ادامه به سراغ تزیین روی پیتزا می رویم.</p><p>&nbsp;</p><p>&nbsp;</p><h3><span style=\'font-size:20px\'><span style=\'color:#e67e22\'>مرحله هفتم</span></span></h3><p>برای تزیین روی پیتزا، قارچ ورقه ای، زیتون ورقه ای، ذرت و فلفل دلمه ای رنگی نگینی شده را به سلیقه خود روی پینر پیتزا می چینیم. فر را باید از ۱۵ دقیقه قبل با حرارت ۱۸۰ درجه سانتیگراد روشن کنیم تا کاملا گرم شود.</p><p>&nbsp;</p><p>&nbsp;</p><h3><span style=\'font-size:20px\'><span style=\'color:#e67e22\'>مرحله هشتم</span></span></h3><p>در این مرحله پس از اینکه فر به طور کامل گرم شد، پیتزا ها را به مدت ۲۰ تا ۳۰ دقیقه درون فر قرار می دهیم تا بپزند. پس از اینکه پیتزاها اماده شدند حدود پنج دقیقه گریل را روشن می کنیم تا پنیر روی پیتزا طلایی شود.</p><p>&nbsp;</p><p>&nbsp;</p><h3><span style=\'font-size:20px\'><span style=\'color:#e67e22\'>مرحله نهم</span></span></h3><p>پس از اینکه پیتزا اماده شد و پینر رویش به طور کامل طلایی شد آنرا از فر خارج می کنیم و با کارد به ۶ تا ۸ قسمت مساوی برش می زنیم. حالا مقداری آویشن روی پیتزا ها می پاشیم و به همراه سس دلخواه سرو می کنیم.</p><p>&nbsp;</p>','پیتزا مخلوط',9,'videos/Recipes/videos/d553fccfa38318b4fe4e22681d71b92840206672-720p.mp4','2023-07-28','2023-07-28','2023-07-28 10:00:24.914230',1,1,0,'sdsdsdsd','','http://127.0.0.1:8000/food/recipe/2',1),(3,'images/food/recipes/pitza-gharch-goosht.jpg','mushrooms-and-meat','<h3><span style=\'font-size:20px\'><span style=\'color:#e67e22\'>مرحله اول</span></span></h3><p>برای تهیه&nbsp;<strong><a href=\'https://chishi.ir/4997-pitza-gharch-goosht/\'>پیتزا قارچ و گوشت رستورانی</a></strong>&nbsp;ابتدا پیاز را به صورت نگینی خرد می کنیم و به همراه مقدار خیلی کمی روغن داخل یک تابه مناسب تفت می دهیم، پس از اینکه پیاز طلایی شد، گوشت چرخ کرده را به تابه اضافه می کنیم.</p><p>&nbsp;</p><h3><span style=\'font-size:20px\'><span style=\'color:#e67e22\'>مرحله دوم</span></span></h3><p>در این مرحله مقداری نمک، فلفل سیاه و زردچوبه اضافه می کنیم و گوشت را به خوبی تفت می دهیم تا رنگش تغییر کند. در ادامه نصف فنجان آب جوش به تابه اضافه می کنیم و درب تابه را می گذاریم تا گوشت به طور کامل بپزد.</p><p>&nbsp;</p><h3><span style=\'font-size:20px\'><span style=\'color:#e67e22\'>مرحله سوم</span></span></h3><p>حالا مقداری از قارچ و فلفل دلمه ای رنگی را برای تزیین روی پیتزا کنار می گذاریم و باقیمانده آنرا به تابه حاوی گوشت اضافه می کنیم و به خوبی تفت می دهیم تا آب اضافی موجود در تابه به طور کامل کشیده شود و قارچ و فلفل دلمه ای نرم شوند.</p><p>&nbsp;</p><h3><span style=\'color:#e67e22\'><span style=\'font-size:20px\'>مرحله چهارم</span></span></h3><p>در این مرحله فر را با دمای ۱۸۰ درجه سانتیگراد روشن می کنیم تا کاملا گرم شودف سپس خمیر پیتزا را درون قالب یا سینی فر قرار می دهیم. در ادامه سس مخصوص پیتزا را روی خمیر پیتزا به صورت یکدست پخش می کنیم.</p><p>&nbsp;</p><h3><span style=\'font-size:20px\'><span style=\'color:#e67e22\'>مرحله پنجم</span></span></h3><p>حالا دو سوم پنیر پیتزا را روی خمیر پیتزا به صورت پخش می ریزیمف در ادامه مخلوط گوشت چرخ کرده را به صورت پخش روی پنیر پیتزا می ریزیم. در ادامه باقیمانده پنیر پیتزا را به صورت پخش روی مخلوط گوشت می ریزیم.</p><p>&nbsp;</p><h3><span style=\'color:#e67e22\'><span style=\'font-size:20px\'>مرحله ششم</span></span></h3><p>در این مرحله قارچ و فلفل دلمه ای رنگی را که که کنار گذاشته بودیم برای تزیین روی پیتزا استفاده می کنیم، سپس پیتزا را به مدت ۲۰ دقیقه درون فر قرار می دهیم تا پینر ذوب شود، سپس چند دقیقه گریل را روشن می کنیم تا روی پیتزا رنگ بگیرد.</p>','پیتزا قارچ و گوشت',2,'videos/Recipes/videos/8fe6350d136abbe37b6468e547a652c112551214-720p.mp4','2023-07-28','2023-07-28','2023-07-28 10:19:12.960213',1,0,1,'sdsdsdsd','','http://127.0.0.1:8000/food/recipe/3',1),(4,'images/food/recipes/shir-berenj.jpg','rice-milk','<h3><span style=\'color:#e67e22\'><span style=\'font-size:20px\'>مرحله اول</span></span></h3><p>برای تهیه شیر برنج مجلسی ابتدا برنج را داخل یک ظرف حاوی آب به مدت دو تا سه ساعت قرار می دهیم تا خیس بخورد، سپس برنج را آبکشی می کنیم و به همراه ۳ لیوان آب و نصف قاشق چایخوری داخل یک قابلمه مناسب می ریزیم.</p><p><strong>نکته:</strong>&nbsp;به هیچ وجه برای خیساندن برنج نباید از نمک استفاده کنیم.</p><p>&nbsp;</p><h3><span style=\'color:#e67e22\'><span style=\'font-size:20px\'>مرحله دوم</span></span></h3><p>در این مرحله قابلمه را روی حرارت زیاد قرار می دهیم تا آب به جوش بیاید. پس از اینکه آب داخل قابلمه جوش امد، صبر می کنیم تا بیشتر آب درون قابلمه تبخیر شد و فقط نصف لیوان از آب باقی ماند.</p><p>&nbsp;</p><p>&nbsp;</p><h3><span style=\'color:#e67e22\'><span style=\'font-size:20px\'>مرحله سوم</span></span></h3><p>حالا شیر را به قابلمه اضافه می کنیم و صبر می کنیم تا برنج به طور کامل مغز پخت و باز شود. حالا شکر را با نصف لیوان آب جوش درون یک کاسه می ریزیم و هم می زنیم، سپس به قابلمه اضافه می کنیم.</p><p>&nbsp;</p><h3><span style=\'color:#e67e22\'><span style=\'font-size:20px\'>مرحله چهارم</span></span></h3><p>پس از اضافه کردن شکر، باید شیر برنج را چند دقیقه متداوم هم بزنیم تا شکر به طور کامل حل شود، حالا باید صبر کنیم تا شیربرنج به غلظت کافی برسد. در ۱۰ دقیقه پایانی پخت، گلاب را به همراه پودر یا اسانس هل به قابلمه اضافه می کنیم.</p><p>&nbsp;</p><p>&nbsp;</p><h3><span style=\'color:#e67e22\'><span style=\'font-size:20px\'>مرحله پنجم</span></span></h3><p>نکته ای که باید در پخت این غذا در نظر داشته باشیم این است که شیر برنج غذایی است که خیلی سریع ته می گیرد، پس در تمام مراحل پخت باید حواس&zwnj;مان به غذا باشد و هر چند لحظه یک&zwnj;بار آن&zwnj;را هم بزنیم تا ته نگیرد.</p><p>&nbsp;</p><p>&nbsp;</p><h3><span style=\'color:#e67e22\'><span style=\'font-size:20px\'>مرحله ششم</span></span></h3><p>پس از گذشت ۱۰ دقیقه قابلمه را از روی حرارت بر می داریم و خامه را به شیر برنج اضافه می کنیم. بهتر است خامه را از قبل در دمای محیط قرار دهیم. پس از اینکه خامه را اضافه کردیم یک دم کنی تمیز روی درب قابلمه قرار می دهیم.</p><p>&nbsp;</p><h3><span style=\'color:#e67e22\'><span style=\'font-size:20px\'>مرحله هفتم</span></span></h3><p>حالا به مدت ۱۰ دقیقه صبر می کنیم تا شیربرنج به طور کامل جا بیفتد. پس از گذشت این زمان دم کنی را برمی داریم و شیر برنج را در ظرف مورد نظرمان می کشیم و با پودر پسته تزیین کرده و سرو می کنیم.</p>','شیر برنج',11,'videos/Recipes/videos/c74f6f03433babbad5b8eefeaa2ce6aa14951066-720p.mp4','2023-07-28','2023-07-28','2023-07-28 10:38:43.701495',0,232,25,'sdsdsdsd','','http://127.0.0.1:8000/food/recipe/4',1);
/*!40000 ALTER TABLE `table_food_recipes` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-08-05 16:47:53
