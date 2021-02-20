from flask_restful import Resource, abort
from sqlalchemy.exc import IntegrityError, OperationalError

from rubix_http.exceptions.exception import NotFoundException, BadDataException


class RubixResource(Resource):
    def dispatch_request(self, *args, **kwargs):
        try:
            return super().dispatch_request(*args, **kwargs)
        except IntegrityError or OperationalError as e:
            abort(400, message=str(e.orig))
        except ValueError or BadDataException as e:
            abort(400, message=str(e))
        except NotFoundException as e:
            abort(404, message=str(e))
        except Exception as e:
            abort(500, message=str(e))
