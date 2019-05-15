-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: 2019 m. Geg 15 d. 18:31
-- Server version: 8.0.13-4
-- PHP Version: 7.2.17-0ubuntu0.18.04.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `UST4tbdtjQ`
--

-- --------------------------------------------------------

--
-- Sukurta duomenų struktūra lentelei `Semestras_Aikstele`
--

CREATE TABLE `Semestras_Aikstele` (
  `Adresas` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `Vietu_skaicius` int(11) NOT NULL,
  `id_Aikstele` int(11) NOT NULL,
  `fk_Kaina` int(11) NOT NULL,
  `fk_Padalinys` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Sukurta duomenų kopija lentelei `Semestras_Aikstele`
--

INSERT INTO `Semestras_Aikstele` (`Adresas`, `Vietu_skaicius`, `id_Aikstele`, `fk_Kaina`, `fk_Padalinys`) VALUES
('6 Toban Road', 127, 1, 1, 1),
('0 Valley Edge Hill', 140, 2, 2, 2),
('2643 Cardinal Terrace', 58, 3, 3, 5),
('225 Center Circle', 109, 4, 4, 1),
('0 Caliangt Way', 106, 5, 5, 1),
('25 Ridgeway Avenue', 64, 6, 6, 3),
('8976 Everett Circle', 91, 7, 7, 3),
('09368 Lien Avenue', 143, 8, 8, 1),
('10 Clemons Parkway', 93, 9, 9, 3),
('6 Esker Lane', 118, 10, 10, 5),
('33 Washington Drive', 84, 11, 11, 1);

-- --------------------------------------------------------

--
-- Sukurta duomenų struktūra lentelei `Semestras_Imone`
--

CREATE TABLE `Semestras_Imone` (
  `Pavadinimas` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `Gyvenamoji_vietove` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `Adresas` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `El_Pastas` varchar(255) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Sukurta duomenų kopija lentelei `Semestras_Imone`
--

INSERT INTO `Semestras_Imone` (`Pavadinimas`, `Gyvenamoji_vietove`, `Adresas`, `El_Pastas`) VALUES
('Hilll-West', 'Wentai', '2356 Ridge Oak Lane', 'acrigin8@mtv.com'),
('Bechtelar-Stokes', 'Andkhōy', '040 Hansons Center', 'bmaccauley2@elpais.com'),
('Romaguera, Schamberger and Cole', 'Tenjolaya', '810 Westport Avenue', 'driddich0@seattletimes.com'),
('Bosco, Mueller and Batz', 'El Mida', '45 Superior Drive', 'jfarran3@blinklist.com'),
('Lockman, Berge and Jenkins', 'Detusoko', '6473 Norway Maple Junction', 'kdearnaly6@chronoengine.com'),
('Botsford, Friesen and Kohler', 'Washington', '788 Fremont Crossing', 'medon5@businesswire.com'),
('Ledner, O\'Reilly and Nader', 'Alubijid', '60840 Nova Place', 'npaolini9@cargocollective.com'),
('Blanda, Reilly and Wiza', 'Reims', '22 Quincy Point', 'pilyas1@ucla.edu'),
('Nader Group', 'Jabłonowo Pomorskie', '699 Veith Way', 'sguarnier4@i2i.jp'),
('Cronin Inc', 'Strazhitsa', '569 Transport Road', 'wcotillard7@hao123.com');

-- --------------------------------------------------------

--
-- Sukurta duomenų struktūra lentelei `Semestras_Kaina`
--

CREATE TABLE `Semestras_Kaina` (
  `Kaina` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `id_Kaina` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Sukurta duomenų kopija lentelei `Semestras_Kaina`
--

INSERT INTO `Semestras_Kaina` (`Kaina`, `id_Kaina`) VALUES
('10.00', 1),
('10.00', 2),
('10.00', 3),
('10.00', 4),
('10.00', 5),
('10.00', 6),
('10.00', 7),
('10.00', 8),
('10.00', 9),
('10.00', 10),
('10.00', 11);

-- --------------------------------------------------------

--
-- Sukurta duomenų struktūra lentelei `Semestras_Padalinys`
--

CREATE TABLE `Semestras_Padalinys` (
  `Pavadinimas` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `Vadovas` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `id_Padalinys` int(11) NOT NULL,
  `fk_Imone` varchar(255) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Sukurta duomenų kopija lentelei `Semestras_Padalinys`
--

INSERT INTO `Semestras_Padalinys` (`Pavadinimas`, `Vadovas`, `id_Padalinys`, `fk_Imone`) VALUES
('SORGHUM HALEPENSE POLLEN', 'Jack', 1, 'bmaccauley2@elpais.com'),
('Lisinopril and Hydrochlorothiazide', 'Vida', 2, 'bmaccauley2@elpais.com'),
('Trazodone Hydrochloride', 'Martguerita', 3, 'jfarran3@blinklist.com'),
('Premarin', 'Ranna', 4, 'jfarran3@blinklist.com'),
('REVITALIZING C I2PL STEMCELL BB', 'Padriac', 5, 'jfarran3@blinklist.com');

-- --------------------------------------------------------

--
-- Sukurta duomenų struktūra lentelei `Semestras_Stovejimo_laikas`
--

CREATE TABLE `Semestras_Stovejimo_laikas` (
  `stovejimo_pradzia` datetime NOT NULL,
  `stovejimo_pabaiga` datetime NOT NULL,
  `Busena` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `Kodas` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `id_Stovejimo_laikas` int(11) NOT NULL,
  `fk_Transporto_priemone` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Sukurta duomenų kopija lentelei `Semestras_Stovejimo_laikas`
--

INSERT INTO `Semestras_Stovejimo_laikas` (`stovejimo_pradzia`, `stovejimo_pabaiga`, `Busena`, `Kodas`, `id_Stovejimo_laikas`, `fk_Transporto_priemone`) VALUES
('2019-05-02 06:00:16', '2019-05-12 10:06:09', 'Paruosta', '9x0rp', 1, 5),
('2019-05-01 00:00:00', '2019-05-13 21:25:31', 'Nesumoketa', 'AgGgM', 2, 1),
('2019-05-13 22:09:32', '2019-05-13 22:12:38', 'Paruosta', '340zJ', 3, 2),
('2019-05-13 22:13:18', '2019-05-13 22:13:18', 'Nesumoketa', 'Dowdx', 5, 2),
('2019-06-09 10:00:00', '2019-06-09 10:00:00', 'Nesumoketa', 'PQ64P', 6, 18),
('2019-05-14 10:52:34', '2019-05-14 10:53:19', 'Paruosta', 'LcZVY', 7, 19),
('2019-05-14 10:53:55', '2019-05-14 10:54:38', 'Paruosta', 'BOnLy', 8, 19),
('2019-05-14 16:02:05', '2019-05-14 16:03:15', 'Paruosta', 'VbRvY', 9, 19),
('2019-05-14 16:03:22', '2019-05-14 16:03:28', 'Paruosta', 'RVrib', 10, 19),
('2019-05-14 16:07:10', '2019-05-14 16:07:34', 'Paruosta', 'joIkX', 11, 19),
('2019-05-14 16:08:14', '2019-05-14 16:10:04', 'Paruosta', '0chHF', 12, 19),
('2019-05-14 16:15:42', '2019-05-14 16:15:42', 'Nesumoketa', 'mh0i7', 13, 19),
('2019-05-14 16:41:50', '2019-05-14 16:42:08', 'Paruosta', 'rHGKT', 14, 20),
('2019-05-14 16:45:33', '2019-05-14 16:45:33', 'Nesumoketa', 'aggvj', 15, 20),
('2019-05-14 16:45:52', '2019-05-14 16:45:52', 'Nesumoketa', 'znoMV', 16, 21),
('2019-05-14 16:50:37', '2019-05-14 16:52:04', 'Paruosta', 'RgaA7', 17, 22);

-- --------------------------------------------------------

--
-- Sukurta duomenų struktūra lentelei `Semestras_Transporto_priemone`
--

CREATE TABLE `Semestras_Transporto_priemone` (
  `Numeris` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `Busena` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `id_Transporto_priemone` int(11) NOT NULL,
  `fk_Aikstele` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Sukurta duomenų kopija lentelei `Semestras_Transporto_priemone`
--

INSERT INTO `Semestras_Transporto_priemone` (`Numeris`, `Busena`, `id_Transporto_priemone`, `fk_Aikstele`) VALUES
('ABC222', 'Stovi', 1, 5),
('ABC123', 'Stovi', 2, 4),
('ABC423', 'Stovi', 3, 4),
('ABC143', 'Stovi', 4, 3),
('ABC413', 'Nebestovi', 5, 3),
('ABC223', 'Nebestovi', 6, 3),
('AB2123', 'Stovi', 7, 1),
('ABC690', 'Nebestovi', 8, 1),
('ABC739', 'Stovi', 9, 1),
('AB1129', 'Nebestovi', 10, 2),
('ABC753', 'Stovi', 11, 2),
('AB1123', 'Nebestovi', 12, 2),
('ABC890', 'Stovi', 13, 5),
('A11123', 'Nebestovi', 14, 5),
('ABC357', 'Stovi', 15, 5),
('GGG111', 'Stovi', 16, 2),
('GGG222', 'Stovi', 17, 2),
('GGG333', 'Stovi', 18, 2),
('BAD696', 'Stovi', 19, 2),
('HHD0E', 'Stovi', 20, 2),
('', 'Stovi', 21, 2),
('DDS38', 'Nebestovi', 22, 2);

-- --------------------------------------------------------

--
-- Sukurta duomenų struktūra lentelei `Test`
--

CREATE TABLE `Test` (
  `numeris` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Sukurta duomenų kopija lentelei `Test`
--

INSERT INTO `Test` (`numeris`) VALUES
(123456),
(123466);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Semestras_Aikstele`
--
ALTER TABLE `Semestras_Aikstele`
  ADD PRIMARY KEY (`id_Aikstele`),
  ADD UNIQUE KEY `fk_Kaina` (`fk_Kaina`),
  ADD KEY `fkc_Padalinys` (`fk_Padalinys`);

--
-- Indexes for table `Semestras_Imone`
--
ALTER TABLE `Semestras_Imone`
  ADD PRIMARY KEY (`El_Pastas`);

--
-- Indexes for table `Semestras_Kaina`
--
ALTER TABLE `Semestras_Kaina`
  ADD PRIMARY KEY (`id_Kaina`);

--
-- Indexes for table `Semestras_Padalinys`
--
ALTER TABLE `Semestras_Padalinys`
  ADD PRIMARY KEY (`id_Padalinys`),
  ADD KEY `fkc_Imone` (`fk_Imone`);

--
-- Indexes for table `Semestras_Stovejimo_laikas`
--
ALTER TABLE `Semestras_Stovejimo_laikas`
  ADD PRIMARY KEY (`id_Stovejimo_laikas`),
  ADD UNIQUE KEY `Kodas` (`Kodas`),
  ADD KEY `fkc_Transporto_priemone` (`fk_Transporto_priemone`) USING BTREE;

--
-- Indexes for table `Semestras_Transporto_priemone`
--
ALTER TABLE `Semestras_Transporto_priemone`
  ADD PRIMARY KEY (`id_Transporto_priemone`),
  ADD KEY `fkc_Aikstele` (`fk_Aikstele`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `Semestras_Stovejimo_laikas`
--
ALTER TABLE `Semestras_Stovejimo_laikas`
  MODIFY `id_Stovejimo_laikas` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `Semestras_Transporto_priemone`
--
ALTER TABLE `Semestras_Transporto_priemone`
  MODIFY `id_Transporto_priemone` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- Apribojimai eksportuotom lentelėm
--

--
-- Apribojimai lentelei `Semestras_Aikstele`
--
ALTER TABLE `Semestras_Aikstele`
  ADD CONSTRAINT `fkc_Kaina` FOREIGN KEY (`fk_Kaina`) REFERENCES `Semestras_Kaina` (`id_kaina`),
  ADD CONSTRAINT `fkc_Padalinys` FOREIGN KEY (`fk_Padalinys`) REFERENCES `Semestras_Padalinys` (`id_padalinys`);

--
-- Apribojimai lentelei `Semestras_Padalinys`
--
ALTER TABLE `Semestras_Padalinys`
  ADD CONSTRAINT `fkc_Imone` FOREIGN KEY (`fk_Imone`) REFERENCES `Semestras_Imone` (`el_pastas`);

--
-- Apribojimai lentelei `Semestras_Stovejimo_laikas`
--
ALTER TABLE `Semestras_Stovejimo_laikas`
  ADD CONSTRAINT `fkc_Transporto_priemone` FOREIGN KEY (`fk_Transporto_priemone`) REFERENCES `Semestras_Transporto_priemone` (`id_transporto_priemone`) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- Apribojimai lentelei `Semestras_Transporto_priemone`
--
ALTER TABLE `Semestras_Transporto_priemone`
  ADD CONSTRAINT `fkc_Aikstele` FOREIGN KEY (`fk_Aikstele`) REFERENCES `Semestras_Aikstele` (`id_aikstele`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
