# Copyright (c) 2026, Mahmoud Tawfeek and contributors
# For license information, please see license.txt

import frappe
from frappe.utils import date_diff, nowdate

def execute(filters=None):
    columns = [
        {
            "label": "Member",
            "fieldname": "member",
            "fieldtype": "Link",
            "options": "Library Member",
            "width": 150
        },
        {
            "label": "Book",
            "fieldname": "book",
            "fieldtype": "Link",
            "options": "Book",
            "width": 150
        },
        {
            "label": "Posting Date",
            "fieldname": "posting_date",
            "fieldtype": "Date",
            "width": 120
        },
        {
            "label": "Return Date",
            "fieldname": "return_date",
            "fieldtype": "Date",
            "width": 120
        },
        {
            "label": "Delayed Days",
            "fieldname": "delayed_days",
            "fieldtype": "Int",
            "width": 120
        },
        {
            "label": "Penalty (Egp)",
            "fieldname": "penalty",
            "fieldtype": "Currency",
            "width": 120
        }
    ]
    
    data = []

    overdue_issues = frappe.db.get_all(
        "Book Issue",
        filters={
            "return_date": ["<", nowdate()]
        },
        fields=["library_member", "library_member.full_name as member_name", "book", "posting_date", "return_date"]
    )
    
    for issue in overdue_issues:
        days = date_diff(nowdate(), issue.return_date)
        penalty_amount = days * 5
        data.append({
            "member": issue[ "member_name" ],
            "book": issue[ "book" ],
            "posting_date": issue[ "posting_date" ],
            "return_date": issue[ "return_date" ],
            "delayed_days": days,
            "penalty": penalty_amount})

    return columns, data