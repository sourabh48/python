-- phpMyAdmin SQL Dump
-- version 3.3.9
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Nov 07, 2017 at 01:29 PM
-- Server version: 5.5.8
-- PHP Version: 5.3.5

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `online_exam`
--

-- --------------------------------------------------------

--
-- Table structure for table `profile`
--

CREATE TABLE IF NOT EXISTS `profile` (
  `FIRST_NAME` varchar(20) NOT NULL,
  `LAST_NAME` varchar(20) NOT NULL,
  `EMAIL_ID` varchar(25) NOT NULL,
  `USER_NAME` varchar(20) NOT NULL,
  `PASSWORD` varchar(15) NOT NULL,
  `USER_TYPE` varchar(15) NOT NULL,
  `STATUS` int(2) NOT NULL,
  PRIMARY KEY (`USER_NAME`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `profile`
--

INSERT INTO `profile` (`FIRST_NAME`, `LAST_NAME`, `EMAIL_ID`, `USER_NAME`, `PASSWORD`, `USER_TYPE`, `STATUS`) VALUES
('Admin', 'Super', 'admin@gmail.com', 'admin', '123', 'ADMIN', 0),
('Arup', 'Karmakar', 'arup@gmail.com', 'arup', '123', 'Student', 1);

-- --------------------------------------------------------

--
-- Table structure for table `question`
--

CREATE TABLE IF NOT EXISTS `question` (
  `Q_NO` int(3) NOT NULL,
  `QUESTION` varchar(70) NOT NULL,
  `ANS1` varchar(30) NOT NULL,
  `ANS2` varchar(30) NOT NULL,
  `ANS3` varchar(30) NOT NULL,
  `ANS4` varchar(30) NOT NULL,
  `C_ANS` int(11) NOT NULL,
  `P_CODE` int(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `question`
--

INSERT INTO `question` (`Q_NO`, `QUESTION`, `ANS1`, `ANS2`, `ANS3`, `ANS4`, `C_ANS`, `P_CODE`) VALUES
(1, 'In C function returns ', 'Single value', 'Double value', 'Multiple value', 'None of this', 1, 1001),
(2, 'getch() is used ', 'to display the output', 'to clear screen', 'to hold the screen', 'None of this', 3, 1001),
(1, 'Linux inventor', 'xyz', 'fdf', 'fdf', 'vcvc', 1, 1002),
(2, 'Open source means?', 'r', 'fdf', 'ff', 'cvc', 4, 1002);

-- --------------------------------------------------------

--
-- Table structure for table `result`
--

CREATE TABLE IF NOT EXISTS `result` (
  `EXAM_CODE` varchar(6) NOT NULL,
  `USER_NAME` varchar(30) NOT NULL,
  `P_NAME` varchar(20) NOT NULL,
  `MARKS1` int(3) NOT NULL,
  `MARKS2` int(3) NOT NULL,
  `STATUS` varchar(10) NOT NULL,
  `EXAM_DATE` date NOT NULL,
  PRIMARY KEY (`EXAM_CODE`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `result`
--

INSERT INTO `result` (`EXAM_CODE`, `USER_NAME`, `P_NAME`, `MARKS1`, `MARKS2`, `STATUS`, `EXAM_DATE`) VALUES
('E1001', 'arup', 'C-C++ and Unix', 1, 0, 'FAIL', '2017-11-07'),
('E1002', 'arup', 'C-C++ and Unix', 2, 1, 'PASS', '2017-11-07');
