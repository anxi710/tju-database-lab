CREATE TABLE `takeout`.`user`  (
  `uid` int(8) ZEROFILL NOT NULL AUTO_INCREMENT,
  `username` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `telephone` bigint(11) ZEROFILL NOT NULL,
  `password` varchar(12) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  PRIMARY KEY (`uid`, `telephone`)
);

INSERT INTO `takeout`.`user` (`username`, `telephone`, `password`) VALUES ('admin', 18720650883, 'admin');