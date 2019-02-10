DROP TABLE IF EXISTS `customer_review`;
CREATE TABLE `customer_review` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `marketplace` varchar(2) DEFAULT NULL,
  `customer_id` varchar(256) DEFAULT NULL,
  `review_id` varchar(80) DEFAULT NULL,
  `product_id` varchar(80) DEFAULT NULL,
  `product_parent` varchar(80) DEFAULT NULL,
  `product_title` varchar(256) DEFAULT NULL,
  `product_category` varchar(80) DEFAULT NULL,
  `star_rating` int(2) DEFAULT NULL,
  `helpful_votes` int(11) DEFAULT NULL,
  `total_votes` int(11) DEFAULT NULL,
  `vine` tinyint(4) DEFAULT '0',
  `verified_purchase` tinyint(4) DEFAULT '0',
  `review_headline` TINYTEXT DEFAULT NULL,
  `review_body` TEXT DEFAULT NULL,
  `review_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
