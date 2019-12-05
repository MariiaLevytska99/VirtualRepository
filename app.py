from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from config import Config


app = Flask(__name__)
app.config.from_object(Config())
CORS(app)
api =Api(app)

from db import db
db.init_app(app)
from resources.accounts import AccountsResource
from resources.requirement_types import RequirementTypeResource
from resources.requirements import RequirementResource
from resources.specifications import SpecificationResource
from resources.specification_requirements import SpecificationRequirementResource
from resources.sessions import SessionResource
from resources.accounts_sessions import AccounSessionsResource
from resources.session_tasks import SessionTaskResource
from resources.specifications import SpecificationDeleteById
from resources.specifications import SpecificationUpdateById
from resources.specification_requirements import SpecificationAddRequirementResource
from resources.specification_requirements import SpecificationDeleteRequirementResource
from resources.specification_requirements import SpecificationUpdateRequirementResource
from resources.account_specifications import AccountSpecificationResource
from resources.tasks import TaskResource

api.add_resource(AccountsResource, '/api/accounts')
api.add_resource(RequirementTypeResource, '/api/requirement/type')
api.add_resource(RequirementResource, '/api/requirements')
api.add_resource(SpecificationResource, '/api/specifications')
api.add_resource(AccountSpecificationResource, '/api/account/<id>/specification')
api.add_resource(SpecificationRequirementResource, '/api/specification/<id>/requirements')
api.add_resource(SessionResource, '/api/sessions')
api.add_resource(TaskResource, '/api/session/<id>/task')
api.add_resource(AccounSessionsResource, '/api/account_session')
api.add_resource(SessionTaskResource, '/api/session_tasks')
api.add_resource(SpecificationDeleteById, '/api/specification/<id>')
api.add_resource(SpecificationUpdateById, '/api/specification/update/<id>')
api.add_resource(SpecificationAddRequirementResource, '/api/specification/<id>/requirement')
api.add_resource(SpecificationDeleteRequirementResource, '/api/specification/<specificationId>/requirement/<id>')
api.add_resource(SpecificationUpdateRequirementResource, '/api/specification/<specificationId>/requirement/<id>')

# somehow make it secure using /current and id from token
if __name__ == '__main__':
    app.run(debug=True, port=5000);


@app.route('/')
@app.route('/api/accounts', methods=['GET', 'PUT', 'POST'])
