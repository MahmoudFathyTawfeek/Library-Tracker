// Copyright (c) 2026, Mahmoud Tawfeek and contributors
// For license information, please see license.txt

frappe.query_reports["Overdue Books Report"] = {
	"filters": [
		{
			"fieldname": "member",
			"label": _("Library Member"),
			"fieldtype": "Link",
			"options": "Library Member"
		}

	]
};
