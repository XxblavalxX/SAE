DROP TABLE IF EXISTS panier ;
DROP TABLE IF EXISTS ligne_commande ;
DROP TABLE IF EXISTS commande ;
DROP TABLE IF EXISTS commentaire ;
DROP TABLE IF EXISTS voiture ;
DROP TABLE IF EXISTS type_voiture ;
DROP TABLE IF EXISTS etat ;
DROP TABLE IF EXISTS user ;







CREATE TABLE user (
    id_user INT AUTO_INCREMENT,
    username VARCHAR(50),
    password VARCHAR(255),
    role VARCHAR(50),
    est_actif VARCHAR(50),
    pseudo VARCHAR(50),
    email VARCHAR(50),
    PRIMARY KEY (id_user)
    );

CREATE TABLE type_voiture
(
    id_type_voiture      INT AUTO_INCREMENT,
    libelle_type_voiture VARCHAR(255),
    PRIMARY KEY (id_type_voiture)
);


CREATE TABLE voiture(
   id_voiture INT AUTO_INCREMENT,
   marque VARCHAR(50),
#    type_voiture VARCHAR(50),
   modele VARCHAR(50),
   prix INT,
   image  VARCHAR(255) ,
   id_type_voiture INT ,
   stock INT,
   PRIMARY KEY(id_voiture),
   CONSTRAINT fk_voiture_type_voiture FOREIGN KEY  (id_type_voiture) REFERENCES type_voiture(id_type_voiture)

);

CREATE TABLE commentaire (
    id_commentaire INT AUTO_INCREMENT ,
    libelle_commentaire VARCHAR(255),
    id_voiture INT ,
    PRIMARY KEY (id_commentaire) ,
    CONSTRAINT fk_commentaire_voiture FOREIGN KEY  (id_voiture) REFERENCES voiture(id_voiture)


) ;




CREATE TABLE etat (
    id_etat INT AUTO_INCREMENT,
    libelle VARCHAR(50),
    PRIMARY KEY (id_etat)
    );


CREATE TABLE commande (
    id_commande INT AUTO_INCREMENT,
    date_achat DATE,
    id_user INT ,
    id_etat INT,
    PRIMARY KEY (id_commande) ,
    CONSTRAINT fk_commande_user FOREIGN KEY  (id_user) REFERENCES user(id_user),
    CONSTRAINT fk_commande_etat FOREIGN KEY  (id_etat) REFERENCES etat(id_etat)
    );



CREATE TABLE ligne_commande (
    prix_unit INT,
    quantite INT,
    id_commande INT ,
    id_voiture INT,
    PRIMARY KEY (prix_unit) ,
    CONSTRAINT fk_ligne_commande_commande FOREIGN KEY  (id_commande) REFERENCES commande(id_commande),
    CONSTRAINT fk_ligne_commande_voiture FOREIGN KEY  (id_voiture) REFERENCES voiture(id_voiture)
    );



CREATE TABLE panier (
    id_panier INT AUTO_INCREMENT ,
    date_ajout DATE,
    prix_unitair INT ,
    quantite INT ,
    id_user INT ,
    id_voiture INT,
    PRIMARY KEY (id_panier) ,
    CONSTRAINT fk_panier_user FOREIGN KEY  (id_user) REFERENCES user(id_user),
    CONSTRAINT fk_panier_etat FOREIGN KEY  (id_voiture) REFERENCES voiture(id_voiture)
    );

INSERT INTO user (id_user, email, username, password, role,  est_actif) VALUES
(NULL, 'admin@admin.fr', 'admin', 'sha256$pBGlZy6UukyHBFDH$2f089c1d26f2741b68c9218a68bfe2e25dbb069c27868a027dad03bcb3d7f69a', 'ROLE_admin', 1);
INSERT INTO user  (id_user, email, username, password, role, est_actif) VALUES
(NULL, 'client@client.fr', 'client', 'sha256$Q1HFT4TKRqnMhlTj$cf3c84ea646430c98d4877769c7c5d2cce1edd10c7eccd2c1f9d6114b74b81c4', 'ROLE_client', 1);
INSERT INTO user  (id_user, email, username, password, role,  est_actif) VALUES
(NULL, 'client2@client2.fr', 'client2', 'sha256$ayiON3nJITfetaS8$0e039802d6fac2222e264f5a1e2b94b347501d040d71cfa4264cad6067cf5cf3', 'ROLE_client',1);



LOAD DATA LOCAL INFILE '/home/laval/Bureau/SAE204/TYPEVOITURE.csv' INTO TABLE type_voiture FIELDS TERMINATED BY ',';
LOAD DATA LOCAL INFILE '/home/laval/Bureau/SAE204/VOITURE.csv' INTO TABLE voiture FIELDS TERMINATED BY ',';

select * from user ;

select * from voiture ;

