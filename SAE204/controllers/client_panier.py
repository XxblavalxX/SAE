#! /usr/bin/python
# -*- coding:utf-8 -*-
from flask import Blueprint
from flask import Flask, request, render_template, redirect, url_for, abort, flash, session, g
import datetime

from connexion_db import get_db

client_panier = Blueprint('client_panier', __name__,
                        template_folder='templates')


@client_panier.route('/client/panier/add', methods=['POST'])
def client_panier_add():
    mycursor = get_db().cursor()
    article_id = request.form.get('idArticle', None)
    user_id = session['user_id']
    quantite = request.form.get('quantite')
    # print(type(quantite))
    # stock='''SELECT stock FROM voiture WHERE id_voiture=%s'''
    # mycursor.execute(stock , article_id)
    # stock=mycursor.fetchone()
    # print(stock)
    # sql='''UPDATE voiture SET stock = %s WHERE id_voiture=%s'''
    # mycursor.execute(sql , stock)
    tuple = (article_id, user_id)
    sql=''' SELECT stock FROM voiture WHERE id_voiture=%s'''
    mycursor.execute(sql, article_id)
    stock_voiture=mycursor.fetchone()
    # print(article_id , "okkkkkk")
    sql = ''' SELECT count(*) FROM panier WHERE id_voiture=%s AND id_user=%s'''

    mycursor.execute(sql, tuple)
    stock_panier = mycursor.fetchall()
    in_panier=stock_panier[0]['count(*)']
    # print( stock_panier[0]['count(*)'], "okksjhiukhqoiefhmreopjfkk ")
    print(in_panier , "in_panier")
    if in_panier != 0 :
        print("ok if1", "iojflxofih")
        sql = ''' SELECT sum(quantite) FROM panier WHERE id_voiture=%s AND id_user=%s'''
        mycursor.execute(sql, tuple)
        stock_panier = mycursor.fetchall()
        print(stock_panier[0]['sum(quantite)'], "sum quantitie")
        if stock_voiture['stock'] >= int(stock_panier[0]['sum(quantite)'])+int(quantite) :
            print("ok if2")
            sql = '''SELECT prix FROM voiture WHERE id_voiture=%s'''
            mycursor.execute(sql, article_id)
            prix = mycursor.fetchone()

            tuple = (prix['prix'], quantite, user_id, article_id , user_id , article_id)
            print(tuple)

            sql = '''UPDATE panier SET id_panier = NULL , date_ajout=CUREDATE() , prix_unitair=%s , quantite=%s , id_user=%s ,id_voiture=%s WHERE id_client=%s and id_voiture=%s'''
            mycursor.execute(sql, tuple)
            get_db().commit()

    if  in_panier == 0 :
        print ("ok if333333333333")
        sql = '''SELECT prix FROM voiture WHERE id_voiture=%s'''
        mycursor.execute(sql, article_id)
        prix = mycursor.fetchone()

        tuple = (prix['prix'], quantite, user_id, article_id)
        # print (tuple)

        sql = '''INSERT INTO panier (id_panier , date_ajout , prix_unitair , quantite , id_user ,id_voiture)
            VALUES (NULL , CURDATE() ,%s ,%s ,%s ,%s)'''
        mycursor.execute(sql, tuple)
        get_db().commit()

    # mycursor.commit()
    # tuple=int(stock['stock'])-int(quantite) ,

    # mycursor.execute(sql,tuple)
    # panier = mycursor.fetchall()

    return redirect('/client/article/show')
    #return redirect(url_for('client_index'))

@client_panier.route('/client/panier/delete', methods=['POST'])
def client_panier_delete():
    mycursor = get_db().cursor()
    user_id = session['user_id']

    sql='''DELETE FROM panier WHERE id_user=%s'''
    mycursor.execute(sql ,user_id)
    # print(user_id, "caca")
    get_db().commit()

    return redirect('/client/article/show')
    #return redirect(url_for('client_index'))


@client_panier.route('/client/panier/vider', methods=['POST'])
def client_panier_vider():
    mycursor = get_db().cursor()

    return redirect('/client/article/show')
    #return redirect(url_for('client_index'))


@client_panier.route('/client/panier/delete/line', methods=['POST'])
def client_panier_delete_line():
    mycursor = get_db().cursor()

    return redirect('/client/article/show')
    #return redirect(url_for('client_index'))


@client_panier.route('/client/panier/filtre', methods=['POST'])
def client_panier_filtre():
    sql="SELECT *  From type_voiture"

    filter_word = request.form.get('filter_word', None)
    filter_prix_min = request.form.get('filter_prix_min', None)
    filter_prix_max = request.form.get('filter_prix_max', None)
    filter_types = request.form.getlist('filter_types', None)
    # sql='''SELECT * FROM panier WHERE id_voiture = %s AND prix<%s AND prix_unitair>%s AND id_type_voiture =%s '''
    return redirect('/client/article/show')
    #return redirect(url_for('client_index'))


@client_panier.route('/client/panier/filtre/suppr', methods=['POST'])
def client_panier_filtre_suppr():
    session.pop('filter_word', None)
    session.pop('filter_prix_min', None)
    session.pop('filter_prix_max', None)
    session.pop('filter_types', None)
    # print("suppr filtre")
    return redirect('/client/article/show')
    #return redirect(url_for('client_index'))
