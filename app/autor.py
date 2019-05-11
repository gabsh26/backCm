from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('autor', __name__)

@bp.route('/autor', methods=('GET'))
def index():
    db = get_db()
    ano = request.form['startDate']
    ano2 = request.form['endDate']
    area = request.form['area']
    authors = request.form['authors']
    result = db.execute(
        'SELECT a.nombre_investigador, a.HIndex, a.FactorImpacto FROM investigador a, areaInstitucion b, area c, detallePublicacion d, publicacion e  WHERE a.nombre_investigador = ? and a.idAreaInstitucion = b.idAreaInstitucion and b.idArea = c.idArea and c.nombreArea = ? and a.idInvestigador = d.idInvestigador and d.idPublicacion = e.idPublicacion and e.añopublicacion between ? and ?'
        (authors, area , ano, ano2)
    )


    db.commit()
    

    return render_template('blog/index.html', posts=posts)


@bp.route('/autor', methods=('GET'))
def index():

   area = request.form['area']
    ano2 = request.form['endDate']
    posts = db.execute(
        'SELECT nombre FROM investigador WHERE añopublicacion between ? and ?'
        (ano, ano2)
    )
    db.commit()
    return render_template('blog/index.html', posts=posts)


@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None 

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO post (title, body, author_id)'
                ' VALUES (?, ?, ?)',
                (title, body, g.user['id'])
            )
            db.commit()
            return redirect(url_for('blog.index'))

    return render_template('blog/create.html')


def get_post(id, check_author=True):
	post = get_db().execute(
	    'SELECT p.id, title, body, created, author_id, username'
	    ' FROM post p JOIN user u ON p.author_id = u.id'
	    ' WHERE p.id = ?',
	    (id,)
	).fetchone()

	if post is None:
	    abort(404, "Post id {0} doesn't exist.".format(id))

	if check_author and post['author_id'] != g.user['id']:
	    abort(403)

	return post


@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'UPDATE post SET title = ?, body = ?'
                ' WHERE id = ?',
                (title, body, id)
            )
            db.commit()
            return redirect(url_for('blog.index'))

    return render_template('blog/update.html', post=post)


@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    get_post(id)
    db = get_db()
    db.execute('DELETE FROM post WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('blog.index'))