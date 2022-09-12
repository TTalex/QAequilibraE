def run_traffic_assig(qgis_project):
    if qgis_project.no_binary:
        qgis_project.message_binary()
    else:
        from .traffic_assignment_dialog import TrafficAssignmentDialog

        if qgis_project.project is None:
            qgis_project.show_message_no_project()
        else:
            dlg2 = TrafficAssignmentDialog(qgis_project)
            dlg2.show()
            dlg2.exec_()