-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost
-- Tiempo de generación: 15-11-2021 a las 05:51:18
-- Versión del servidor: 10.4.21-MariaDB
-- Versión de PHP: 8.0.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `sistema_de_inventario`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `colaborador`
--

CREATE TABLE `colaborador` (
  `id` int(11) NOT NULL,
  `username` varchar(80) NOT NULL,
  `codigoDeIdentificacion` varchar(80) NOT NULL,
  `puesto` varchar(120) DEFAULT NULL,
  `rol` varchar(100) NOT NULL,
  `fotografia` varchar(2000) NOT NULL,
  `descripcion` varchar(2000) NOT NULL,
  `anotacionDeGerente` varchar(2000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `colaborador`
--

INSERT INTO `colaborador` (`id`, `username`, `codigoDeIdentificacion`, `puesto`, `rol`, `fotografia`, `descripcion`, `anotacionDeGerente`) VALUES
(1, 'Pamela', '134000228225', 'fronterr', 'Programadorr', 'https://d2skuhm0vrry40.cloudfront.net/2021/articles/2021-05-18-11-01/pokemon-go-luminous-legends-y-header.jpg/EG11/resize/1200x-1/pokemon-go-luminous-legends-y-header.jpg', 'Muy competitiva', 'Excelente colaboradora'),
(2, 'Adonis', '503910258', 'fronter', 'Programador master', 'https://scontent.fsyq6-1.fna.fbcdn.net/v/t1.6435-9/147630760_2821949361353840_3634859273946931384_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=09cbfe&_nc_ohc=LiTZ95Gp9XwAX-2Pl4n&_nc_oc=AQn9U91Yod_49ZSZFNPdE_fgRLDA3w85TJKV2_RE0ZDlGQtLshG15bWrl5eW00OKWMA&_nc_ht=scontent.fsyq6-1.fna&oh=0bb8401300da4dbe1fdbb8af223d9b5f&oe=61B7B70E', 'modelo de DIos ', 'Excelente trabajos'),
(3, 'Danna', '23847467373773', 'ejectuva', 'Administradora ', 'https://scontent.fsyq6-1.fna.fbcdn.net/v/t1.6435-9/67732821_2376902562525191_4720042498502688768_n.jpg?_nc_cat=111&ccb=1-5&_nc_sid=174925&_nc_ohc=ZCHH_i6fIfcAX8mHPtc&tn=A3eNAohE2uNnQ81s&_nc_ht=scontent.fsyq6-1.fna&oh=ba1ab411a971336440f31f0e867d7f46&oe=61B8DA87', 'Competitiva', 'Excelencia '),
(4, 'Pedro', '45552525255', 'Reclutador', 'recursos humanos', 'https://destinonegocio.com/wp-content/uploads/2016/02/ico-destinonegocio-recursos-humanos-en-las-empresas-istock-getty-images-1030x685.jpg', 'Competitivo', 'Excelencia en todo');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `username` varchar(80) NOT NULL,
  `codigoDeIdentificacion` varchar(80) NOT NULL,
  `precio` varchar(120) DEFAULT NULL,
  `categoria` varchar(100) NOT NULL,
  `fotografia` varchar(100) NOT NULL,
  `descripcion` varchar(2000) NOT NULL,
  `anotacionDeGerente` varchar(2000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `user`
--

INSERT INTO `user` (`id`, `username`, `codigoDeIdentificacion`, `precio`, `categoria`, `fotografia`, `descripcion`, `anotacionDeGerente`) VALUES
(1, 'Blastoise', '12300045', '14000', 'jxcvhkzhsvkxckjvhzxckjvhxjckv', 'https://assets.pokemon.com/assets/cms2/img/pokedex/full/009.png', 'muy bien producto', 'Esta todo muy bien hecho'),
(2, 'Arroz Luisiana', '12300043', '13000', 'Carboidratos', 'https://superviquez.com/image/cache/catalog/Productos/40452650-1000x1000.png', 'De muy buena calidad el arroz', 'Excelente calidad'),
(3, 'Frijoles montiel', '12300050', '13555', 'Embrudos', 'https://m.media-amazon.com/images/I/71-7iyA5v2L._SX679_.jpg', 'frijole de calidad', 'Esquisitos trabajo');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `colaborador`
--
ALTER TABLE `colaborador`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `colaborador`
--
ALTER TABLE `colaborador`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
