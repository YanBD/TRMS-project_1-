from controllers import employee_controller, ev_type_controller, info_request_controller, reimburse_status_controller, \
    reimbursement_controller, stage_controller, status_controller, userbase_controller


def route(app):
    employee_controller.route(app)
    ev_type_controller.route(app)
    info_request_controller.route(app)
    reimburse_status_controller.route(app)
    reimbursement_controller.route(app)
    stage_controller.route(app)
    status_controller.route(app)
    userbase_controller.route(app)
