-- MySQL Workbench Forward Engineering
SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0; SET @OLD_SQL_MODE=@@SQL_MODE,
SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- Schema mydb



-- Schema mydb

CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8mb3 ;
USE `mydb` ;

-- Table `mydb`.`Categoria`

CREATE TABLE IF NOT EXISTS `mydb`.`Categoria` (
`id_Categoria` INT NOT NULL AUTO_INCREMENT,
`Nome` VARCHAR(100) NOT NULL,
`Descricao` VARCHAR(255) NOT NULL, PRIMARY KEY (`id_Categoria`))
ENGINE = InnoDB;


-- Table `mydb`.`Cadastro_Produto`

CREATE TABLE IF NOT EXISTS `mydb`.`Cadastro_Produto` (
`id_Cadastro_Produto` INT NOT NULL AUTO_INCREMENT,
`Nome` VARCHAR(100) NOT NULL,
`Descricao` VARCHAR(255) NOT NULL, PRIMARY KEY (`id_Cadastro_Produto`))
ENGINE = InnoDB;


-- Table `mydb`.`Usuario`

CREATE TABLE IF NOT EXISTS `mydb`.`Usuario`(
`id_Usuario` INT NOT NULL AUTO_INCREMENT,
`Nome` VARCHAR(100) NOT NULL,
`Email` VARCHAR(50) NOT NULL,
`Telefone` VARCHAR(20) NOT NULL,
`Senha` VARCHAR(255) NOT NULL,
`Preferencia` ENUM('Troca', 'Doação', "Receber Doação") NOT NULL,
`Tipo_Conta` ENUM('Pessoal', 'ONG', 'Instituição') NOT NULL, PRIMARY KEY (`id_Usuario`),
UNIQUE INDEX `Email_UNIQUE` (`Email` ASC) VISIBLE) ENGINE = InnoDB;


-- Table `mydb`.`Produto`

CREATE TABLE IF NOT EXISTS `mydb`.`Produto` (
`id_Produto` INT NOT NULL AUTO_INCREMENT,
`Nome` VARCHAR(100) NOT NULL,
`Descricao` VARCHAR(255) NOT NULL,
`Imagem_url` VARCHAR(255) NOT NULL,
`Criado_em` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
`Estado` ENUM('novo', 'semi-novo', 'usado') NOT NULL,
`Status` ENUM('disponivel', 'reservado', 'doado') NOT NULL,
`Cadastro_Produto_id_Cadastro_Produto` INT NOT NULL,
`Usuario_id_Usuario` INT NOT NULL,
`Categoria_id_Categoria` INT NOT NULL, PRIMARY KEY (`id_Produto`),
INDEX `fk_Produto_Cadastro_Produto1_idx` (`Cadastro_Produto_id_Cadastro_Produto` ASC) VISIBLE,
INDEX `fk_Produto_Usuario1_idx` (`Usuario_id_Usuario` ASC) VISIBLE, INDEX `fk_Produto_Categoria1_idx` (`Categoria_id_Categoria` ASC) VISIBLE, CONSTRAINT `fk_Produto_Cadastro_Produto1`
FOREIGN KEY (`Cadastro_Produto_id_Cadastro_Produto`) REFERENCES `mydb`.`Cadastro_Produto` (`id_Cadastro_Produto`) ON DELETE NO ACTION
ON UPDATE NO ACTION,
CONSTRAINT `fk_Produto_Usuario1` FOREIGN KEY (`Usuario_id_Usuario`)
REFERENCES `mydb`.`Usuario` (`id_Usuario`) ON DELETE NO ACTION
ON UPDATE NO ACTION,
CONSTRAINT `fk_Produto_Categoria1` FOREIGN KEY (`Categoria_id_Categoria`)
REFERENCES `mydb`.`Categoria` (`id_Categoria`) ON DELETE NO ACTION
ON UPDATE NO ACTION) ENGINE = InnoDB;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS; SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;


