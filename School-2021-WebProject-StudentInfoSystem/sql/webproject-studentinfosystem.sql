/*
 Navicat Premium Data Transfer

 Source Server         : Navicat
 Source Server Type    : MySQL
 Source Server Version : 80022
 Source Host           : localhost:3306
 Source Schema         : webproject-studentinfosystem

 Target Server Type    : MySQL
 Target Server Version : 80022
 File Encoding         : 65001

 Date: 02/03/2022 16:03:49
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for grade
-- ----------------------------
DROP TABLE IF EXISTS `grade`;
CREATE TABLE `grade`  (
  `gradeid` int NOT NULL AUTO_INCREMENT,
  `gradename` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`gradeid`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 6 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of grade
-- ----------------------------
INSERT INTO `grade` VALUES (1, '一年级');
INSERT INTO `grade` VALUES (2, '二年级');
INSERT INTO `grade` VALUES (3, '三年级');
INSERT INTO `grade` VALUES (4, '四年级');
INSERT INTO `grade` VALUES (5, '五年级');

-- ----------------------------
-- Table structure for menu
-- ----------------------------
DROP TABLE IF EXISTS `menu`;
CREATE TABLE `menu`  (
  `menuid` int NOT NULL AUTO_INCREMENT,
  `menuname` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `upmenuid` int NULL DEFAULT NULL,
  `state` int NULL DEFAULT NULL,
  `desc` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `url` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`menuid`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 7 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of menu
-- ----------------------------
INSERT INTO `menu` VALUES (1, '教务中心', 0, 1, NULL, NULL);
INSERT INTO `menu` VALUES (2, '权限管理', 0, 1, NULL, NULL);
INSERT INTO `menu` VALUES (3, '学生管理', 1, 1, NULL, '/Educational/student/StudentServlet');
INSERT INTO `menu` VALUES (4, '用户管理', 2, 1, NULL, '/power/user/users?method=select');
INSERT INTO `menu` VALUES (5, '角色管理', 2, 1, NULL, '/power/role/roles?method=select');
INSERT INTO `menu` VALUES (6, '菜单管理', 2, 1, NULL, '#');

-- ----------------------------
-- Table structure for middle
-- ----------------------------
DROP TABLE IF EXISTS `middle`;
CREATE TABLE `middle`  (
  `middleid` int NOT NULL AUTO_INCREMENT,
  `roleid` int NULL DEFAULT NULL,
  `menuid` int NULL DEFAULT NULL,
  PRIMARY KEY (`middleid`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 91 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of middle
-- ----------------------------
INSERT INTO `middle` VALUES (1, 1, 1);
INSERT INTO `middle` VALUES (2, 1, 2);
INSERT INTO `middle` VALUES (3, 1, 3);
INSERT INTO `middle` VALUES (4, 1, 4);
INSERT INTO `middle` VALUES (5, 1, 5);
INSERT INTO `middle` VALUES (6, 1, 6);
INSERT INTO `middle` VALUES (24, 4, 1);
INSERT INTO `middle` VALUES (25, 4, 3);
INSERT INTO `middle` VALUES (65, 3, 1);
INSERT INTO `middle` VALUES (66, 3, 3);
INSERT INTO `middle` VALUES (83, 2, 1);
INSERT INTO `middle` VALUES (84, 2, 3);

-- ----------------------------
-- Table structure for role
-- ----------------------------
DROP TABLE IF EXISTS `role`;
CREATE TABLE `role`  (
  `roleid` int NOT NULL AUTO_INCREMENT,
  `rolename` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `rolestate` int NULL DEFAULT NULL COMMENT '0 禁用 1 启用',
  PRIMARY KEY (`roleid`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 16 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of role
-- ----------------------------
INSERT INTO `role` VALUES (1, '管理员', 1);
INSERT INTO `role` VALUES (2, '班主任', 1);
INSERT INTO `role` VALUES (3, '学生', 1);
INSERT INTO `role` VALUES (4, '老师', 0);

-- ----------------------------
-- Table structure for student
-- ----------------------------
DROP TABLE IF EXISTS `student`;
CREATE TABLE `student`  (
  `stuid` int NOT NULL AUTO_INCREMENT,
  `stuname` varchar(5) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `stuno` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `sex` int NULL DEFAULT NULL,
  `phone` varchar(11) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `email` varchar(15) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `registered` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `address` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `profession` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `idnumber` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `politics` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `regdate` date NULL DEFAULT NULL,
  `state` int NULL DEFAULT NULL,
  `introduction` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `gid` int NULL DEFAULT NULL,
  PRIMARY KEY (`stuid`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 18 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of student
-- ----------------------------
INSERT INTO `student` VALUES (1, '张三1', 'stu1001', 0, '13719203921', '1233253@qq.com', '北京', '昌平区XXX镇', '物理', '11091211029121212', '党员', '2020-06-12', 4, '优秀学员1', 1);
INSERT INTO `student` VALUES (2, '李四4', 'stu1002', 1, '13719203421', '121253@qq.com', '上海', 'XXX区', '化学', '45691211029121212', '党员', '2020-05-03', 4, '优秀学员2', 1);
INSERT INTO `student` VALUES (3, '王五22', 'stu1003', 1, '13715203921', '2321253@qq.com', '杭州', 'XXX区', '生物', '32291211029121212', '党员', '2020-04-04', 1, '优秀学员3', 2);
INSERT INTO `student` VALUES (4, '赵六', 'stu1004', 1, '13716203921', '35463253@qq.com', '四川', 'XXX区', '英语', '33391211029121212', '群众', '2020-03-10', 1, '优秀学员4', 2);
INSERT INTO `student` VALUES (5, '李磊', 'stu1005', 0, '18719203921', '65765553@qq.com', '湖南', 'XXX区', '医学', '222291211029121212', '群众', '2020-02-18', 1, '优秀学员5', 3);
INSERT INTO `student` VALUES (6, '韩梅梅', 'stu1006', 0, '13719673921', '54654653@qq.com', '武汉', 'XXX区', '政治', '242291211029121212', '群众', '2020-01-17', 4, '优秀学员6', 3);
INSERT INTO `student` VALUES (7, '斯蒂文', 'stu1007', 0, '13743203921', '43532253@qq.com', '天津', 'XXX区', '计算机', '22091211029121212', '群众', '2020-07-18', 4, '优秀学员7', 3);
INSERT INTO `student` VALUES (11, '杨11', 's1010', 1, '13333333333', '1332@126.com', '北京', '朝阳', 'java', '11011111', '党员', '2020-11-29', 1, '一个新开辟领域的探讨，探讨摸索', 1);
INSERT INTO `student` VALUES (12, '杨XX', 's1020', 1, '13333333333', '1332@126.com', '北京', '朝阳', 'java', '11011111111', '党员', '2020-11-30', 1, '一个新开辟领域的探讨，探讨摸索', 1);
INSERT INTO `student` VALUES (13, '杨XX', 's1020', 1, '13333333333', '1332@126.com', '北京', '朝阳', 'java', '1101111111', '党员', '2020-11-30', 1, '一个新开辟领域的探讨，探讨摸索', 1);
INSERT INTO `student` VALUES (15, '杨Xa', 's1111', 1, '13333333333', '1332@126.com', '北京', '朝阳', 'java', '11011111111', '党员', '2020-11-30', 1, '一个新开辟领域的探讨，探讨摸索', 1);
INSERT INTO `student` VALUES (16, '杨aa', 's1111', 1, '13333333333', '1332@126.com', '北京', '朝阳', 'java', '110111111', '党员', '2020-11-30', 1, '一个新开辟领域的探讨，探讨摸索', 1);
INSERT INTO `student` VALUES (17, '杨q', 's1113', 1, '13333333333', '1332@126.com', '北京1', '朝阳', 'java', '11011111', '党员', '2020-11-30', 4, '一个新开辟领域的探讨，探讨摸索', 1);
INSERT INTO `student` VALUES (19, '阿斯顿发', '阿斯顿发', 0, '阿斯顿发', '阿斯顿发', '阿斯顿发', '阿斯顿发', '阿斯顿发', '阿斯顿发', '阿斯顿发', NULL, NULL, NULL, NULL);

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user`  (
  `username` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `password` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES ('admin', '123456');

-- ----------------------------
-- Table structure for users
-- ----------------------------
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users`  (
  `userid` int NOT NULL AUTO_INCREMENT,
  `loginname` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `password` varchar(12) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `realname` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `sex` int NULL DEFAULT NULL,
  `email` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `address` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `phone` varchar(12) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `cardid` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `desc` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `roleid` int NULL DEFAULT NULL,
  PRIMARY KEY (`userid`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 7 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of users
-- ----------------------------
INSERT INTO `users` VALUES (1, 'admin', '123456', '张三', 1, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `users` VALUES (2, 'user1', '123456', '李四', 1, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `users` VALUES (3, 'user2', '123456', '王五', 0, NULL, NULL, NULL, NULL, NULL, 2);
INSERT INTO `users` VALUES (4, 'aaa', '111', 'a', NULL, NULL, NULL, NULL, NULL, NULL, 3);
INSERT INTO `users` VALUES (5, 'bb', '111', 'b', NULL, NULL, NULL, NULL, NULL, NULL, 3);
INSERT INTO `users` VALUES (6, 'cc', '111', 'c', NULL, NULL, NULL, NULL, NULL, NULL, 3);

SET FOREIGN_KEY_CHECKS = 1;
