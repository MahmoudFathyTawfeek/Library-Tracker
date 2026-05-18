# Copyright (c) 2026, Mahmoud Tawfeek and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Book(Document):
	def validate(self):
		if self.title and len(self.title) > 200:
			frappe.throw("Title must be at least 3 characters long.")
			# تأكد من أن العنوان لا يتجاوز 200 حرف
		if self.puplication_year and int(self.puplication_year) > 2027:
			frappe.throw("Publication year cannot be more than 1 year in the future.")
			# تأكد من أن سنة النشر ليست في المستقبل


@frappe.whitelist()
def mark_out_of_stock(book_name):
    """دالة مسموح باستدعائها من المتصفح لتعيين الكتاب غير متوفر"""
    book = frappe.get_doc("Book", book_name)
    
    # تأكد من مطابقة الكلمة لحالة الـ Select عندك (Unavailable)
    if book.in_stock == "Unavailable":
        frappe.throw("Book is already out of stock.")
        
    book.in_stock = "Unavailable"
    book.save()
    
    # إضافة تعليق تلقائي في التايم لاين بتاع الكتاب
    book.add_comment("Comment", text="This book was marked as Out of Stock via custom action.")
    # إعادة تحميل الصفحة لتحديث الواجهة
    return f"Marked {book.title} as out of stock."