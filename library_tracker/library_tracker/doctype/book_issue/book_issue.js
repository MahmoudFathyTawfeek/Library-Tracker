// Copyright (c) 2026, Mahmoud Tawfeek and contributors
// For license information, please see license.txt

 frappe.ui.form.on("Book Issue", {
 	onload: function(frm) {

        frm.set_query('book',
              function(){
                return {
                    filters:{
                        'in_stock':'Available'
                    }
                }
              })
 	},

    return_date: function(frm){
        if (frm.doc.return_date < frm.doc.posting_date) {
            frappe.msgprint(_("تاريخ الإرجاع لا يمكن ان يكون قبل تاريخ الاستعارة"))
        }
    }
 });
