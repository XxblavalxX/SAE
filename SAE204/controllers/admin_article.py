#! /usr/bin/python
# -*- coding:utf-8 -*-
from flask import Blueprint
from flask import Flask, request, render_template, redirect, url_for, abort, flash, session, g

from connexion_db import get_db

admin_article = Blueprint('admin_article', __name__,
                        template_folder='templates')

@admin_article.route('/admin/article/show')
def show_article():
    mycursor = get_db().cursor()
    sql = ''' SELECT * FROM voiture '''
    mycursor.execute(sql)
    articles = mycursor.fetchall()
    print(articles)
    return render_template('admin/article/show_article.html', articles=articles)

@admin_article.route('/admin/article/add', methods=['GET'])
def add_article():
    mycursor = get_db().cursor()
    types_articles = ''' SELECT * FROM type_voiture'''
    return render_template('admin/article/add_article.html', types_articles=types_articles)

@admin_article.route('/admin/article/add', methods=['POST'])
def valid_add_article():
    marque = request.form.get('nom', '')
    type_article_id = request.form.get('type_article_id', '')
    type_article_id = int(type_article_id)
    prix = request.form.get('prix', '')
    stock = request.form.get('stock', '')
    modele = request.form.get('description', '')
    image = request.form.get('image', '')
    tuple( "null" , marque , modele ,prix , image ,type_article_id)
    sql = ''' INSERT INTO voiture ( id_voiture ,   marque , modele , prix , image , type_voiture ) VALUES ( %s,%s,%s,%s,%s,%s,%s) '''
    mycursor.execute(sql , tuple)


    print(u'article ajouté , nom: ', nom, ' - type_article:', type_article_id, ' - prix:', prix, ' - stock:', stock, ' - description:', description, ' - image:', image)
    message = u'article ajouté , nom:'+nom + '- type_article:' + type_article_id + ' - prix:' + prix + ' - stock:'+  stock + ' - description:' + description + ' - image:' + image
    flash(message)
    return redirect(url_for('admin_article.show_article'),articles=articles)

@admin_article.route('/admin/article/delete', methods=['POST'])
def delete_article():
    # id = request.args.get('id', '')
    id = request.form.get('id', '')

    print("un article supprimé, id :", id)
    flash(u'un article supprimé, id : ' + id)
    return redirect(url_for('admin_article.show_article'))

@admin_article.route('/admin/article/edit/<int:id>', methods=['GET'])
def edit_article(id):
    mycursor = get_db().cursor()
    sql='''SELECT * FROM voiture'''
    mycursor.execute(sql)
    article = mycursor.fetchall()
    sql='''SELECT * FROM type_voiture'''
    mycursor.execute()
    types_articles = mycursor.fetchall()

    return render_template('admin/article/edit_article.html', article=article, types_articles=types_articles)

@admin_article.route('/admin/article/edit', methods=['POST'])
def valid_edit_article():
    marque = request.form['nom']
    id_voiture = request.form.get('id', '')
    id_type_voiture = request.form.get('type_article_id', '')
    #type_article_id = int(type_article_id)
    prix = request.form.get('prix', '')
    stock = request.form.get('stock', '')
    modele = request.form.get('description', '')
    image = request.form.get('image', '')
    tuple =(prix ,id_type_voiture ,stock ,modele, image ,id_voiture)
    sql='''UPDATE  voiture 
    SET prix=%s
    id_type_voiture=%s
    stock=%s
    modele=%s 
    image =%s
    WHERE id_voiture = %s
    '''
    mycursor.execute(sql, tuple)

    print(u'article modifié , nom : ', nom, ' - type_article:', type_article_id, ' - prix:', prix, ' - stock:', stock, ' - description:', description, ' - image:', image)
    message = u'article modifié , nom:'+nom + '- type_article:' + type_article_id + ' - prix:' + prix + ' - stock:'+  stock + ' - description:' + description + ' - image:' + image
    flash(message)
    return redirect(url_for('admin_article.show_article'))
