/*
 Navicat Premium Data Transfer

 Source Server         : digi kala
 Source Server Type    : MySQL
 Source Server Version : 80030 (8.0.30)
 Source Host           : localhost:3306
 Source Schema         : club

 Target Server Type    : MySQL
 Target Server Version : 80030 (8.0.30)
 File Encoding         : 65001

 Date: 31/08/2026 15:10:44
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for attendance
-- ----------------------------
DROP TABLE IF EXISTS `attendance`;
CREATE TABLE `attendance`  (
  `id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `member_id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `checkin` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `checkout` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of attendance
-- ----------------------------
INSERT INTO `attendance` VALUES ('1', '1', '08:05', '10:09');
INSERT INTO `attendance` VALUES ('10', '10', '7:30', '9:56');
INSERT INTO `attendance` VALUES ('2', '2', '09:03', '11:47');
INSERT INTO `attendance` VALUES ('3', '3', '17:15', '20:01');
INSERT INTO `attendance` VALUES ('4', '4', '17:56', '19:49');
INSERT INTO `attendance` VALUES ('5', '5', '13:16', '15:54');
INSERT INTO `attendance` VALUES ('6', '6', '12:56', '14:59');
INSERT INTO `attendance` VALUES ('7', '7', '21:05', '23:20');
INSERT INTO `attendance` VALUES ('8', '8', '16:45', '19:02');
INSERT INTO `attendance` VALUES ('9', '9', '22:02', '00:02');

-- ----------------------------
-- Table structure for class
-- ----------------------------
DROP TABLE IF EXISTS `class`;
CREATE TABLE `class`  (
  `id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `coach_id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `className` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `capacity` int NOT NULL,
  `dayofWeek` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `starttime` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `endtime` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `price` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of class
-- ----------------------------
INSERT INTO `class` VALUES (' 1', '1', 'بدنسازی', 50, '6', '08:00', '00:00', 5000000);
INSERT INTO `class` VALUES ('2', '2', 'کراس فیت', 30, '3', '10:00', '18:00', 9000000);
INSERT INTO `class` VALUES ('3', '3', 'فیتنس', 56, '5', '08:00', '22:00', 6000000);
INSERT INTO `class` VALUES ('4', '4', 'پاورلیفتینگ', 20, '4', '16:30', '22:00', 8000000);
INSERT INTO `class` VALUES ('5', '5', 'TRX', 70, '4', '07:00', '19:00', 7000000);
INSERT INTO `class` VALUES ('6', '3', 'یوگا', 30, '3', '10:00', '18:00', 4500000);
INSERT INTO `class` VALUES ('7', '6', 'بدنسازی', 20, '3', '08:00', '22:00', 5000000);
INSERT INTO `class` VALUES ('8', '7', 'بوکس', 15, '4', '08:00', '17:00', 7500000);

-- ----------------------------
-- Table structure for classregistration
-- ----------------------------
DROP TABLE IF EXISTS `classregistration`;
CREATE TABLE `classregistration`  (
  `id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `member_id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `class_id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `registerDate` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of classregistration
-- ----------------------------
INSERT INTO `classregistration` VALUES ('1', '1', '1', NULL);
INSERT INTO `classregistration` VALUES ('10', '10', '5', NULL);
INSERT INTO `classregistration` VALUES ('11', '11', '8', NULL);
INSERT INTO `classregistration` VALUES ('12', '12', '8', NULL);
INSERT INTO `classregistration` VALUES ('13', '13', '7', NULL);
INSERT INTO `classregistration` VALUES ('14', '14', '7', NULL);
INSERT INTO `classregistration` VALUES ('2', '2', '2', NULL);
INSERT INTO `classregistration` VALUES ('3', '3', '3', NULL);
INSERT INTO `classregistration` VALUES ('4', '4', '1', NULL);
INSERT INTO `classregistration` VALUES ('5', '5', '2', NULL);
INSERT INTO `classregistration` VALUES ('6', '6', '4', NULL);
INSERT INTO `classregistration` VALUES ('7', '7', '5', NULL);
INSERT INTO `classregistration` VALUES ('8', '8', '3', NULL);
INSERT INTO `classregistration` VALUES ('9', '9', '6', NULL);

-- ----------------------------
-- Table structure for coach
-- ----------------------------
DROP TABLE IF EXISTS `coach`;
CREATE TABLE `coach`  (
  `id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `f_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `l_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `start_date` datetime NOT NULL,
  `speciality` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `salary` int NULL DEFAULT NULL,
  `hire_date` datetime NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of coach
-- ----------------------------
INSERT INTO `coach` VALUES ('1', 'حمید', 'احمدی', '1404-03-03 00:00:00', 'بدنسازی', 19000000, '1404-03-06 00:00:00');
INSERT INTO `coach` VALUES ('2', 'سعید', 'کریمی', '1404-04-01 00:00:00', 'کراس فیت', 22000000, '1404-04-02 00:00:00');
INSERT INTO `coach` VALUES ('3', 'مهدی', 'رضایی', '1404-04-03 00:00:00', 'فیتنس', 26000000, '1404-04-01 00:00:00');
INSERT INTO `coach` VALUES ('4', 'آرمان', 'محمدی', '1404-04-03 00:00:00', 'پاورلیفتینگ', 16000000, '1404-04-06 00:00:00');
INSERT INTO `coach` VALUES ('5', 'رضا', 'اسدی', '1404-04-16 00:00:00', 'TRX', 30000000, '1404-04-20 00:00:00');
INSERT INTO `coach` VALUES ('6', 'علی', 'حسنی', '1404-09-11 00:00:00', 'بدنسازی', 19000000, '1404-09-13 00:00:00');
INSERT INTO `coach` VALUES ('7', 'سعید', 'امیری', '1404-11-12 00:00:00', 'بوکس', 22000000, '1404-11-15 00:00:00');
INSERT INTO `coach` VALUES ('8', 'سهیل', 'بدری', '1404-12-15 00:00:00', 'کراس فیت', 22000000, '1404-12-20 00:00:00');

-- ----------------------------
-- Table structure for dietfood
-- ----------------------------
DROP TABLE IF EXISTS `dietfood`;
CREATE TABLE `dietfood`  (
  `id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `diet_id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `food_id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `mealTime` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `quantity` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of dietfood
-- ----------------------------
INSERT INTO `dietfood` VALUES ('1', '1', '1', 'صبحانه', NULL);
INSERT INTO `dietfood` VALUES ('10', '10', '3', 'شام', NULL);
INSERT INTO `dietfood` VALUES ('2', '1', '5', 'ناهار', NULL);
INSERT INTO `dietfood` VALUES ('3', '2', '6', 'صبحانه', NULL);
INSERT INTO `dietfood` VALUES ('4', '2', '4', 'شام', NULL);
INSERT INTO `dietfood` VALUES ('5', '4', '9', 'عصرانه', NULL);
INSERT INTO `dietfood` VALUES ('6', '5', '2', 'ناهار', NULL);
INSERT INTO `dietfood` VALUES ('7', '6', '8', 'شام', NULL);
INSERT INTO `dietfood` VALUES ('8', '7', '7', 'میان وعده', NULL);
INSERT INTO `dietfood` VALUES ('9', '8', '10', 'صبحانه', NULL);

-- ----------------------------
-- Table structure for dietprogram
-- ----------------------------
DROP TABLE IF EXISTS `dietprogram`;
CREATE TABLE `dietprogram`  (
  `id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `coach_id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `member_id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `startdate` datetime NULL DEFAULT NULL,
  `goal` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of dietprogram
-- ----------------------------
INSERT INTO `dietprogram` VALUES ('1', '1', '1', NULL, 'افزایش حجم');
INSERT INTO `dietprogram` VALUES ('10', '5', '10', NULL, 'کاهش وزن');
INSERT INTO `dietprogram` VALUES ('11', '7', '11', NULL, 'استقامت');
INSERT INTO `dietprogram` VALUES ('12', '7', '12', NULL, 'استقامت');
INSERT INTO `dietprogram` VALUES ('13', '6', '13', NULL, 'افزایش حجم');
INSERT INTO `dietprogram` VALUES ('14', '6', '14', NULL, 'افزیش حجم');
INSERT INTO `dietprogram` VALUES ('2', '1', '2', NULL, 'کاهش وزن');
INSERT INTO `dietprogram` VALUES ('3', '2', '3', NULL, 'افزایش قدرت');
INSERT INTO `dietprogram` VALUES ('4', '3', '4', NULL, 'تناسب اندام');
INSERT INTO `dietprogram` VALUES ('5', '2', '5', NULL, 'چربی سوزی');
INSERT INTO `dietprogram` VALUES ('6', '4', '6', NULL, 'افزایش حجم');
INSERT INTO `dietprogram` VALUES ('7', '5', '7', NULL, 'استفامت');
INSERT INTO `dietprogram` VALUES ('8', '3', '8', NULL, 'فیتنس');
INSERT INTO `dietprogram` VALUES ('9', '4', '9', NULL, 'عضله سازی');

-- ----------------------------
-- Table structure for employee
-- ----------------------------
DROP TABLE IF EXISTS `employee`;
CREATE TABLE `employee`  (
  `emp_id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `F_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `L_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `phone` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `Position` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `salary` float(16, 2) NULL DEFAULT NULL,
  `hire.date` datetime NULL DEFAULT NULL,
  PRIMARY KEY (`emp_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of employee
-- ----------------------------
INSERT INTO `employee` VALUES ('1', 'علی', 'کاظمی', NULL, 'پذیرش', NULL, NULL);
INSERT INTO `employee` VALUES ('10', 'نیما', 'احمدی', NULL, 'پذیرش', NULL, NULL);
INSERT INTO `employee` VALUES ('2', 'رضا', 'حسینی', NULL, 'حسابدار', NULL, NULL);
INSERT INTO `employee` VALUES ('3', 'محمد', 'اکبری', NULL, 'پذیرش', NULL, NULL);
INSERT INTO `employee` VALUES ('4', 'مهدی', 'رحیمی', NULL, 'مدیر', NULL, NULL);
INSERT INTO `employee` VALUES ('5', 'امیر', 'محمدی', NULL, 'پذیرش', NULL, NULL);
INSERT INTO `employee` VALUES ('6', 'حسین', 'کریمی', NULL, 'نظافت', NULL, NULL);
INSERT INTO `employee` VALUES ('7', 'سعید', 'اسدی', NULL, 'پذیرش', NULL, NULL);
INSERT INTO `employee` VALUES ('8', 'آرش', 'قاسمی', NULL, 'مدیر', NULL, NULL);
INSERT INTO `employee` VALUES ('9', 'پویا', 'نادری', NULL, 'حسابدار', NULL, NULL);

-- ----------------------------
-- Table structure for equipment
-- ----------------------------
DROP TABLE IF EXISTS `equipment`;
CREATE TABLE `equipment`  (
  `id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `equipmentName` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Purchase_date` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `status` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of equipment
-- ----------------------------
INSERT INTO `equipment` VALUES ('1', 'تردمیل', NULL, 'سالم');
INSERT INTO `equipment` VALUES ('10', 'دستگاه شکم', NULL, 'سالم');
INSERT INTO `equipment` VALUES ('2', 'دوچرخه ثابت', NULL, 'سالم');
INSERT INTO `equipment` VALUES ('3', 'پرس سینه', NULL, 'نیاز به سرویس');
INSERT INTO `equipment` VALUES ('4', 'لت', NULL, 'سالم');
INSERT INTO `equipment` VALUES ('5', 'اسکوات رک', NULL, 'سالم');
INSERT INTO `equipment` VALUES ('6', 'دمبل', NULL, 'سالم');
INSERT INTO `equipment` VALUES ('7', 'هالتر', NULL, 'سالم');
INSERT INTO `equipment` VALUES ('8', 'کراس اوور', NULL, 'خراب');
INSERT INTO `equipment` VALUES ('9', 'پرس پا', NULL, 'سالم');

-- ----------------------------
-- Table structure for equipmentmaintance
-- ----------------------------
DROP TABLE IF EXISTS `equipmentmaintance`;
CREATE TABLE `equipmentmaintance`  (
  `id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `EQuipmentID` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `serviceDate` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `description` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `cost` float(12, 2) NOT NULL,
  `NextServiceDate` datetime NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of equipmentmaintance
-- ----------------------------
INSERT INTO `equipmentmaintance` VALUES ('1', '3', '2026/01/10', NULL, 900000.00, NULL);
INSERT INTO `equipmentmaintance` VALUES ('10', '10', '2026/06/01', NULL, 400000.00, NULL);
INSERT INTO `equipmentmaintance` VALUES ('2', '8', '2026/01/15', NULL, 1500000.00, NULL);
INSERT INTO `equipmentmaintance` VALUES ('3', '1', '2026/02/10', NULL, 600000.00, NULL);
INSERT INTO `equipmentmaintance` VALUES ('4', '5', '2026/02/20', NULL, 500000.00, NULL);
INSERT INTO `equipmentmaintance` VALUES ('5', '9', '2026/03/01', NULL, 700000.00, NULL);
INSERT INTO `equipmentmaintance` VALUES ('6', '2', '2026/03/15', NULL, 450000.00, NULL);
INSERT INTO `equipmentmaintance` VALUES ('7', '6', '2026/04/10', NULL, 300000.00, NULL);
INSERT INTO `equipmentmaintance` VALUES ('8', '4', '2026/05/01', NULL, 650000.00, NULL);
INSERT INTO `equipmentmaintance` VALUES ('9', '7', '2026/05/20', NULL, 350000.00, NULL);

-- ----------------------------
-- Table structure for exercise
-- ----------------------------
DROP TABLE IF EXISTS `exercise`;
CREATE TABLE `exercise`  (
  `id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `exerciseName` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `muscleGroup` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Description` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of exercise
-- ----------------------------
INSERT INTO `exercise` VALUES ('1', 'پرس سینه', 'سینه', NULL);
INSERT INTO `exercise` VALUES ('10', 'ساق پا', 'پا', NULL);
INSERT INTO `exercise` VALUES ('2', 'اسکوات', 'پا', NULL);
INSERT INTO `exercise` VALUES ('3', 'ددلیفت', 'پشت', NULL);
INSERT INTO `exercise` VALUES ('4', 'جلوبازو', 'بازو', NULL);
INSERT INTO `exercise` VALUES ('5', 'پشت بازو', 'بازو', NULL);
INSERT INTO `exercise` VALUES ('6', 'پرس سرشانه', 'سرشانه', NULL);
INSERT INTO `exercise` VALUES ('7', 'بارفیکس', 'پشت', NULL);
INSERT INTO `exercise` VALUES ('8', 'کرانچ', 'شکم', NULL);
INSERT INTO `exercise` VALUES ('9', 'لانچ', 'پا', NULL);

-- ----------------------------
-- Table structure for food
-- ----------------------------
DROP TABLE IF EXISTS `food`;
CREATE TABLE `food`  (
  `id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `foodName` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Calories` int NOT NULL,
  `Protein` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `Carbohydrate` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `Fat` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of food
-- ----------------------------
INSERT INTO `food` VALUES ('1', 'سینه مرغ', 165, '31', NULL, NULL);
INSERT INTO `food` VALUES ('10', 'بادام', 576, '21', NULL, NULL);
INSERT INTO `food` VALUES ('2', 'برنج', 130, '2', NULL, NULL);
INSERT INTO `food` VALUES ('3', 'تخم مرغ', 155, '13', NULL, NULL);
INSERT INTO `food` VALUES ('4', 'ماهی', 206, '22', NULL, NULL);
INSERT INTO `food` VALUES ('5', 'جودوسر', 389, '17', NULL, NULL);
INSERT INTO `food` VALUES ('6', 'سیب', 52, '0', NULL, NULL);
INSERT INTO `food` VALUES ('7', 'موز', 89, '1', NULL, NULL);
INSERT INTO `food` VALUES ('8', 'گوشت گوساله', 250, '26', NULL, NULL);
INSERT INTO `food` VALUES ('9', 'ماست یونانی', 59, '10', NULL, NULL);

-- ----------------------------
-- Table structure for invoice
-- ----------------------------
DROP TABLE IF EXISTS `invoice`;
CREATE TABLE `invoice`  (
  `id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `member_id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `payment_id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `invoiceDate` datetime NULL DEFAULT NULL,
  `TotalPrice` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of invoice
-- ----------------------------
INSERT INTO `invoice` VALUES ('1', '1', '1', NULL, 15000000);
INSERT INTO `invoice` VALUES ('10', '10', '10', NULL, 120000000);
INSERT INTO `invoice` VALUES ('2', '2', '2', NULL, 40000000);
INSERT INTO `invoice` VALUES ('3', '3', '3', NULL, 70000000);
INSERT INTO `invoice` VALUES ('4', '4', '4', NULL, 15000000);
INSERT INTO `invoice` VALUES ('5', '5', '5', NULL, 40000000);
INSERT INTO `invoice` VALUES ('6', '6', '6', NULL, 120000000);
INSERT INTO `invoice` VALUES ('7', '7', '7', NULL, 15000000);
INSERT INTO `invoice` VALUES ('8', '8', '8', NULL, 70000000);
INSERT INTO `invoice` VALUES ('9', '9', '9', NULL, 40000000);

-- ----------------------------
-- Table structure for locker
-- ----------------------------
DROP TABLE IF EXISTS `locker`;
CREATE TABLE `locker`  (
  `id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `lockernumber` int NOT NULL,
  `status` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of locker
-- ----------------------------
INSERT INTO `locker` VALUES ('1', 101, 'سالم ');
INSERT INTO `locker` VALUES ('10', 110, 'سالم ');
INSERT INTO `locker` VALUES ('11', 111, 'سالم ');
INSERT INTO `locker` VALUES ('12', 112, 'سالم ');
INSERT INTO `locker` VALUES ('13', 113, 'سالم ');
INSERT INTO `locker` VALUES ('14', 114, 'سالم ');
INSERT INTO `locker` VALUES ('15', 115, 'سالم ');
INSERT INTO `locker` VALUES ('16', 116, 'سالم ');
INSERT INTO `locker` VALUES ('17', 117, 'سالم ');
INSERT INTO `locker` VALUES ('18', 118, 'سالم ');
INSERT INTO `locker` VALUES ('19', 119, 'سالم ');
INSERT INTO `locker` VALUES ('2', 102, 'سالم ');
INSERT INTO `locker` VALUES ('20', 120, 'نیاز به تعمیر');
INSERT INTO `locker` VALUES ('21', 121, 'نیاز به تعمیر');
INSERT INTO `locker` VALUES ('22', 122, 'سالم ');
INSERT INTO `locker` VALUES ('23', 123, 'سالم ');
INSERT INTO `locker` VALUES ('24', 124, 'سالم ');
INSERT INTO `locker` VALUES ('25', 125, 'سالم ');
INSERT INTO `locker` VALUES ('3', 103, 'سالم ');
INSERT INTO `locker` VALUES ('4', 104, 'سالم ');
INSERT INTO `locker` VALUES ('5', 105, 'سالم ');
INSERT INTO `locker` VALUES ('6', 106, 'سالم ');
INSERT INTO `locker` VALUES ('7', 107, 'سالم ');
INSERT INTO `locker` VALUES ('8', 108, 'سالم ');
INSERT INTO `locker` VALUES ('9', 109, 'سالم ');

-- ----------------------------
-- Table structure for member
-- ----------------------------
DROP TABLE IF EXISTS `member`;
CREATE TABLE `member`  (
  `id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Fname` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Lname` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `startDate` datetime NOT NULL,
  `gender` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `phone` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `status` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of member
-- ----------------------------
INSERT INTO `member` VALUES ('1', 'علی', 'احمدی', '1404-04-03 00:00:00', 'male', '09121111111', 'فعال');
INSERT INTO `member` VALUES ('10', 'نیما', 'اکبری', '1404-04-16 00:00:00', 'male', '09121111111', 'فعال');
INSERT INTO `member` VALUES ('11', 'علی', 'حامدی', '1405-02-11 00:00:00', 'male', '09145555555', 'فعال');
INSERT INTO `member` VALUES ('12', 'حسن', 'حامدی', '1404-12-20 00:00:00', 'male', '09142523691', 'فعال');
INSERT INTO `member` VALUES ('13', 'مهرداد', 'عبدللهیان', '1404-11-29 00:00:00', 'male', '09143333333', 'فعال');
INSERT INTO `member` VALUES ('14', 'مهدی', 'آستانه ای ', '1405-01-12 00:00:00', 'male', '09142222222', 'فعال');
INSERT INTO `member` VALUES ('2', 'رضا', 'کریمی', '1404-04-01 00:00:00', 'male', '09123333333', 'فعال');
INSERT INTO `member` VALUES ('3', 'محمد', 'حسینی', '1404-04-03 00:00:00', 'male', '09124444444', 'فعال');
INSERT INTO `member` VALUES ('4', 'امیر', 'رضایی', '1404-04-03 00:00:00', 'male', '09125555555', 'فعال');
INSERT INTO `member` VALUES ('5', 'سجاد', 'محمدی', '1404-02-03 00:00:00', 'male', '09126666666', 'فعال');
INSERT INTO `member` VALUES ('6', 'حسین', 'رحیمی', '1404-01-03 00:00:00', 'male', '09127777777', 'فعال');
INSERT INTO `member` VALUES ('7', 'مهدی', 'اسدی', '1404-04-03 00:00:00', 'male', '09128888888', 'فعال');
INSERT INTO `member` VALUES ('8', 'مهدی', 'اباذری', '1404-03-05 00:00:00', 'male', '09135555555', 'فعال');
INSERT INTO `member` VALUES ('9', 'آرش', 'نادری', '1404-04-15 00:00:00', 'male', '09129999999', 'فعال');

-- ----------------------------
-- Table structure for memberlocker
-- ----------------------------
DROP TABLE IF EXISTS `memberlocker`;
CREATE TABLE `memberlocker`  (
  `id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `member_id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `locker_id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `startdate` datetime NULL DEFAULT NULL,
  `enddate` datetime NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of memberlocker
-- ----------------------------
INSERT INTO `memberlocker` VALUES ('1', '1', '1', '2026-02-01 00:00:00', '2026-04-01 00:00:00');
INSERT INTO `memberlocker` VALUES ('10', '10', '10', '2026-06-01 00:00:00', '2026-09-01 00:00:00');
INSERT INTO `memberlocker` VALUES ('11', '11', '11', '2026-05-05 00:00:00', '2026-06-04 00:00:00');
INSERT INTO `memberlocker` VALUES ('12', '12', '12', '2026-08-01 00:00:00', '2026-09-01 00:00:00');
INSERT INTO `memberlocker` VALUES ('13', '13', '13', '2026-07-01 00:00:00', '2026-10-01 00:00:00');
INSERT INTO `memberlocker` VALUES ('2', '2', '2', '2026-03-01 00:00:00', '2026-06-01 00:00:00');
INSERT INTO `memberlocker` VALUES ('3', '3', '3', '2026-04-01 00:00:00', '2026-10-01 00:00:00');
INSERT INTO `memberlocker` VALUES ('4', '4', '4', '2026-01-02 00:00:00', '2026-04-01 00:00:00');
INSERT INTO `memberlocker` VALUES ('5', '5', '5', '2026-02-05 00:00:00', '2026-04-05 00:00:00');
INSERT INTO `memberlocker` VALUES ('6', '6', '6', '2026-03-03 00:00:00', '2026-09-03 00:00:00');
INSERT INTO `memberlocker` VALUES ('7', '7', '7', '2026-03-10 00:00:00', '2026-06-09 00:00:00');
INSERT INTO `memberlocker` VALUES ('8', '8', '8', '2026-01-01 00:00:00', '2027-01-01 00:00:00');
INSERT INTO `memberlocker` VALUES ('9', '9', '9', '2026-02-02 00:00:00', '2026-08-02 00:00:00');

-- ----------------------------
-- Table structure for membership
-- ----------------------------
DROP TABLE IF EXISTS `membership`;
CREATE TABLE `membership`  (
  `id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `member_id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `plan_id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `startdate` datetime NOT NULL,
  `enddate` datetime NOT NULL,
  `status` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of membership
-- ----------------------------
INSERT INTO `membership` VALUES ('1', '1', '1', '2026-01-01 00:00:00', '2026-01-31 00:00:00', 'فعال');
INSERT INTO `membership` VALUES ('10', '10', '4', '2026-03-01 00:00:00', '2027-02-28 00:00:00', 'فعال');
INSERT INTO `membership` VALUES ('11', '11', '1', '2026-01-02 00:00:00', '2026-02-01 00:00:00', 'فعال');
INSERT INTO `membership` VALUES ('12', '12', '2', '2026-01-01 00:00:00', '2026-03-01 00:00:00', 'فعال');
INSERT INTO `membership` VALUES ('13', '13', '3', '2026-01-01 00:00:00', '2026-06-30 00:00:00', 'فعال');
INSERT INTO `membership` VALUES ('14', '14', '4', '2026-01-01 00:00:00', '2027-01-01 00:00:00', 'فعال');
INSERT INTO `membership` VALUES ('2', '2', '2', '2026-01-01 00:00:00', '2026-03-31 00:00:00', 'فعال');
INSERT INTO `membership` VALUES ('3', '3', '3', '2026-01-01 00:00:00', '2026-06-30 00:00:00', 'فعال');
INSERT INTO `membership` VALUES ('4', '4', '1', '2026-01-01 00:00:00', '2026-01-31 00:00:00', 'فعال');
INSERT INTO `membership` VALUES ('5', '5', '2', '2026-02-01 00:00:00', '2026-04-30 00:00:00', 'فعال');
INSERT INTO `membership` VALUES ('6', '6', '4', '2026-02-01 00:00:00', '2027-01-31 00:00:00', 'فعال');
INSERT INTO `membership` VALUES ('7', '7', '1', '2026-03-01 00:00:00', '2026-03-31 00:00:00', 'فعال');
INSERT INTO `membership` VALUES ('8', '8', '3', '2026-03-01 00:00:00', '2026-08-31 00:00:00', 'فعال');
INSERT INTO `membership` VALUES ('9', '9', '2', '2026-06-20 00:00:00', '2026-08-21 00:00:00', 'فعال');

-- ----------------------------
-- Table structure for membership_plan
-- ----------------------------
DROP TABLE IF EXISTS `membership_plan`;
CREATE TABLE `membership_plan`  (
  `id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `plan_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `duration` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `price` int NOT NULL,
  `description` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of membership_plan
-- ----------------------------
INSERT INTO `membership_plan` VALUES ('1', 'یکماهه', '1', 15000000, NULL);
INSERT INTO `membership_plan` VALUES ('2', 'سه ماه', '3', 40000000, NULL);
INSERT INTO `membership_plan` VALUES ('3', 'شش ماهه', '6', 70000000, NULL);
INSERT INTO `membership_plan` VALUES ('4', 'یکساله', '12', 120000000, NULL);

-- ----------------------------
-- Table structure for payment
-- ----------------------------
DROP TABLE IF EXISTS `payment`;
CREATE TABLE `payment`  (
  `id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `membership_id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `amount` int NOT NULL,
  `paymentdate` datetime NOT NULL,
  `paymentmethode` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `status` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of payment
-- ----------------------------
INSERT INTO `payment` VALUES ('1', '1', 15000000, '2026-01-05 00:00:00', 'card', 'موفق');
INSERT INTO `payment` VALUES ('10', '10', 120000000, '2026-03-05 00:00:00', 'card', 'موفق');
INSERT INTO `payment` VALUES ('2', '2', 40000000, '2026-01-08 00:00:00', 'cash', 'ناموفق');
INSERT INTO `payment` VALUES ('3', '3', 70000000, '2026-01-10 00:00:00', 'card', 'موفق');
INSERT INTO `payment` VALUES ('4', '4', 15000000, '2026-01-15 00:00:00', 'card', 'موفق');
INSERT INTO `payment` VALUES ('5', '5', 40000000, '2026-02-01 00:00:00', 'card', 'موفق');
INSERT INTO `payment` VALUES ('6', '6', 120000000, '2026-02-05 00:00:00', 'cash', 'موفق');
INSERT INTO `payment` VALUES ('7', '7', 15000000, '2026-02-10 00:00:00', 'card', 'موفق');
INSERT INTO `payment` VALUES ('8', '8', 70000000, '2026-02-15 00:00:00', 'card', 'موفق');
INSERT INTO `payment` VALUES ('9', '9', 40000000, '2026-03-01 00:00:00', 'cash', 'موفق');

-- ----------------------------
-- Table structure for programexercise
-- ----------------------------
DROP TABLE IF EXISTS `programexercise`;
CREATE TABLE `programexercise`  (
  `id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `program_id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `exercise_id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `sets` int NOT NULL,
  `reps` int NOT NULL,
  `resttime` datetime NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of programexercise
-- ----------------------------
INSERT INTO `programexercise` VALUES ('1', '1', '1', 4, 10, NULL);
INSERT INTO `programexercise` VALUES ('10', '5', '10', 4, 10, NULL);
INSERT INTO `programexercise` VALUES ('2', '1', '4', 3, 12, NULL);
INSERT INTO `programexercise` VALUES ('3', '2', '2', 4, 15, NULL);
INSERT INTO `programexercise` VALUES ('4', '3', '3', 5, 5, NULL);
INSERT INTO `programexercise` VALUES ('5', '4', '6', 4, 10, NULL);
INSERT INTO `programexercise` VALUES ('6', '5', '8', 3, 20, NULL);
INSERT INTO `programexercise` VALUES ('7', '6', '7', 4, 8, NULL);
INSERT INTO `programexercise` VALUES ('8', '7', '9', 3, 12, NULL);
INSERT INTO `programexercise` VALUES ('9', '8', '10', 5, 15, NULL);

-- ----------------------------
-- Table structure for workoutprogram
-- ----------------------------
DROP TABLE IF EXISTS `workoutprogram`;
CREATE TABLE `workoutprogram`  (
  `id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `coach_id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `member_id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `programName` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `createDate` datetime NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of workoutprogram
-- ----------------------------
INSERT INTO `workoutprogram` VALUES ('1', '1', '1', 'حجم', NULL);
INSERT INTO `workoutprogram` VALUES ('10', '5', '10', 'ترکیبی', NULL);
INSERT INTO `workoutprogram` VALUES ('2', '2', '2', 'چربی سوزی', NULL);
INSERT INTO `workoutprogram` VALUES ('3', '3', '3', 'قدرت', NULL);
INSERT INTO `workoutprogram` VALUES ('4', '1', '4', 'فینس', NULL);
INSERT INTO `workoutprogram` VALUES ('5', '2', '5', 'افزایش وزن', NULL);
INSERT INTO `workoutprogram` VALUES ('6', '4', '6', 'پاور', NULL);
INSERT INTO `workoutprogram` VALUES ('7', '5', '7', 'TRX', NULL);
INSERT INTO `workoutprogram` VALUES ('8', '3', '8', 'استقامت', NULL);
INSERT INTO `workoutprogram` VALUES ('9', '4', '9', 'حرفه ای', NULL);

SET FOREIGN_KEY_CHECKS = 1;
