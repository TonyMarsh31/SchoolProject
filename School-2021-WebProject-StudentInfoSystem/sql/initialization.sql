-- MySQL dump 10.13  Distrib 8.0.26, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: webproject-studentinfosystem
-- ------------------------------------------------------
-- Server version	8.0.26

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
-- Table structure for table `grade`
--

DROP TABLE IF EXISTS `grade`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `grade` (
  `gradeid` int NOT NULL AUTO_INCREMENT,
  `gradename` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`gradeid`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `grade`
--

LOCK TABLES `grade` WRITE;
/*!40000 ALTER TABLE `grade` DISABLE KEYS */;
INSERT INTO `grade` VALUES (1,'一年级'),(2,'二年级'),(3,'三年级'),(4,'四年级'),(5,'五年级');
/*!40000 ALTER TABLE `grade` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student` (
  `stuid` int NOT NULL AUTO_INCREMENT,
  `stuname` varchar(5) DEFAULT NULL,
  `stuno` varchar(10) DEFAULT NULL,
  `sex` int DEFAULT NULL COMMENT '1表示男生，0表示女生',
  `phone` varchar(11) DEFAULT NULL,
  `email` varchar(30) DEFAULT NULL,
  `registered` varchar(10) DEFAULT NULL COMMENT '户籍所在地',
  `address` varchar(50) DEFAULT NULL,
  `profession` varchar(10) DEFAULT NULL,
  `idnumber` varchar(20) DEFAULT NULL,
  `politics` varchar(10) DEFAULT NULL COMMENT '政治面貌',
  `regdate` date DEFAULT NULL,
  `state` int DEFAULT NULL COMMENT '就学状态 1:在读 2：休学 3：退学 4：删除',
  `introduction` varchar(200) DEFAULT NULL,
  `gid` int DEFAULT NULL COMMENT '班级',
  PRIMARY KEY (`stuid`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

LOCK TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
INSERT INTO `student` VALUES (1,'张三1','stu1001',0,'13719203921','1233253@qq.com','北京','昌平区XXX镇','物理','11091211029121212','党员','2020-06-12',1,'优秀学员1',1),(2,'李四','stu1002',1,'13719203421','121253@qq.com','上海','XXX区','化学','45691211029121212','党员','2020-05-03',4,'优秀学员2',1),(3,'王五223','stu1003',1,'13715203921','2321253@qq.com','杭州','XXX区','生物','32291211029121212','党员','2020-04-04',1,'优秀学员3',2),(4,'赵六','stu1004',1,'13716203921','35463253@qq.com','四川','XXX区','英语','33391211029121212','群众','2020-03-10',1,'优秀学员4',2),(5,'李磊','stu1005',0,'18719203921','65765553@qq.com','湖南','XXX区','医学','222291211029121212','群众','2020-02-18',1,'优秀学员5',3),(6,'韩梅梅','stu1006',0,'13719673921','54654653@qq.com','武汉','XXX区','政治','242291211029121212','群众','2020-01-17',4,'优秀学员6',3),(7,'斯蒂文','stu1007',0,'13743203921','43532253@qq.com','天津','XXX区','计算机','22091211029121212','群众','2020-07-18',4,'优秀学员7',3),(11,'杨11','s1010',1,'13333333333','1332@126.com','北京','朝阳','java','11011111','党员','2020-11-29',1,'一个新开辟领域的探讨，探讨摸索',1),(12,'杨XX','s1020',1,'13333333333','1332@126.com','北京','朝阳','java','11011111111','党员','2020-11-30',1,'一个新开辟领域的探讨，探讨摸索',1),(13,'杨XX','s1020',1,'13333333333','1332@126.com','北京','朝阳','java','1101111111','党员','2020-11-30',1,'一个新开辟领域的探讨，探讨摸索',1),(14,'abc','s1021',1,'13333333333','1332@126.com','北京','朝阳','java','1101111','党员','2020-11-30',1,'一个新开辟领域的探讨，探讨摸索',1),(15,'杨Xa','s1111',1,'13333333333','1332@126.com','北京','朝阳','java','11011111111','党员','2020-11-30',1,'一个新开辟领域的探讨，探讨摸索',1),(16,'杨aa','s1111',1,'13333333333','1332@126.com','北京','朝阳','java','110111111','党员','2020-11-30',1,'一个新开辟领域的探讨，探讨摸索',1),(17,'杨q','s1113',1,'13333333333','1332@126.com','北京1','朝阳','java','11011111','党员','2020-11-30',4,'一个新开辟领域的探讨，探讨摸索',1),(20,'测试1','',1,'12312311231','name@address.com','','','xxx','','','2021-12-19',4,'介绍的内容：',1);
/*!40000 ALTER TABLE `student` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `userid` int NOT NULL AUTO_INCREMENT,
  `loginname` varchar(10) DEFAULT NULL,
  `password` varchar(12) DEFAULT NULL,
  `realname` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`userid`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'admin','123456','张三'),(2,'user1','123456','李四'),(3,'user2','123456','王五');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-12-19 20:58:10
