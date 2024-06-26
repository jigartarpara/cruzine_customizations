import frappe
from frappe.utils import cint, flt

@frappe.whitelist()
def get_query_method(doctype, txt, searchfield, start, page_len, filters):
	data = ('Sales Order', '', 'name', 0, '25', {'docstatus': 1, 'per_delivered': ['<', 100], 'status': ['!=', ''], 'customer': 'Jigar Tarpara', 'company': 'Cruzine Healthcare'})
	conditions = ""
	if txt:
		conditions += "and so.name like '%%" + txt + "%%' "
	
	if filters.get("customer"):
		conditions += " and so.customer = '{0}' ".format(filters.get("customer"))

	if filters.get("transaction_date"):
		date = filters.get("transaction_date")[1]
		conditions += f"and so.transaction_date between '{date[0]}' and '{date[1]}' "

	sales_order = frappe.db.sql(
		"""select distinct so.name, so.company,so.customer
		from `tabSales Order` so, `tabSales Order Item` so_item, `tabCustomer` customer
		where so.name = so_item.parent and so.customer = customer.name
			and customer.custom_verification in ('Verified','On Approval')
			and so.custom_verification in ('Verified','On Approval')
			and so.per_delivered < 100
			and so.docstatus = 1
			and so.status != ''
			and so.company = %s
			{}
		order by so.name ASC
		""".format(
			conditions,
		),
		(filters.get("company")),
		as_dict=1,
	)
	final_so = []
	for so in sales_order:
		is_valid = True
		payment_schedule = frappe.get_all("Payment Schedule",{"parent": so.name }, ["payment_term"])
		for row in payment_schedule:
			term_type = frappe.db.get_value("Payment Term", row.payment_term, "term_type")
			if term_type == "Before Dispatch":
				percentage = frappe.db.get_value("Payment Term", row.payment_term, "invoice_portion")
				rounded_total = frappe.db.get_value("Sales Order", so.name, "rounded_total")
				advance_paid = frappe.db.get_value("Sales Order", so.name, "advance_paid")
				minimum_criteria = flt(rounded_total) * flt(percentage) / 100
				if minimum_criteria > flt(advance_paid):
					is_valid = False
		if is_valid:
			final_so.append(so)
		

	return final_so