from flask import Blueprint
import asyncio

main = Blueprint('main', __name__)

from . import views
