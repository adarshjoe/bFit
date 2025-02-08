/*
SQLyog Community Edition- MySQL GUI v8.03 
MySQL - 5.6.12-log : Database - fitness
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`fitness` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `fitness`;

/*Table structure for table `allocate_user` */

DROP TABLE IF EXISTS `allocate_user`;

CREATE TABLE `allocate_user` (
  `allocation_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `batch_id` int(11) DEFAULT NULL,
  `instructor_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`allocation_id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

/*Data for the table `allocate_user` */

insert  into `allocate_user`(`allocation_id`,`user_id`,`batch_id`,`instructor_id`) values (1,1,1,2),(4,15,3,3),(5,19,1,1),(6,18,2,1),(7,17,2,2),(8,21,3,4),(9,13,2,6),(10,13,3,23),(11,14,2,23),(12,3,1,1);

/*Table structure for table `applicants` */

DROP TABLE IF EXISTS `applicants`;

CREATE TABLE `applicants` (
  `applicant_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `competition_id` int(11) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`applicant_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `applicants` */

insert  into `applicants`(`applicant_id`,`user_id`,`competition_id`,`date`,`status`) values (2,3,2,'2023-03-13','approved'),(3,3,3,'2023-03-13','approved'),(4,3,4,'2023-03-13','rejected');

/*Table structure for table `appointment` */

DROP TABLE IF EXISTS `appointment`;

CREATE TABLE `appointment` (
  `appointment_id` int(11) NOT NULL AUTO_INCREMENT,
  `date` varchar(50) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `schedule_id` int(11) DEFAULT NULL,
  `token_no` int(11) DEFAULT NULL,
  PRIMARY KEY (`appointment_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

/*Data for the table `appointment` */

insert  into `appointment`(`appointment_id`,`date`,`user_id`,`schedule_id`,`token_no`) values (1,'2023-02-27',15,2,1),(2,'2023-02-27',14,2,2),(3,'2023-02-27',14,2,3),(4,'2023-02-27',13,2,4),(5,'2023-02-27',16,4,5),(6,'2023-02-28',17,2,5),(7,'2023-02-28',19,2,6),(8,'2023-03-06',3,3,1),(9,'2023-03-06',3,4,6),(10,'2023-03-06',3,6,1);

/*Table structure for table `attendance` */

DROP TABLE IF EXISTS `attendance`;

CREATE TABLE `attendance` (
  `attendance_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  `check_in` varchar(50) DEFAULT NULL,
  `check_out` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`attendance_id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;

/*Data for the table `attendance` */

insert  into `attendance`(`attendance_id`,`user_id`,`date`,`check_in`,`check_out`) values (1,1,'13-2-2023','12:00','3:00'),(2,2,'13-2-2023','2:00','4:00'),(7,0,NULL,'10:00','11:00'),(8,0,NULL,'ljh','bvn'),(9,3,'2023-02-13','12:48:36','12:49:02'),(10,5,'2023-02-20','14:27:03','pending'),(11,1,'2023-02-25','19:29:03','pending'),(12,17,'2023-03-06','10:59:28','pending'),(13,17,'2023-03-07','15:21:26','15:28:00'),(14,1,'2023-03-07','15:21:36','15:27:05');

/*Table structure for table `bank` */

DROP TABLE IF EXISTS `bank`;

CREATE TABLE `bank` (
  `bank_id` int(11) NOT NULL AUTO_INCREMENT,
  `bank_name` varchar(100) DEFAULT NULL,
  `account_no` varchar(100) DEFAULT NULL,
  `ifsc` varchar(100) DEFAULT NULL,
  `balance` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`bank_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `bank` */

insert  into `bank`(`bank_id`,`bank_name`,`account_no`,`ifsc`,`balance`) values (1,'SBI','5455612','52524','11000'),(2,'FEDERAL','12345','123','500'),(3,'AXIS','123456','1234','49620');

/*Table structure for table `batches` */

DROP TABLE IF EXISTS `batches`;

CREATE TABLE `batches` (
  `batch_id` int(11) NOT NULL AUTO_INCREMENT,
  `date_of_join` varchar(50) DEFAULT NULL,
  `time_from` varchar(50) DEFAULT NULL,
  `time_to` varchar(50) DEFAULT NULL,
  `batch_name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`batch_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `batches` */

insert  into `batches`(`batch_id`,`date_of_join`,`time_from`,`time_to`,`batch_name`) values (1,'2022','21/1/2022','25/1/2023','Morning'),(2,'2022','21/12/2022','21/1/2023','Evening'),(3,'2023','8/1/2002','5/8/2022','Afternnon'),(4,'2023-03-09','08:40','10:40','Evening'),(5,'2023-03-09','18:49','20:49','morning'),(6,'2023-03-08','16:57','17:56','morning');

/*Table structure for table `booking` */

DROP TABLE IF EXISTS `booking`;

CREATE TABLE `booking` (
  `booking_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `physician_id` int(11) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `amount` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`booking_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

/*Data for the table `booking` */

insert  into `booking`(`booking_id`,`user_id`,`physician_id`,`date`,`amount`,`status`) values (1,17,7,'2023-02-28','0','add_to_cart'),(2,17,8,'2023-02-28','0','add_to_cart'),(3,15,7,'2023-02-28','0','add_to_cart'),(4,15,8,'2023-02-28','0','add_to_cart'),(5,19,7,'2023-02-28','0','add_to_cart'),(6,3,7,'2023-03-06','0','Paid'),(7,3,8,'2023-03-07','0','Paid'),(8,3,7,'2023-03-07','45.0','Paid'),(9,3,8,'2023-03-07','45.0','Paid');

/*Table structure for table `booking_sub` */

DROP TABLE IF EXISTS `booking_sub`;

CREATE TABLE `booking_sub` (
  `sub_id` int(11) NOT NULL AUTO_INCREMENT,
  `booking_id` int(11) DEFAULT NULL,
  `medicine_id` int(11) DEFAULT NULL,
  `quantity` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`sub_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

/*Data for the table `booking_sub` */

insert  into `booking_sub`(`sub_id`,`booking_id`,`medicine_id`,`quantity`) values (2,1,1,'2'),(3,2,1,'3'),(4,3,1,'5'),(5,4,1,'10'),(6,5,1,'34'),(7,6,1,'25'),(8,7,1,'4'),(9,8,1,'6'),(10,9,2,'5');

/*Table structure for table `chat` */

DROP TABLE IF EXISTS `chat`;

CREATE TABLE `chat` (
  `chat_id` int(11) NOT NULL AUTO_INCREMENT,
  `from_id` int(11) DEFAULT NULL,
  `to_id` int(11) DEFAULT NULL,
  `message` varchar(200) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`chat_id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;

/*Data for the table `chat` */

insert  into `chat`(`chat_id`,`from_id`,`to_id`,`message`,`date`) values (1,8,16,'hy','2023-02-28'),(2,16,8,'how are you?','2023-02-28'),(3,16,16,'haii','2023-02-28'),(4,16,16,'how are you','2023-02-28'),(5,15,15,'haii','2023-02-28'),(6,17,17,'haii','2023-02-28'),(7,17,11,'hy','2023-02-28'),(8,11,17,'hello','2023-02-28'),(9,NULL,17,NULL,NULL),(10,19,11,'ji','2023-02-28'),(11,8,16,'haii','2023-03-01'),(12,3,8,'haii','2023-03-06'),(13,8,3,'hello','2023-03-06'),(14,8,3,'uuuh','2023-03-06'),(15,3,22,'haii','2023-03-06'),(16,22,3,'hello','2023-03-06'),(17,3,22,'can i change the booking ','2023-03-06'),(18,22,3,'yes but you will get the last token number','2023-03-06');

/*Table structure for table `competition` */

DROP TABLE IF EXISTS `competition`;

CREATE TABLE `competition` (
  `competition_id` int(11) NOT NULL AUTO_INCREMENT,
  `competition_name` varchar(50) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  `details` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`competition_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `competition` */

insert  into `competition`(`competition_id`,`competition_name`,`date`,`details`) values (2,'deadlift','2023-03-01','kannur '),(3,'WEIGHT','2023-03-02','MALLAPURAM'),(4,'PULLUP','2023-03-02','IRITTY');

/*Table structure for table `complaints` */

DROP TABLE IF EXISTS `complaints`;

CREATE TABLE `complaints` (
  `complaint_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(50) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  `complaint` varchar(50) DEFAULT NULL,
  `reply` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`complaint_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `complaints` */

insert  into `complaints`(`complaint_id`,`user_id`,`date`,`complaint`,`reply`) values (1,1,'12/12/2022','bad response','pending'),(3,15,'2023-02-27','hjgfjjvvjvnmvnvnmv','pending'),(4,15,'2023-02-27','cbcgcchgchb','pending'),(5,19,'2023-02-28','not good\r\n','tyffucfu'),(6,3,'2023-03-07','bad','pending');

/*Table structure for table `diet` */

DROP TABLE IF EXISTS `diet`;

CREATE TABLE `diet` (
  `diet_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `break_fast` varchar(100) DEFAULT NULL,
  `lunch` varchar(100) DEFAULT NULL,
  `post_workout_food` varchar(100) DEFAULT NULL,
  `pre_workout_food` varchar(100) DEFAULT NULL,
  `amount_of_protien` varchar(100) DEFAULT NULL,
  `calorie_of_food` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`diet_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `diet` */

insert  into `diet`(`diet_id`,`user_id`,`break_fast`,`lunch`,`post_workout_food`,`pre_workout_food`,`amount_of_protien`,`calorie_of_food`) values (1,NULL,'egg','chapathi','banana','milk','15','10'),(3,NULL,'banana','rice','egg','protien','20','13'),(4,3,'q','w','e','r','t','y'),(5,1,'s','d','e','w','q','w'),(6,1,'vn  b n','bjkbkjbkb','nkbkb','lnkjnkn','nknbk','nbjbjb');

/*Table structure for table `doctor` */

DROP TABLE IF EXISTS `doctor`;

CREATE TABLE `doctor` (
  `doctor_id` int(11) NOT NULL AUTO_INCREMENT,
  `doctor_name` varchar(50) DEFAULT NULL,
  `experience` varchar(50) DEFAULT NULL,
  `qualification` varchar(50) DEFAULT NULL,
  `email_id` varchar(50) DEFAULT NULL,
  `phone_no` varchar(50) DEFAULT NULL,
  `dob` varchar(50) DEFAULT NULL,
  `gender` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`doctor_id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=latin1;

/*Data for the table `doctor` */

insert  into `doctor`(`doctor_id`,`doctor_name`,`experience`,`qualification`,`email_id`,`phone_no`,`dob`,`gender`) values (6,'anandhu','3','mbbs','anandhu@gmail.com','2142565652','12/2/2002','male'),(8,'aswin','5','mbbs,md','shibu@gmail.com','64646131','19/6/2001','Male'),(10,'adarsh','gkg','feef','rferf','feef','feerf','radio'),(22,'deon','3 years','mbbs','deon','1234567898','2023-03-02','Male');

/*Table structure for table `doubts` */

DROP TABLE IF EXISTS `doubts`;

CREATE TABLE `doubts` (
  `doubt_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `doubt` varchar(100) DEFAULT NULL,
  `reply` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`doubt_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `doubts` */

insert  into `doubts`(`doubt_id`,`user_id`,`date`,`doubt`,`reply`) values (1,1,'12/2/2022','health tips','fffjbjkbkbkbkbkb'),(2,3,'1/2/2022','amount of food','m ,,m   , , ,'),(3,15,'2023-02-27','hgfvhjvjgv','n mm'),(4,19,'2023-02-28','grgryhtd','gtgt5');

/*Table structure for table `employee` */

DROP TABLE IF EXISTS `employee`;

CREATE TABLE `employee` (
  `employee_id` int(11) NOT NULL AUTO_INCREMENT,
  `employee_name` varchar(50) DEFAULT NULL,
  `email_id` varchar(50) DEFAULT NULL,
  `phone_no` varchar(50) DEFAULT NULL,
  `dob` varchar(50) DEFAULT NULL,
  `gender` varchar(50) DEFAULT NULL,
  `experience` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`employee_id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=latin1;

/*Data for the table `employee` */

insert  into `employee`(`employee_id`,`employee_name`,`email_id`,`phone_no`,`dob`,`gender`,`experience`) values (1,'aswin shibu','aswin@gmail.com','64556131','19/6/2001','male','5'),(4,'albin mb','djdcjcjc','23456464','2023-02-03','Male','fguyf'),(6,'naveen','naveen@gmail.com','22514266','2002-02-05','Male','2 year'),(7,'anandhu','anandhu','4646161','2023-02-22','Male','2'),(8,'dwefcsddf','fdsfdcs@ga','2536142512','2023-02-07','Male','xasxas'),(23,'shanith','shanith@gmail.com','8281259244','2023-03-02','Male','ghjggjkkjk');

/*Table structure for table `equipment_details` */

DROP TABLE IF EXISTS `equipment_details`;

CREATE TABLE `equipment_details` (
  `equipment_id` int(11) NOT NULL AUTO_INCREMENT,
  `equipment_name` varchar(50) DEFAULT NULL,
  `details` varchar(150) DEFAULT NULL,
  `photo` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`equipment_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `equipment_details` */

insert  into `equipment_details`(`equipment_id`,`equipment_name`,`details`,`photo`) values (1,'dumbels','25 pcs','/static/equipment/20221215_144206.jpg'),(3,'dumbels','fyffufuvjvu','/static/equipment/20230225_190251.jpg'),(5,'csd','yyyyyyyyyyyyyyyy','/static/equipment/20230228_131028.jpg'),(6,'gg','hhhhhhhhhhh','/static/equipments/20230228-131207.jpg');

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `feedback_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  `feedback` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`feedback_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `feedback` */

insert  into `feedback`(`feedback_id`,`user_id`,`date`,`feedback`) values (1,1,'12/12/2022','good'),(2,2,'21/10/2021','bad'),(3,15,'2023-02-27','cfhgdgdhch'),(5,15,'2023-02-27','cfchch'),(6,19,'2023-02-28','nkjkj');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `usertype` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`usertype`) values (1,'admin','admin','admin'),(2,'instructor','instructor','instructor'),(3,'user','user','user'),(4,'user','user','pending'),(6,'doctor','d','doctor'),(7,'physician','physician','physician'),(8,'doctor','doctor','doctor'),(10,'adarsh','adarsh','doctor'),(12,'naveen','1234','user'),(13,'athul','1234','user'),(14,'jeswin','123','user'),(15,'deon','123','user'),(16,'adarsh','123654','user'),(17,'jilson','123654','user'),(18,'h@gmail.com','ss','user'),(19,'anand','1234','user'),(20,'naveen','1236','instructor'),(21,'albin','55','user'),(22,'deon','deon','doctor'),(23,'shanith@gmail.com','5025','instructor');

/*Table structure for table `medicine` */

DROP TABLE IF EXISTS `medicine`;

CREATE TABLE `medicine` (
  `medicine_id` int(11) NOT NULL AUTO_INCREMENT,
  `medicine_name` varchar(100) DEFAULT NULL,
  `medicine_price` varchar(100) DEFAULT NULL,
  `description` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`medicine_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `medicine` */

insert  into `medicine`(`medicine_id`,`medicine_name`,`medicine_price`,`description`) values (1,'dolo','5','low dose'),(2,'paracetamol','3','500');

/*Table structure for table `payment` */

DROP TABLE IF EXISTS `payment`;

CREATE TABLE `payment` (
  `payment_id` int(11) NOT NULL AUTO_INCREMENT,
  `booking_id` int(11) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `time` varchar(100) DEFAULT NULL,
  `account_no` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`payment_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `payment` */

insert  into `payment`(`payment_id`,`booking_id`,`date`,`time`,`account_no`) values (1,1,'12/2/2021','12:00','651431'),(2,2,'1?2?2019','8:00','654651');

/*Table structure for table `performer` */

DROP TABLE IF EXISTS `performer`;

CREATE TABLE `performer` (
  `performer_id` int(11) NOT NULL AUTO_INCREMENT,
  `applicant_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`performer_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `performer` */

insert  into `performer`(`performer_id`,`applicant_id`) values (1,1),(2,2),(3,3);

/*Table structure for table `physician` */

DROP TABLE IF EXISTS `physician`;

CREATE TABLE `physician` (
  `physician_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `email_id` varchar(50) DEFAULT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `dob` varchar(50) DEFAULT NULL,
  `gender` varchar(50) DEFAULT NULL,
  `qualification` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`physician_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `physician` */

insert  into `physician`(`physician_id`,`name`,`email_id`,`phone`,`dob`,`gender`,`qualification`) values (7,'naveen','naveen@gmail.com','51544654','12/2/2021','male','mbbs'),(8,'aswin','aswin@gmail.com','142.53698','2023-01-30','Male','mbbs');

/*Table structure for table `review` */

DROP TABLE IF EXISTS `review`;

CREATE TABLE `review` (
  `review_id` int(11) NOT NULL AUTO_INCREMENT,
  `date` varchar(50) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `doctor_id` int(11) DEFAULT NULL,
  `review` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`review_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `review` */

insert  into `review`(`review_id`,`date`,`user_id`,`doctor_id`,`review`) values (1,'12/12/2022',3,11,'good'),(2,'2023-02-27',13,8,'bnvjvjvjvbjvj'),(3,'2023-02-27',16,11,'vjfjfvjgbkjknknnj'),(4,'2023-02-27',16,8,'ihiuggiggiguig');

/*Table structure for table `schedule` */

DROP TABLE IF EXISTS `schedule`;

CREATE TABLE `schedule` (
  `schedule_id` int(11) NOT NULL AUTO_INCREMENT,
  `doctor_id` int(11) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  `time_from` varchar(50) DEFAULT NULL,
  `time_to` varchar(50) DEFAULT NULL,
  `number_of_tokens` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`schedule_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `schedule` */

insert  into `schedule`(`schedule_id`,`doctor_id`,`date`,`time_from`,`time_to`,`number_of_tokens`) values (1,12,NULL,'12:00','3:00',NULL),(2,11,'2023-02-22','13:47','14:45','5'),(3,8,'2023-02-28','19:53','15:41','10'),(4,8,'2023-02-28','18:00','19:00','10'),(5,8,'2023-02-27','10:09','11:12','2'),(6,22,'2023-03-07','00:00','04:00','50');

/*Table structure for table `stock` */

DROP TABLE IF EXISTS `stock`;

CREATE TABLE `stock` (
  `stock_id` int(11) NOT NULL AUTO_INCREMENT,
  `physician_id` int(11) DEFAULT NULL,
  `medicine_id` int(11) DEFAULT NULL,
  `stock` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`stock_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `stock` */

insert  into `stock`(`stock_id`,`physician_id`,`medicine_id`,`stock`) values (1,7,1,'69'),(2,8,1,'83'),(3,7,2,'100'),(4,8,2,'95');

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `email_id` varchar(50) DEFAULT NULL,
  `phone_no` varchar(50) DEFAULT NULL,
  `dob` varchar(50) DEFAULT NULL,
  `gender` varchar(50) DEFAULT NULL,
  `photo` varchar(200) DEFAULT NULL,
  `weight` varchar(50) DEFAULT NULL,
  `height` varchar(50) DEFAULT NULL,
  `bmi` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=latin1;

/*Data for the table `user` */

insert  into `user`(`user_id`,`name`,`email_id`,`phone_no`,`dob`,`gender`,`photo`,`weight`,`height`,`bmi`) values (1,'s','df','g','h',NULL,'h','55','148','55.0'),(3,'user','evdwv','11635635','5135151',NULL,'m','55','145','55.0'),(13,'athul','athul','56464446','625663',NULL,'male','155','85','35.38'),(14,'dsffv','vsxdvdd','23543','32q4',NULL,'male','434','23','8204.16'),(15,'anandhu','csd','sdc','4564',NULL,'male','23','34','198.96'),(16,'adarsh','adarsh','254136','654544544',NULL,'male','656','45456','0.0'),(17,'fdhg','jilson','1236549873','2023-02-07',NULL,'male','322','65','762.13'),(18,'ffd','h@gmail.com','7609876543','2023-03-03','male','/static/profile_photo/20230228-152241.jpg','56','175','18.29'),(19,'Anand','anand','1234567890','2012-07-11','male','/static/profile_photo/20230228-161752.jpg','66','170','22.84'),(21,'albin','albin','8281259244','2023-02-27','male','/static/profile_photo/20230301-153932.jpg','56','155','23.31');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
