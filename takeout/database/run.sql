CREATE TABLE `takeout`.`user`  (
  `sex` varchar(5) DEFAULT '',
  `role` varchar(5),
  `username` varchar(20) NOT NULL,
  `realname` varchar(20) DEFAULT '',
  `telephone` bigint NOT NULL,
  `password` varchar(12) NOT NULL,
  PRIMARY KEY (`username`, `telephone`)
);

CREATE TABLE `takeout`.`shop`  (
  `name` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL DEFAULT '',
  `address` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL DEFAULT '',
  PRIMARY KEY (`name`)
);

INSERT INTO `takeout`.`shop` VALUES ('豪大大香鸡排', '上海市嘉定区曹安路158号');
INSERT INTO `takeout`.`shop` VALUES ('小麻鲜', '上海市嘉定区曹安路160号');
INSERT INTO `takeout`.`shop` VALUES ('熊大爷现包饺子', '上海市嘉定区曹安路148号');
INSERT INTO `takeout`.`shop` VALUES ('奈哥酸菜鱼', '上海市嘉定区曹安路146号');

CREATE TABLE `takeout`.`food`  (
  `shopName` varchar(255) NOT NULL DEFAULT '',
  `name` varchar(255) NOT NULL DEFAULT '',
  `price` decimal(10, 2) NULL,
  `image` varchar(255) NULL,
  PRIMARY KEY (`name`),
  CONSTRAINT `shopName` FOREIGN KEY (`shopName`) REFERENCES `takeout`.`shop` (`name`)
);

INSERT INTO `takeout`.`food` VALUES ('豪大大香鸡排', '香辣鸡排', 12.00, 'xxx');
INSERT INTO `takeout`.`food` VALUES ('豪大大香鸡排', '原味鸡排', 10.00, 'xxx');
INSERT INTO `takeout`.`food` VALUES ('豪大大香鸡排', '孜然鸡排', 15.00, 'xxx');
INSERT INTO `takeout`.`food` VALUES ('豪大大香鸡排', '可乐鸡排套餐', 21.00, 'xxx');
INSERT INTO `takeout`.`food` VALUES ('豪大大香鸡排', '雪碧鸡排套餐', 20.50, 'xxx');
INSERT INTO `takeout`.`food` VALUES ('豪大大香鸡排', '芬达鸡排套餐', 20.00, 'xxx');
INSERT INTO `takeout`.`food` VALUES ('豪大大香鸡排', '汉堡套餐', 20.00, 'xxx');
INSERT INTO `takeout`.`food` VALUES ('豪大大香鸡排', '鸡排饭', 15.00, 'xxx');
INSERT INTO `takeout`.`food` VALUES ('豪大大香鸡排', '鸡排炒饭', 15.00, 'xxx');
INSERT INTO `takeout`.`food` VALUES ('豪大大香鸡排', '鸡排炒面', 15.00, 'xxx');
INSERT INTO `takeout`.`food` VALUES ('豪大大香鸡排', '鸡排炒粉', 15.00, 'xxx');
INSERT INTO `takeout`.`food` VALUES ('豪大大香鸡排', '鸡排炒河粉', 15.00, 'xxx');

INSERT INTO `takeout`.`food` VALUES ('小麻鲜', '麻辣小龙虾套餐', 30.00, 'xxx');
INSERT INTO `takeout`.`food` VALUES ('小麻鲜', '六素两荤麻辣烫套餐', 20.00, 'xxx');
INSERT INTO `takeout`.`food` VALUES ('小麻鲜', '全家桶麻辣烫套餐', 25.00, 'xxx');
INSERT INTO `takeout`.`food` VALUES ('小麻鲜', '香辣烤鱼饭', 15.00, 'xxx');
INSERT INTO `takeout`.`food` VALUES ('小麻鲜', '麻辣烤鱼饭', 15.00, 'xxx');
INSERT INTO `takeout`.`food` VALUES ('小麻鲜', '酸辣烤鱼饭', 15.00, 'xxx');

INSERT INTO `takeout`.`food` VALUES ('熊大爷现包饺子', '鲜肉饺子', 10.00, 'xxx');
INSERT INTO `takeout`.`food` VALUES ('熊大爷现包饺子', '韭菜鸡蛋饺子', 10.00, 'xxx');
INSERT INTO `takeout`.`food` VALUES ('熊大爷现包饺子', '虾仁饺子', 15.00, 'xxx');
INSERT INTO `takeout`.`food` VALUES ('熊大爷现包饺子', '鲜肉馅饼', 10.00, 'xxx');
INSERT INTO `takeout`.`food` VALUES ('熊大爷现包饺子', '韭菜鸡蛋馅饼', 10.00, 'xxx');
INSERT INTO `takeout`.`food` VALUES ('熊大爷现包饺子', '虾仁馅饼', 15.00, 'xxx');

INSERT INTO `takeout`.`food` VALUES ('奈哥酸菜鱼', '酸菜鱼', 25.00, 'xxx');
INSERT INTO `takeout`.`food` VALUES ('奈哥酸菜鱼', '麻辣鱼', 25.00, 'xxx');
INSERT INTO `takeout`.`food` VALUES ('奈哥酸菜鱼', '酸辣鱼', 25.00, 'xxx');
INSERT INTO `takeout`.`food` VALUES ('奈哥酸菜鱼', '麻辣香锅', 30.00, 'xxx');
INSERT INTO `takeout`.`food` VALUES ('奈哥酸菜鱼', '酸辣香锅', 30.00, 'xxx');
INSERT INTO `takeout`.`food` VALUES ('奈哥酸菜鱼', '麻辣烤鱼', 32.00, 'xxx');
INSERT INTO `takeout`.`food` VALUES ('奈哥酸菜鱼', '酸辣烤鱼', 32.00, 'xxx');

CREATE TABLE `takeout`.`oder`  (
  `orderID` int(10) NOT NULL AUTO_INCREMENT,
  `username` varchar(20) NOT NULL,
  `foodName` varchar(255) NOT NULL,
  `orderPrice` decimal(10, 2) NOT NULL,
  `orderWay` varchar(255) NOT NULL,
  `consName` varchar(255) NOT NULL,
  `consPhone` bigint NOT NULL,
  `consAddress` varchar(255) NOT NULL,
  PRIMARY KEY (`orderID`),
  CONSTRAINT `username` FOREIGN KEY (`username`) REFERENCES `takeout`.`user` (`username`),
  CONSTRAINT `foodName` FOREIGN KEY (`foodName`) REFERENCES `takeout`.`food` (`name`)
);
