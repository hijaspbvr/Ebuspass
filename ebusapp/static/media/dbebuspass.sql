-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 06, 2022 at 03:15 PM
-- Server version: 10.4.21-MariaDB
-- PHP Version: 8.0.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `dbebuspass`
--

-- --------------------------------------------------------

--
-- Table structure for table `tblaffiliation`
--

CREATE TABLE `tblaffiliation` (
  `affId` int(11) NOT NULL,
  `inId` int(11) NOT NULL,
  `affType` varchar(50) NOT NULL,
  `affPath` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tblaffiliation`
--

INSERT INTO `tblaffiliation` (`affId`, `inId`, `affType`, `affPath`, `status`) VALUES
(1, 1, 'aaa', 'affiliations/1111 MGU.png', '1'),
(2, 1, 'awde', 'affiliations/images.jpg', '1'),
(3, 1, 'rgfrre', '/media/__studymat_Sunset_x99oUBP.jpg', '1');

-- --------------------------------------------------------

--
-- Table structure for table `tblcard`
--

CREATE TABLE `tblcard` (
  `cardId` int(11) NOT NULL,
  `cardType` varchar(50) NOT NULL,
  `noDays` int(11) NOT NULL,
  `status` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tblcard`
--

INSERT INTO `tblcard` (`cardId`, `cardType`, `noDays`, `status`) VALUES
(2, '1 month', 30, '1'),
(3, '2 months', 90, '1'),
(4, '6 months', 180, '1'),
(5, '10 months', 300, '1'),
(6, '12 month', 365, '1');

-- --------------------------------------------------------

--
-- Table structure for table `tblconcession`
--

CREATE TABLE `tblconcession` (
  `cardId` int(11) NOT NULL,
  `sdId` int(11) NOT NULL,
  `from_date` date NOT NULL,
  `to_date` date NOT NULL,
  `amount` bigint(20) NOT NULL,
  `status` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tblconcession`
--

INSERT INTO `tblconcession` (`cardId`, `sdId`, `from_date`, `to_date`, `amount`, `status`) VALUES
(3, 2, '2019-07-23', '2019-08-22', 210, 'paid'),
(4, 5, '2019-08-22', '2019-09-21', 150, 'paid'),
(5, 4, '2019-08-22', '2019-11-20', 270, 'approved'),
(6, 6, '2020-02-20', '2020-03-21', 210, 'paid'),
(7, 7, '2020-03-20', '2020-04-19', 210, 'approved'),
(8, 7, '2020-03-20', '2020-04-19', 210, 'approved'),
(9, 8, '2020-03-20', '2020-04-19', 210, 'approved'),
(10, 9, '2020-03-20', '2020-04-19', 210, 'approved'),
(11, 10, '2020-03-20', '2020-06-18', 630, 'approved'),
(12, 10, '2020-03-20', '2020-06-18', 630, 'approved'),
(13, 11, '2022-04-02', '2022-07-01', 630, 'paid'),
(14, 12, '2022-04-07', '2022-10-04', 1260, 'paid'),
(15, 13, '2022-04-09', '2022-10-06', 1260, 'paid'),
(16, 14, '2022-05-06', '2022-11-02', 900, 'paid'),
(17, 15, '2022-05-06', '2022-08-04', 630, 'paid');

-- --------------------------------------------------------

--
-- Table structure for table `tblcourse`
--

CREATE TABLE `tblcourse` (
  `courseId` int(11) NOT NULL,
  `courseName` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tblcourse`
--

INSERT INTO `tblcourse` (`courseId`, `courseName`, `status`) VALUES
(1, 'BCA', '1'),
(2, 'MCA', '1'),
(3, 'BCom', '1'),
(4, 'Bsc', '1'),
(5, 'BA', '1'),
(6, 'MSc', '1');

-- --------------------------------------------------------

--
-- Table structure for table `tbldepo`
--

CREATE TABLE `tbldepo` (
  `depoId` int(11) NOT NULL,
  `depoPlace` varchar(50) NOT NULL,
  `depoEmail` varchar(50) NOT NULL,
  `depoContact` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tbldepo`
--

INSERT INTO `tbldepo` (`depoId`, `depoPlace`, `depoEmail`, `depoContact`) VALUES
(1, 'aluva', 'aluva@gmail.com', '9587412631'),
(2, 'angamaly', 'angamaly@gmail.com', '8847150263'),
(3, 'paravoor', 'p@gmail.com', '7867463423'),
(4, 'Ernakulam', 'ernakulam@gmail.com', '9517538245'),
(5, 'Kalamassery', 'kalamassery@gmail.com', '9632587410');

-- --------------------------------------------------------

--
-- Table structure for table `tblinstitute`
--

CREATE TABLE `tblinstitute` (
  `inId` int(11) NOT NULL,
  `inName` varchar(50) NOT NULL,
  `inAddress` varchar(100) NOT NULL,
  `inContact` varchar(50) NOT NULL,
  `inEmail` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tblinstitute`
--

INSERT INTO `tblinstitute` (`inId`, `inName`, `inAddress`, `inContact`, `inEmail`) VALUES
(1, 'mes marampally', 'marampally', '9587410268', 'mesmply@gmail.com'),
(2, 'STAS', 'gfdhfgj', '7564673833', 'stas@gmail.com'),
(3, 'ilahia', 'ilahia college', '759484525', 'ilahia@gmail.com'),
(4, 'Presentation', 'Adrs\r\ncmknckj', '9090909090', 'pre@mail.com');

-- --------------------------------------------------------

--
-- Table structure for table `tblinstitutecourse`
--

CREATE TABLE `tblinstitutecourse` (
  `icId` int(11) NOT NULL,
  `inEmail` varchar(50) NOT NULL,
  `courseId` int(11) NOT NULL,
  `status` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tblinstitutecourse`
--

INSERT INTO `tblinstitutecourse` (`icId`, `inEmail`, `courseId`, `status`) VALUES
(1, 'mesmply@gmail.com', 1, '1'),
(5, 'mesmply@gmail.com', 3, '1'),
(6, 'stas@gmail.com', 1, '1'),
(7, 'mesmply@gmail.com', 2, '1');

-- --------------------------------------------------------

--
-- Table structure for table `tbllogin`
--

CREATE TABLE `tbllogin` (
  `uname` varchar(50) NOT NULL,
  `pwd` varchar(50) NOT NULL,
  `utype` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tbllogin`
--

INSERT INTO `tbllogin` (`uname`, `pwd`, `utype`, `status`) VALUES
('aluva@gmail.com', 'aluvadepo', 'depo', '1'),
('angamaly@gmail.com', 'angamaly@gmail.com', 'depo', '1'),
('mesmply@gmail.com', 'mesmply', 'institute', '1'),
('admin@gmail.com', 'admin', 'admin', '1'),
('abhi@gmail.com', 'abhi', 'student', '1'),
('anju@gmail.com', 'anju@gmail.com', 'student', '1'),
('kari@gmail.com', 'kari', 'student', '1'),
('stas@gmail.com', 'stas', 'institute', '1'),
('p@gmail.com', 'p@gmail.com', 'depo', '1'),
('ernakulam@gmail.com', 'ernakulam@gmail.com', 'depo', '1'),
('megha@gmail.com', 'megha', 'student', '1'),
('anoop@gmail.com', 'anoop', 'student', '1'),
('kalamassery@gmail.com', 'kalamassery@gmail.com', 'depo', '0'),
('ilahia@gmail.com', 'ilahia', 'institute', '1'),
('akhila@gmail.com', 'akhila@111', 'student', '1'),
('ammu@gmail.com', 'ammu@111', 'student', '1'),
('gopu@gmail.com', 'gopu@111', 'student', '1'),
('manju@gmail.com', 'manju@123', 'student', '1'),
('vis@mail.com', 'Vis@12345', 'student', '1'),
('aji@mail.com', 'Aji@12345', 'student', '1'),
('pre@mail.com', 'Pre@12345', 'institute', '1'),
('vish@mail.com', 'Vis@12345', 'student', '1'),
('hisham@mail.com', 'Hisham@12345', 'student', '1'),
('gh@mail.com', 'Gh@12345', 'student', '1');

-- --------------------------------------------------------

--
-- Table structure for table `tblroute`
--

CREATE TABLE `tblroute` (
  `rId` int(11) NOT NULL,
  `rFrom` varchar(50) NOT NULL,
  `rTo` varchar(50) NOT NULL,
  `charge` int(11) NOT NULL,
  `status` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tblroute`
--

INSERT INTO `tblroute` (`rId`, `rFrom`, `rTo`, `charge`, `status`) VALUES
(1, 'Aluva Bank Junction', 'Aluva Pump Junction', 5, '1'),
(2, 'Aluva Bank Junction', 'Pulinchode', 7, '1'),
(3, 'Aluva Bank Junction', 'paravoor kavala', 4, '1'),
(4, 'paravoor kavala', 'Aluva Pump Junction', 3, '1'),
(5, '5', '1', 7, '0'),
(6, 'seminary pady', 'Aluva Pump Junction', 7, '1'),
(7, 'Aluva Bank Junction', 'seminary pady', 7, '1'),
(8, 'Aluva Bank Junction', 'Aluva Pump Junction', 12, '1'),
(9, 'Aluva Bank Junction', 'Pulinchode', 12, '1');

-- --------------------------------------------------------

--
-- Table structure for table `tblstop`
--

CREATE TABLE `tblstop` (
  `stopId` int(11) NOT NULL,
  `stopName` varchar(50) NOT NULL,
  `depoEmail` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tblstop`
--

INSERT INTO `tblstop` (`stopId`, `stopName`, `depoEmail`, `status`) VALUES
(1, 'Aluva Bank Junction', 'aluva@gmail.com', '1'),
(2, 'Aluva Pump Junction', 'aluva@gmail.com', '1'),
(3, 'Pulinchode', 'aluva@gmail.com', '1'),
(4, 'paravoor kavala', 'p@gmail.com', '1'),
(5, 'seminary pady', 'aluva@gmail.com', '1'),
(6, 'Ambattukavu', 'aluva@gmail.com', '1');

-- --------------------------------------------------------

--
-- Table structure for table `tblstudentdetails`
--

CREATE TABLE `tblstudentdetails` (
  `sdId` int(11) NOT NULL,
  `sEmail` varchar(50) NOT NULL,
  `placeFrom` varchar(50) NOT NULL,
  `placeTo` varchar(50) NOT NULL,
  `cardId` int(11) NOT NULL,
  `aadharNo` varchar(50) NOT NULL,
  `photo` varchar(100) NOT NULL,
  `status` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tblstudentdetails`
--

INSERT INTO `tblstudentdetails` (`sdId`, `sEmail`, `placeFrom`, `placeTo`, `cardId`, `aadharNo`, `photo`, `status`) VALUES
(2, 'abhi@gmail.com', 'Aluva Bank Junction', 'Pulinchode', 2, '96582014730256', 'images/pic.jpg', 'paid'),
(3, 'abhi@gmail.com', 'Pulinchode', 'Pulinchode', 2, '654356465', 'images/164621135-pencil-wallpapers.jpg', 'rejected'),
(4, 'kari@gmail.com', 'paravoor kavala', 'Aluva Pump Junction', 3, '113243536678', 'images/enc.png', 'approved'),
(5, 'kari@gmail.com', 'Aluva Bank Junction', 'Aluva Pump Junction', 2, '12342345455', 'images/enc.png', 'paid'),
(6, 'megha@gmail.com', 'Aluva Bank Junction', 'Pulinchode', 2, '788945612302', '/media/beautiful-scenery-8_KccxZjE.jpg', 'paid'),
(7, 'akhila@gmail.com', 'Aluva Bank Junction', 'Pulinchode', 2, '987654321', '/media/0_578_872_0_70_http___cdni.autocarindia.com_ExtraImages_20180123124138_Swift_BLUE.jpg', 'approved'),
(8, 'ammu@gmail.com', 'Aluva Bank Junction', 'Ambattukavu', 2, '9876564321', '/media/0_578_872_0_70_http___cdni.autocarindia.com_ExtraImages_20180123124138_Swift_BLUE_J0NMg9L.jpg', 'approved'),
(9, 'manju@gmail.com', 'Aluva Bank Junction', 'Pulinchode', 2, '987654321', '/media/0_578_872_0_70_http___cdni.autocarindia.com_ExtraImages_20180123124138_Swift_BLUE_1UCJ1nb.jpg', 'approved'),
(10, 'manju@gmail.com', 'Aluva Bank Junction', 'Pulinchode', 3, '569847102365', '/media/Screenshot%20(28).png', 'approved'),
(11, 'vis@mail.com', 'Aluva Bank Junction', 'seminary pady', 3, '1234567654321234567', '/media/hanna-morris-Eu_jjK6Z67Q-unsplash%20(1).jpg', 'paid'),
(12, 'aji@mail.com', 'Aluva Bank Junction', 'Pulinchode', 4, '12345678987654222', '/media/pwd.jpg', 'paid'),
(13, 'vish@mail.com', 'Aluva Bank Junction', 'Pulinchode', 4, '12345678987654321', '/media/userimages_1level%20(1).jpg', 'paid'),
(14, 'hisham@mail.com', 'Aluva Bank Junction', 'Aluva Pump Junction', 4, '111111111111111', '/media/1level_fRAN3Rk%20(1).jpg', 'paid'),
(15, 'gh@mail.com', 'Aluva Bank Junction', 'Pulinchode', 3, '1234565432123456', '/media/1level_fRAN3Rk%20(1)_5Ppw1XT.jpg', 'paid');

-- --------------------------------------------------------

--
-- Table structure for table `tblstudentregistration`
--

CREATE TABLE `tblstudentregistration` (
  `sId` int(11) NOT NULL,
  `sName` varchar(50) NOT NULL,
  `sAge` varchar(50) NOT NULL,
  `sAddress` varchar(50) NOT NULL,
  `sGender` varchar(50) NOT NULL,
  `sFather` varchar(50) NOT NULL,
  `sEmail` varchar(50) NOT NULL,
  `sContact` varchar(50) NOT NULL,
  `inId` int(11) NOT NULL,
  `admnNo` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tblstudentregistration`
--

INSERT INTO `tblstudentregistration` (`sId`, `sName`, `sAge`, `sAddress`, `sGender`, `sFather`, `sEmail`, `sContact`, `inId`, `admnNo`) VALUES
(1, 'Abhi', '18', 'dfvkbfj', 'Male', 'Aji', 'abhi@gmail.com', '9587412036', 1, '4857'),
(2, 'Anju', '18', 'Female', 'dfgsdfg', 'Anand', 'anju@gmail.com', '95586321470', 1, '1236'),
(3, 'karishma', '24', 'Female', 'fjgkjgd', 'rajan', 'kari@gmail.com', '687587653', 1, '2344'),
(4, 'Megha', '1', 'Female', 'sdrfgser', 'erger', 'megha@gmail.com', '9632580147', 1, '3423'),
(5, 'Anoop', '21', 'Male', 'awerfger', 'aertger', 'anoop@gmail.com', '9541782630', 1, '7844'),
(6, 'akhila', '18', 'Female', 'akhila devassy', 'devassy', 'akhila@gmail.com', '7594845250', 1, '123'),
(7, 'ammu', '19', 'Female', 'ammukutty', 'jose', 'ammu@gmail.com', '7594845250', 3, '123'),
(8, 'gopu', '19', 'Female', 'gopuzzz', 'biju', 'gopu@gmail.com', '7594845250', 2, '123'),
(9, 'Manju', '20', 'Female', 'Aluva', 'Amal', 'manju@gmail.com', '7594845250', 3, '1245'),
(10, 'Vis', '18', 'Male', 'Vis\r\nAdrs', 'VV', 'vis@mail.com', '9090909090', 2, '123'),
(11, 'Aji', '19', 'Male', 'Aji\r\nAdrs', 'Ragu', 'aji@mail.com', '7878787878', 2, '123'),
(12, 'Vis', '24', 'Male', 'Vis\r\nAdrs', 'V', 'vish@mail.com', '8989898989', 4, '101'),
(13, 'Hisham', '21', 'Male', 'His\r\nAdrs', 'Haris', 'hisham@mail.com', '9090909090', 3, 'IL12345'),
(14, 'ghj', '21', 'Male', 'bhvj\r\nhbjh', 'ghg', 'gh@mail.com', '9090909090', 1, '12345');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `tblaffiliation`
--
ALTER TABLE `tblaffiliation`
  ADD PRIMARY KEY (`affId`);

--
-- Indexes for table `tblcard`
--
ALTER TABLE `tblcard`
  ADD PRIMARY KEY (`cardId`);

--
-- Indexes for table `tblconcession`
--
ALTER TABLE `tblconcession`
  ADD PRIMARY KEY (`cardId`);

--
-- Indexes for table `tblcourse`
--
ALTER TABLE `tblcourse`
  ADD PRIMARY KEY (`courseId`);

--
-- Indexes for table `tbldepo`
--
ALTER TABLE `tbldepo`
  ADD PRIMARY KEY (`depoId`);

--
-- Indexes for table `tblinstitute`
--
ALTER TABLE `tblinstitute`
  ADD PRIMARY KEY (`inId`);

--
-- Indexes for table `tblinstitutecourse`
--
ALTER TABLE `tblinstitutecourse`
  ADD PRIMARY KEY (`icId`);

--
-- Indexes for table `tblroute`
--
ALTER TABLE `tblroute`
  ADD PRIMARY KEY (`rId`);

--
-- Indexes for table `tblstop`
--
ALTER TABLE `tblstop`
  ADD PRIMARY KEY (`stopId`);

--
-- Indexes for table `tblstudentdetails`
--
ALTER TABLE `tblstudentdetails`
  ADD PRIMARY KEY (`sdId`);

--
-- Indexes for table `tblstudentregistration`
--
ALTER TABLE `tblstudentregistration`
  ADD PRIMARY KEY (`sId`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `tblaffiliation`
--
ALTER TABLE `tblaffiliation`
  MODIFY `affId` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `tblcard`
--
ALTER TABLE `tblcard`
  MODIFY `cardId` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `tblconcession`
--
ALTER TABLE `tblconcession`
  MODIFY `cardId` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT for table `tblcourse`
--
ALTER TABLE `tblcourse`
  MODIFY `courseId` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `tbldepo`
--
ALTER TABLE `tbldepo`
  MODIFY `depoId` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `tblinstitute`
--
ALTER TABLE `tblinstitute`
  MODIFY `inId` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `tblinstitutecourse`
--
ALTER TABLE `tblinstitutecourse`
  MODIFY `icId` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `tblroute`
--
ALTER TABLE `tblroute`
  MODIFY `rId` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `tblstop`
--
ALTER TABLE `tblstop`
  MODIFY `stopId` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `tblstudentdetails`
--
ALTER TABLE `tblstudentdetails`
  MODIFY `sdId` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `tblstudentregistration`
--
ALTER TABLE `tblstudentregistration`
  MODIFY `sId` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
