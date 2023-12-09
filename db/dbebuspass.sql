-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 06, 2023 at 05:57 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

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
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- --------------------------------------------------------

--
-- Table structure for table `tblcard`
--

CREATE TABLE `tblcard` (
  `cardId` int(11) NOT NULL,
  `cardType` varchar(50) NOT NULL,
  `noDays` int(11) NOT NULL,
  `status` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

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
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- --------------------------------------------------------

--
-- Table structure for table `tblcourse`
--

CREATE TABLE `tblcourse` (
  `courseId` int(11) NOT NULL,
  `courseName` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- --------------------------------------------------------

--
-- Table structure for table `tbldepo`
--

CREATE TABLE `tbldepo` (
  `depoId` int(11) NOT NULL,
  `depoPlace` varchar(50) NOT NULL,
  `depoEmail` varchar(50) NOT NULL,
  `depoContact` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

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
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- --------------------------------------------------------

--
-- Table structure for table `tblinstitutecourse`
--

CREATE TABLE `tblinstitutecourse` (
  `icId` int(11) NOT NULL,
  `inEmail` varchar(50) NOT NULL,
  `courseId` int(11) NOT NULL,
  `status` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- --------------------------------------------------------

--
-- Table structure for table `tbllogin`
--

CREATE TABLE `tbllogin` (
  `uname` varchar(50) NOT NULL,
  `pwd` varchar(50) NOT NULL,
  `utype` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `tbllogin`
--

INSERT INTO `tbllogin` (`uname`, `pwd`, `utype`, `status`) VALUES
('admin@gmail.com', 'admin', 'admin', '1');

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
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- --------------------------------------------------------

--
-- Table structure for table `tblstop`
--

CREATE TABLE `tblstop` (
  `stopId` int(11) NOT NULL,
  `stopName` varchar(50) NOT NULL,
  `depoEmail` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

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
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

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
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

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
  MODIFY `affId` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tblcard`
--
ALTER TABLE `tblcard`
  MODIFY `cardId` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tblconcession`
--
ALTER TABLE `tblconcession`
  MODIFY `cardId` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tblcourse`
--
ALTER TABLE `tblcourse`
  MODIFY `courseId` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tbldepo`
--
ALTER TABLE `tbldepo`
  MODIFY `depoId` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tblinstitute`
--
ALTER TABLE `tblinstitute`
  MODIFY `inId` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tblinstitutecourse`
--
ALTER TABLE `tblinstitutecourse`
  MODIFY `icId` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tblroute`
--
ALTER TABLE `tblroute`
  MODIFY `rId` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tblstop`
--
ALTER TABLE `tblstop`
  MODIFY `stopId` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tblstudentdetails`
--
ALTER TABLE `tblstudentdetails`
  MODIFY `sdId` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tblstudentregistration`
--
ALTER TABLE `tblstudentregistration`
  MODIFY `sId` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
