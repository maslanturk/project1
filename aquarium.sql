-- phpMyAdmin SQL Dump
-- version 4.8.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 13, 2018 at 12:21 AM
-- Server version: 10.1.34-MariaDB
-- PHP Version: 7.2.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `aquarium`
--

-- --------------------------------------------------------

--
-- Table structure for table `inputs`
--

CREATE TABLE `inputs` (
  `ID` int(11) NOT NULL,
  `Baslik` text NOT NULL,
  `Kullanici` text NOT NULL,
  `Tarih` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `Kh` float NOT NULL,
  `Alkalinity` float NOT NULL,
  `Ca` float NOT NULL,
  `Mg` float NOT NULL,
  `Fosfat` float NOT NULL,
  `NO3` float NOT NULL,
  `PH` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `inputs`
--

INSERT INTO `inputs` (`ID`, `Baslik`, `Kullanici`, `Tarih`, `Kh`, `Alkalinity`, `Ca`, `Mg`, `Fosfat`, `NO3`, `PH`) VALUES
(2, 'fsadfdsa', 'mmmraslntrk@gmail.com', '2018-08-09 20:31:06', 27, 9, 8, 12, 18, 9, 10),
(3, 'asdfds', 'mmmraslntrk@gmail.com', '2018-08-09 20:35:07', 0, 0, 0, 0, 0, 0, 0),
(4, 'fdsfsd', 'mmmraslntrk@gmail.com', '2018-08-10 11:38:39', 16, 25, 12, 11, 16, 14, 13),
(5, 'fsdafdasfds', 'mmmraslntrk@gmail.com', '2018-08-12 20:15:56', 13, 10, 20, 22, 120, 140, 45),
(6, 'deneme', 'mmmraslntrk@gmail.com', '2018-08-12 21:11:30', 20, 15, 23, 27, -15, 18, 7);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `ID` int(11) NOT NULL,
  `Adi_Soyadi` text NOT NULL,
  `Email` text NOT NULL,
  `Sifre` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`ID`, `Adi_Soyadi`, `Email`, `Sifre`) VALUES
(1, 'adf', 'asd', '$5$rounds=535000$LogUp4JRcnRCXc3I$rUmnffxjEDoExec3QCOh6UtCIrgRYCI44R61yiCjhj6'),
(2, 'adf', 'adsf@outlook.com', '$5$rounds=535000$iu1bsvQZEo/g1W.y$mSC89Gimn3wj1UTXF.78LLPacUQcjC4DIaSgy.3ftbB'),
(3, 'adf', 'adsf@outlook.com', '$5$rounds=535000$M8Kn5qHo6/6lFdij$f1CJV60wyalhpczwYwfyrLIwkdMYh3Lwqs6bsE6OWeB'),
(18, 'muammer aslantürk', 'mmmraslntrk@gmail.com', '$5$rounds=535000$dDquG80D/Tz.Dbix$TJFp7Gbgu24zN0b2nwzU9fUGJZgecSDzhOgP1UHSbX2'),
(19, 'muammer aslantürk', 'mmmraslntrk@outlook.com', '$5$rounds=535000$4CC5oVxLXlO/4kq8$DdriOBhSkr9TLQL40hE56.2/SU/sWbZji.VAmmgJ6xC');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `inputs`
--
ALTER TABLE `inputs`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `inputs`
--
ALTER TABLE `inputs`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
