app_name = "cruzine_customizations"
app_title = "Cruzine Customizations"
app_publisher = "Jigar Tarpara"
app_description = "Cruzine Customizations"
app_email = "jigartarpara@khatavahi.in"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/cruzine_customizations/css/cruzine_customizations.css"
# app_include_js = "/assets/cruzine_customizations/js/cruzine_customizations.js"

# include js, css files in header of web template
# web_include_css = "/assets/cruzine_customizations/css/cruzine_customizations.css"
# web_include_js = "/assets/cruzine_customizations/js/cruzine_customizations.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "cruzine_customizations/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {
    "Pick List" : "public/js/pick_list.js",
    "Sales Order" : "public/js/sales_order.js",
    "Delivery Note" : "public/js/delivery_note.js"
}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "cruzine_customizations.utils.jinja_methods",
# 	"filters": "cruzine_customizations.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "cruzine_customizations.install.before_install"
# after_install = "cruzine_customizations.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "cruzine_customizations.uninstall.before_uninstall"
# after_uninstall = "cruzine_customizations.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "cruzine_customizations.utils.before_app_install"
# after_app_install = "cruzine_customizations.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "cruzine_customizations.utils.before_app_uninstall"
# after_app_uninstall = "cruzine_customizations.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "cruzine_customizations.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Delivery Note": {
		"on_submit": "cruzine_customizations.delivery_note.on_submit",
		"before_insert": "cruzine_customizations.delivery_note.before_insert",
	},
    "Address": {
        "before_insert": "cruzine_customizations.address.before_insert"
    },
    "Customer": {
        "validate": "cruzine_customizations.customer.validate"
    },
    "Sales Order": {
        "validate": "cruzine_customizations.sales_order.validate"
    },
    "Shipment": {
        "on_submit": "cruzine_customizations.shipment.on_submit"
    }
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"cruzine_customizations.tasks.all"
# 	],
# 	"daily": [
# 		"cruzine_customizations.tasks.daily"
# 	],
# 	"hourly": [
# 		"cruzine_customizations.tasks.hourly"
# 	],
# 	"weekly": [
# 		"cruzine_customizations.tasks.weekly"
# 	],
# 	"monthly": [
# 		"cruzine_customizations.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "cruzine_customizations.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "cruzine_customizations.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "cruzine_customizations.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["cruzine_customizations.utils.before_request"]
# after_request = ["cruzine_customizations.utils.after_request"]

# Job Events
# ----------
# before_job = ["cruzine_customizations.utils.before_job"]
# after_job = ["cruzine_customizations.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"cruzine_customizations.auth.validate"
# ]