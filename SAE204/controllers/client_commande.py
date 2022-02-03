#! /usr/bin/python
# -*- coding:utf-8 -*-
from flask import Blueprint
from flask import Flask, request, render_template, redirect, url_for, abort, flash, session, g
from datetime import datetime
from connexion_db import get_db

client_commande = Blueprint('client_commande', __name__,
                        template_folder='templates')


@client_commande.route('/client/commande/add', methods=['POST'])
def client_commande_add():
    mycursor = get_db().cursor()

    sql='''INSERT INTO commande (id_commande , date_achat ,id_user , id etat) VALUES (NULL , )'''
    flash(u'Commande ajoutée')
    return redirect('/client/article/show')
    #return redirect(url_for('client_index'))



@client_commande.route('/client/commande/show', methods=['get','post'])
def client_commande_show():
    mycursor = get_db().cursor()

    sql= '''SELECT * FROM commande '''
    mycursor.execute(sql)
    commandes = mycursor.fetchall()

    sql = '''SELECT * FROM panier '''
    mycursor.execute(sql)
    articles_commande= mycursor.fetchall()
    return render_template('client/commandes/show.html', commandes=commandes, articles_commande=articles_commande)

