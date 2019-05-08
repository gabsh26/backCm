from app.common.database import Database
import functools

from flask import (
    flash, g, redirect, render_template, request, session, url_for
)
class Logout:
    @classmethod
    def logout(cls, data):
        session.clear()
    	return redirect(url_for('index'))