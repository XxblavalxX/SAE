#! /usr/bin/python
# -*- coding:utf-8 -*-
from flask import Blueprint
from flask import Flask, request, render_template, redirect, url_for, abort, flash, session, g

from connexion_db import get_db

client_commentaire = Blueprint('client_commentaire', __name__,
                        template_folder='templates')

@client_commentaire.route('/client/comment/add', methods=['POST'])
def client_comment_add():
    mycursor = get_db().cursor()
    article_id = request.form.get('idArticle', None)
    commentaire= request.form.get('inputAvis',None)
    tuple=(NULL ,commentaire)
    sql='''INSERT INTO commentaire (id_commentaire , libelle_commentaire , id_voiture)VALUES (NULL ,"patate", %s ) '''
    mycursor.execute(sql , article_id)

    return redirect('/client/article/details/'+article_id)
    #return redirect(url_for('client_article_details', id=int(article_id)))

@client_commentaire.route('/client/comment/delete', methods=['POST'])
def client_comment_detete():
    mycursor = get_db().cursor()
    article_id = request.form.get('idArticle', None)
    sql='''DELETE FROM commentaire WHERE id_voiture=%s'''
    mycursor.execute(sql ,  article_id)

    return redirect('/client/article/details/'+article_id)
    #return redirect(url_for('client_article_details', id=int(article_id)))