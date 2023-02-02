-- MySQL Administrator dump 1.4
--
-- ------------------------------------------------------
-- Server version	5.0.15-nt


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


--
-- Create schema fproject
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ fproject;
USE fproject;

--
-- Table structure for table `fproject`.`c_members`
--

DROP TABLE IF EXISTS `c_members`;
CREATE TABLE `c_members` (
  `M_id` int(9) NOT NULL,
  `Name` varchar(30) default NULL,
  `Gender` char(1) default NULL,
  `Dob` date default NULL,
  `Aadhar_card` bigint(12) default NULL,
  `Address` varchar(50) default NULL,
  `M_no` bigint(10) default NULL,
  `Doj` varchar(8) default NULL,
  `Fees_Paid` int(7) default NULL,
  `Fees_Delay` int(6) default NULL,
  PRIMARY KEY  (`M_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `fproject`.`c_members`
--

/*!40000 ALTER TABLE `c_members` DISABLE KEYS */;
/*!40000 ALTER TABLE `c_members` ENABLE KEYS */;


--
-- Table structure for table `fproject`.`cars`
--

DROP TABLE IF EXISTS `cars`;
CREATE TABLE `cars` (
  `No_plate` varchar(10) NOT NULL,
  `company` varchar(15) default NULL,
  `Model` varchar(15) default NULL,
  `department` varchar(8) default NULL,
  `Feul_type` varchar(8) default NULL,
  `puc` char(1) default NULL,
  `Insurance` char(1) default NULL,
  `availibility` char(1) default NULL,
  PRIMARY KEY  (`No_plate`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `fproject`.`cars`
--

/*!40000 ALTER TABLE `cars` DISABLE KEYS */;
INSERT INTO `cars` (`No_plate`,`company`,`Model`,`department`,`Feul_type`,`puc`,`Insurance`,`availibility`) VALUES 
 ('RJ14557895','model','company','Premium','Electric','N','Y','Y'),
 ('rj14dd0001','honda','activa','Normal','Feul','Y','Y','Y'),
 ('rj14yd4578','ifad','gafu','Normal','Desiel','Y','Y','Y');
/*!40000 ALTER TABLE `cars` ENABLE KEYS */;


--
-- Table structure for table `fproject`.`drivers`
--

DROP TABLE IF EXISTS `drivers`;
CREATE TABLE `drivers` (
  `D_id` varchar(6) NOT NULL,
  `Name` varchar(30) default NULL,
  `Gender` char(1) default NULL,
  `Dob` varchar(8) default NULL,
  `D_Lisence` varchar(16) default NULL,
  `aadhar_card` bigint(12) default NULL,
  `Address` varchar(30) default NULL,
  `M_no` bigint(10) default NULL,
  `Doj` varchar(8) default NULL,
  `D_test` char(1) default NULL,
  PRIMARY KEY  (`D_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `fproject`.`drivers`
--

/*!40000 ALTER TABLE `drivers` DISABLE KEYS */;
/*!40000 ALTER TABLE `drivers` ENABLE KEYS */;


--
-- Table structure for table `fproject`.`l_drivers`
--

DROP TABLE IF EXISTS `l_drivers`;
CREATE TABLE `l_drivers` (
  `D_id` varchar(6) NOT NULL,
  `Name` varchar(30) default NULL,
  `Gender` char(1) default NULL,
  `Dob` varchar(8) default NULL,
  `D_Lisence` varchar(16) default NULL,
  `aadhar_card` bigint(12) default NULL,
  `Address` varchar(30) default NULL,
  `M_no` bigint(10) default NULL,
  `Doj` varchar(8) default NULL,
  `D_test` char(1) default NULL,
  PRIMARY KEY  (`D_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `fproject`.`l_drivers`
--

/*!40000 ALTER TABLE `l_drivers` DISABLE KEYS */;
/*!40000 ALTER TABLE `l_drivers` ENABLE KEYS */;


--
-- Table structure for table `fproject`.`members`
--

DROP TABLE IF EXISTS `members`;
CREATE TABLE `members` (
  `M_id` int(9) NOT NULL,
  `Name` varchar(30) default NULL,
  `Gender` char(1) default NULL,
  `Dob` date default NULL,
  `Aadhar_card` bigint(12) default NULL,
  `Address` varchar(50) default NULL,
  `M_no` bigint(10) default NULL,
  `Doj` varchar(8) default NULL,
  `Fees_Paid` int(7) default NULL,
  `Fees_Delay` int(6) default NULL,
  PRIMARY KEY  (`M_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `fproject`.`members`
--

/*!40000 ALTER TABLE `members` DISABLE KEYS */;
/*!40000 ALTER TABLE `members` ENABLE KEYS */;


--
-- Table structure for table `fproject`.`mlogin`
--

DROP TABLE IF EXISTS `mlogin`;
CREATE TABLE `mlogin` (
  `login_id` varchar(30) NOT NULL,
  `password` varchar(30) default NULL,
  PRIMARY KEY  (`login_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `fproject`.`mlogin`
--

/*!40000 ALTER TABLE `mlogin` DISABLE KEYS */;
INSERT INTO `mlogin` (`login_id`,`password`) VALUES 
 ('first ','project');
/*!40000 ALTER TABLE `mlogin` ENABLE KEYS */;


--
-- Table structure for table `fproject`.`routine`
--

DROP TABLE IF EXISTS `routine`;
CREATE TABLE `routine` (
  `No_plate` varchar(10) NOT NULL,
  `6_7AM` varchar(50) default NULL,
  `7_8AM` varchar(50) default NULL,
  `3_4PM` varchar(50) default NULL,
  `4_5PM` varchar(50) default NULL,
  `5_6PM` varchar(50) default NULL,
  `6_7PM` varchar(50) default NULL,
  `7_8PM` varchar(50) default NULL,
  PRIMARY KEY  (`No_plate`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `fproject`.`routine`
--

/*!40000 ALTER TABLE `routine` DISABLE KEYS */;
INSERT INTO `routine` (`No_plate`,`6_7AM`,`7_8AM`,`3_4PM`,`4_5PM`,`5_6PM`,`6_7PM`,`7_8PM`) VALUES 
 ('RJ14557895','1231','m123/d123','','','','123',''),
 ('rj14dd0001','','','','','','',''),
 ('RJ14YD4539','','','','','','','');
/*!40000 ALTER TABLE `routine` ENABLE KEYS */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
