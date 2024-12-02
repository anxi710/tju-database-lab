CREATE TABLE `takeout`.`user`  (
  `sex` varchar(5) NOT NULL DEFAULT '',
  `role` varchar(5) NOT NULL,
  `username` varchar(20) NOT NULL,
  `realname` varchar(20) NOT NULL DEFAULT '',
  `telephone` bigint NOT NULL,
  `password` varchar(12) NOT NULL,
  PRIMARY KEY (`username`, `telephone`)
);
