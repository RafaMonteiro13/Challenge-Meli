-- MySQL dump 10.13  Distrib 8.0.42, for Win64 (x86_64)
--
-- Host: localhost    Database: DriveDocuments
-- ------------------------------------------------------
-- Server version	8.0.42

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `files`
--

DROP TABLE IF EXISTS `files`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `files` (
  `id` varchar(150) NOT NULL,
  `name` varchar(260) NOT NULL,
  `extension` varchar(200) NOT NULL,
  `owner` varchar(300) NOT NULL,
  `lastModify` varchar(200) NOT NULL,
  `visibility` enum('True','False') DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `files`
--

LOCK TABLES `files` WRITE;
/*!40000 ALTER TABLE `files` DISABLE KEYS */;
INSERT INTO `files` VALUES ('0BxUeU__vcP6Ffjg2VWROdl8yVjJuUkJnUDI3R1JyODdmaUdVME5DSWpxWXoxS3FCMVZWUDA','Classroom','application/vnd.google-apps.folder','rafaelmonteirocaldas@gmail.com','2018-03-08T00:15:50.700Z','False'),('0BxUeU__vcP6FfllVcjNyUGplcFpGRjJMS0hGVjRtcUtuOVRLT0lfaWczNFlDUFliTVVSMmM','TERCEIR├âO IBI├ÜNA VESTIBULAR 2018','application/vnd.google-apps.folder','rafaelmonteirocaldas@gmail.com','2018-03-08T00:15:50.700Z','False'),('1_-1cBU2vaO9oY7D-4MuQEdUKGiY4rUVM','Frequ├¬ncias','application/vnd.google-apps.folder','ualgcbl2020@gmail.com','2020-11-03T21:42:52.062Z','True'),('1_CZoDXF9jFbBHJpXN3PJzJLNwjjzqZWi','Fase 3  - Tech Challenge_Rafael_Monteiro - Forensics.docx','application/vnd.openxmlformats-officedocument.wordprocessingml.document','rafaelmonteirosouza123@gmail.com','2025-03-24T20:20:53.000Z','False'),('1_QtYbRBj8zsNe6UWQGUzq9MsAaHkXA_U','Keycloak_AP1.pdf','application/pdf','rafaelmonteirosouza123@gmail.com','2025-03-26T18:15:30.000Z','False'),('10TB3KLbor1d5uAtxBkLWtiP-YmoJuCGb','Sociedade dos Poetas Mortos ','application/vnd.google-apps.folder','guipedrozo0705@gmail.com','2023-12-08T20:52:03.208Z','True'),('11w5lIkeXqZ4ECUPv01v8D2e0ZiViQuXe','04. Nutri├º├úo, Metabolismo e Regula├º├úo da Temperatura.pdf','application/pdf','ualgcbl2020@gmail.com','2020-10-17T16:56:27.000Z','True'),('12k0ZPi3RWuc_nSHFEgCUDVQUtFwN2Isr','Anatomofisiologia 1','application/vnd.google-apps.folder','ualgcbl2020@gmail.com','2020-11-21T22:13:35.005Z','True'),('13hhvs3yLKf2XMBb-MXbOJl70RPjsyKvR','Evid├¬ncias_GoPhishing.docx','application/vnd.openxmlformats-officedocument.wordprocessingml.document','rafaelmonteirosouza123@gmail.com','2024-09-27T13:34:38.000Z','False'),('16tlXrBjd7PdBwHgKQ6clN95fGEA4FhlA','Historico_Faculdade.pdf','application/pdf','rafaelmonteirosouza123@gmail.com','2024-08-27T14:39:22.000Z','False'),('17KRk_UOlA4GqOiXQ6i6viAUiowGCSZ45','TIAGO_CARDOSO Curr├¡culo - TemplatE_MODELO TESTE.docx','application/vnd.openxmlformats-officedocument.wordprocessingml.document','tcsdudu1@gmail.com','2024-07-22T17:57:40.568Z','True'),('17ZW-ySgmy6SSEf0BIBXcDQnheA1do4r5','Documenta├º├úo Instala├º├úo.zip','application/zip','paulorbindo@gmail.com','2019-11-06T01:21:20.627Z','True'),('18usApKt50-DHF9jegozcyaKP5wEBQNxN','UC - ├ëTICA e L├ôGICA','application/vnd.google-apps.folder','orthmannpatricia@gmail.com','2023-09-01T01:34:35.146Z','True'),('19GRmOv2io-0m-0ohAD-tQCtbSROPE01V','Projeto The Last Of Us - Grupo 10','application/vnd.google-apps.folder','rafaelmonteirocaldas@gmail.com','2023-11-29T13:50:12.515Z','True'),('1aMyG6lYP_3iqX0reu-Wh-8XPjbzWFMbwC-lPLPUGW5s','Aborto slides','application/vnd.google-apps.presentation','rafaelmonteirocaldas@gmail.com','2017-06-13T18:04:49.752Z','False'),('1b_f0RVEBeokyaKQmq_htMlTXiEDq_7cgRjj7yTjBv5w','Game Design Document','application/vnd.google-apps.document','wenes78@gmail.com','2019-03-09T23:26:44.092Z','True'),('1bAEzK0_CmkZxt8XGdbKQkt3pfxJcCMtB','Dilemas das redes sociais','application/vnd.google-apps.folder','chaampzz10@gmail.com','2023-12-07T23:45:59.707Z','True'),('1by0NdePJd-svKiKuaUWWxBysASJufG7UQ9rF9kNe6_4','RAFAEL_MONTEIRO Curr├¡culo','application/vnd.google-apps.document','rafaelmonteirocaldas@gmail.com','2024-09-27T14:47:30.282Z','False'),('1C5jwdWcRA6qQL_yS5B6f8JkuVgySN4re','Shinobu Print.pdf','application/pdf','carolineviannafarah@gmail.com','2021-09-10T17:45:09.000Z','True'),('1DGiikfumLhRr89eznDdWdA09T-Mn-S7f','access.log','text/plain','arquivosexternosmbafiap@gmail.com','2023-04-13T16:38:25.000Z','True'),('1DH6Bnp8lviTl_O4vUlKJtMu30386hR1r','km_20231122-2_720p_60f_20231122_191941.mp4','video/mp4','jorgejuniorvencedor@gmail.com','2023-11-22T22:51:36.071Z','True'),('1DNy-3s0stwCidzHGELmsMFZwIyKSHCNA','Aula 01.ipynb','application/vnd.google.colaboratory','cedmenezes@gmail.com','2022-03-04T22:35:20.224Z','True'),('1DOHFc2MhDhiJq891o3IyXoVL12XrYp-7','09. Sistema Muscular ÔÇô Cabe├ºa e Pesco├ºo.pdf','application/pdf','ualgcbl2020@gmail.com','2020-11-08T19:27:36.000Z','True'),('1EELBJbtZvmvmKrTLDbSeJzq0qrpxA4Ot','Colab Notebooks','application/vnd.google-apps.folder','rafaelmonteirocaldas@gmail.com','2022-09-13T22:36:08.805Z','False'),('1EyWHpxYYh4Bn94oauMF2LltKtwAgrEicWitf8lZgr7EkufW4-xXCQk6uD5V0UlJ2W-4Y7D4','Rafael Monteiro - Atividade 02 - Final','application/vnd.google-apps.shortcut','rafaelmonteirocaldas@gmail.com','2021-11-24T22:09:35.447Z','False'),('1FaZyzAtI2dhQFqW5nsajvde3xtgxu_b6','api-guide.html','text/html','rafaelmonteirosouza123@gmail.com','2024-07-24T15:12:55.000Z','False'),('1FBmejs3PYIWyIYyZVZKOaNpAuBaLD3Nw','A3 - CORE-CURRICULUM - wanderson gomes (1).pdf','application/pdf','natalia.almeida@saojudas.br','2023-10-27T00:34:35.000Z','True'),('1GBAya6AknAs_zx7V4YJZPei0V4I6zMfO','Atividade 6_221003_205720 (1).pdf','application/pdf','alef.developerweb@gmail.com','2022-10-03T23:59:02.208Z','True'),('1GdXQdYcrsN6E3u4dN7WamQ6iwNWnYYRY32vgl3n0eg4MALYM0jgIURGas_OuX7qRn7vzY8Y','Rafael Monteiro - Ingl├¬s Instrumental Atividade Final.docx','application/vnd.google-apps.shortcut','rafaelmonteirocaldas@gmail.com','2021-11-02T13:59:19.149Z','False'),('1gno3q_-Hp9UuB5wlr43Eqhw2eQm7O_Sl','08. Introdu├º├úo aos M├║sculos e Reflexos.pdf','application/pdf','ualgcbl2020@gmail.com','2020-10-31T10:23:46.000Z','True'),('1gSrEvR-vYNWmiuBH3w39XMkTDmcO8zXq','Pos Tech - CBTT - Cyberlaw  - Aula 4 - Efeito Snowden_Marco Civil da Internet.pdf','application/pdf','rafaelmonteirosouza123@gmail.com','2024-11-25T19:18:19.000Z','False'),('1Hm2NMoHv8XOQAjw2stRpCcZVf5gdWaVJ','Ingl├¬s Instrumental - Aula 2 - 18.08.21.pptx','application/vnd.openxmlformats-officedocument.presentationml.presentation','drikatoguchi@gmail.com','2021-08-18T17:57:46.000Z','True'),('1I3edSdS6WcsgHpeDCOmzPCTqjb0-_oZC','PrivacyNoticeForJob (1).pdf','application/pdf','vickynhamah95@gmail.com','2024-02-14T20:28:18.784Z','True'),('1J3aNB-vxzld5EllM-K39K-Ok1JRY9XLF','03. Histologia dos Tecidos.pdf','application/pdf','ualgcbl2020@gmail.com','2020-11-08T19:27:15.201Z','True'),('1Jj6r7Eszv0_V4wazj7b4sh2kiO4nQoka','TUTORIAL AVALIA├ç├âO A2 2022.2.pdf','application/pdf','geravaliacao@gmail.com','2022-09-14T20:29:12.000Z','True'),('1JsNHo_WiTlxtdtroMJr5DfBd02xWv-t9','caderno-amarelo-enem-2018-dia-2.pdf','application/pdf','redepassaporte@gmail.com','2018-11-11T22:51:20.726Z','True'),('1lg1rYUd7VWBUH5YsS6ml1XnTFBmQ5ui3Mb66mpb5VFk','Documento sem t├¡tulo','application/vnd.google-apps.document','rafaelmonteirocaldas@gmail.com','2019-05-24T13:55:16.935Z','False'),('1lSrPwNv6yDNOu5OtwGuPsURfS35oLxhIC781Mg4ILIs','localDeProva','application/vnd.google-apps.document','rafaelmonteirocaldas@gmail.com','2019-11-02T16:46:22.724Z','False'),('1mH3Zp67dDhSbjz_FRzumuDtvQL4080yh','10. Sistema Muscular ÔÇô Tronco e Membros.pdf','application/pdf','ualgcbl2020@gmail.com','2020-11-08T19:27:45.000Z','True'),('1mkmxucAeQGNZMsiroTLmDen1IvlShFmJxUFzdVmLllnACELz0ly1PZVgEY0l_wx-_eotq2LJ','Inova├º├úo e Sustentabilidade Projeto A3','application/vnd.google-apps.folder','rafaelmonteirocaldas@gmail.com','2023-11-02T18:38:24.363Z','False'),('1MSAf-4a3qAU77W6_tAvtQLsZkwCL9g3S','Ingl├¬s Instrumental - Aula 1 - 16.08.21.pptx','application/vnd.openxmlformats-officedocument.presentationml.presentation','drikatoguchi@gmail.com','2021-08-15T15:18:21.000Z','True'),('1npWSZ1QWQXV6sXpO_i1crOmm6Oto3-RN','TUTORIAL AVALIA├ç├âO A1 - 2022.1.pdf','application/pdf','guilherme.messias.lima@gmail.com','2022-04-01T12:23:24.000Z','True'),('1OSRKwzkdLr7MAxiv_uMA0ulIsx8rPMzm','outros ficheiros','application/vnd.google-apps.folder','ualgcbl2020@gmail.com','2020-11-01T15:33:35.179Z','True'),('1qeIloECfMENCVWq99FUcu4nCjHDQOcfyyrhy2WpPuFE','A2 - FAQ ALUNOS','application/vnd.google-apps.document','geravaliacao@gmail.com','2024-01-27T16:36:53.260Z','True'),('1qvCsxGQyczIySxSlidbWBdwn1gd8Iutu','cyber - Pos Tech','application/vnd.google-apps.folder','arquivosexternosmbafiap@gmail.com','2023-04-13T17:38:03.513Z','True'),('1QvuFZfusPLH9CDLvaKBjpa42SaXaQp4A','arp.pcap','application/cap','arquivosexternosmbafiap@gmail.com','2023-04-13T16:38:29.000Z','True'),('1th_2yvIV_SE3_w66Lv7jwkykwPMlM8OpZYvJZbrtlY0','Documento Externo 43126.2024\\_Respondido','application/vnd.google-apps.document','rafaelmonteirocaldas@gmail.com','2024-11-21T19:01:46.357Z','False'),('1tK1Nup2dHIjEs68OcBT8_GspCCZHlMGx','http.cap','image/cap','arquivosexternosmbafiap@gmail.com','2023-04-13T16:38:33.000Z','True'),('1tzVB0TznHffESrH-DqfssfKdDfywJAdGM26Hxqk3Y4A','Guerra Cibern├®tica 2','application/vnd.google-apps.document','juliapereira240300@gmail.com','2023-05-23T20:53:54.940Z','False'),('1u1_BB0QIPmhvCxXOjtnsf1uvNqSrfpwv','Documento Externo 43126.2024.pdf','application/pdf','rafaelmonteirocaldas@gmail.com','2024-11-11T16:44:53.000Z','False'),('1unk_upGcjuCHz1b54exqKkQQkarMtoCV','TRABALHOS A3','application/vnd.google-apps.folder','natalia.almeida@saojudas.br','2023-10-27T00:31:08.430Z','True'),('1uvSwmFdnopYIdRxkLve9z4vWxHnqbhaXbInWUSIF8iSBN1uAo76Dci_xlJkyVkKSciLftiPv','Ingl├¬s Instrumental - Adri','application/vnd.google-apps.folder','rafaelmonteirocaldas@gmail.com','2021-08-23T14:26:24.825Z','False'),('1v2HBvLLkKWZ95g4mI4RCrGD7oTZWCkoJ','Slide Netflix - Urso Branco (1).pptx','application/vnd.openxmlformats-officedocument.presentationml.presentation','natalia.almeida@saojudas.br','2023-11-28T04:30:55.125Z','True'),('1vDiqe41JwATbenF3Xxcy0qQdTDBUZoHA','teste','application/vnd.google-apps.folder','juliapereira240300@gmail.com','2024-01-26T21:12:36.967Z','True'),('1VZ5bogxcg8qGP1OdVtK2FL6Ct_Qp1xpj','Ingl├¬s Instrumental - Aula 3 - 23.08.21.pptx','application/vnd.openxmlformats-officedocument.presentationml.presentation','drikatoguchi@gmail.com','2021-08-23T18:41:41.000Z','True'),('1wzQ0b63snDRIVxvEyEc10hX9NFbfGSgY','icmp_ping.pcap','application/cap','arquivosexternosmbafiap@gmail.com','2023-04-13T16:38:30.000Z','True'),('1XG5I591ZT4jS7_gIQi9WeSUYQvTAHEZw','FILATTE - PROVAS ANTERIORES','application/vnd.google-apps.folder','felipefilatte@gmail.com','2021-08-13T16:27:33.067Z','True');
/*!40000 ALTER TABLE `files` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `logfiles`
--

DROP TABLE IF EXISTS `logfiles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `logfiles` (
  `id` varchar(100) NOT NULL,
  `name` varchar(255) NOT NULL,
  `visibility` enum('True','False') DEFAULT NULL,
  `owner` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `logfiles`
--

LOCK TABLES `logfiles` WRITE;
/*!40000 ALTER TABLE `logfiles` DISABLE KEYS */;
INSERT INTO `logfiles` VALUES ('17KRk_UOlA4GqOiXQ6i6viAUiowGCSZ45','TIAGO_CARDOSO Curr├¡culo - TemplatE_MODELO TESTE.docx','True','tcsdudu1@gmail.com'),('1by0NdePJd-svKiKuaUWWxBysASJufG7UQ9rF9kNe6_4','RAFAEL_MONTEIRO Curr├¡culo','True','rafaelmonteirocaldas@gmail.com'),('1I3edSdS6WcsgHpeDCOmzPCTqjb0-_oZC','PrivacyNoticeForJob (1).pdf','True','vickynhamah95@gmail.com'),('1lSrPwNv6yDNOu5OtwGuPsURfS35oLxhIC781Mg4ILIs','localDeProva','True','rafaelmonteirocaldas@gmail.com'),('1tzVB0TznHffESrH-DqfssfKdDfywJAdGM26Hxqk3Y4A','Guerra Cibern├®tica 2','True','juliapereira240300@gmail.com');
/*!40000 ALTER TABLE `logfiles` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-04-29 17:25:17
