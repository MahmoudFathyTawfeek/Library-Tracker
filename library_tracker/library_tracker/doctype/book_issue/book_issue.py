# Copyright (c) 2026, Mahmoud Tawfeek and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe import _


class BookIssue(Document):
	def validate(self):
		if self.return_date and self.posting_date:
			if self.return_date < self.posting_date:
				frappe.throw(_("Return Date cannot be before Posting Date."))

		if not frappe.db.exists("Library Membership",{
			"library_member": self.library_member, "docstatus": 1,
			"to_date": (">=", self.posting_date)}):
			frappe.throw(_("هذا العضو ليس لديه اشتراك سارى"))

	def on_submit(self):
		frappe.db.set_value("Book", self.book, "in_stock", "Unavailable")

	def on_cancel(self):
		frappe.db.set_value("Book", self.book, "in_stock", "Available")