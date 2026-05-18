// Copyright (c) 2026, Mahmoud Tawfeek and contributors
// For license information, please see license.txt

frappe.ui.form.on("Book", {
    // عند تحميل النموذج، ضبط ظهور حقل الغلاف وإضافة زر "Mark Out of Stock" إذا كان الكتاب متوفرًا
    refresh(frm) {
        console.log('Book form loaded for :', frm.doc.title || '(new)');
        
        // 1. ضبط ظهور حقل الغلاف
        toggle_cover_image_display(frm);
        
        // 2. استدعاء دالة إضافة الزر المخصص
        add_out_of_stock_button(frm);
    },
    // عند تغيير حالة التوفر، تحديث ظهور حقل الغلاف
    in_stock(frm) {
        toggle_cover_image_display(frm);
        frm.refresh_fields();
    },

    
});

frappe.ui.form.on("Book Author Link", {
    // عند اختيار مؤلف في جدول الروابط، جلب البلد وتحديث الحقل
    author(frm, cdt, cdn) {
        const row = locals[cdt][cdn];
        if (!row.author) return;
        // جلب البلد من سجل المؤلف وتحديث الحقل في النموذج
        frappe.db.get_value('Author', row.author, 'country').then(r => {
            if (r.message && r.message.country) {
                frm.set_value('primary_author_country', r.message.country);
            }
        });
    }
});
// دالة لتبديل ظهور حقل الغلاف بناءً على حالة التوفر
function toggle_cover_image_display(frm) {
    let is_available = (frm.doc.in_stock === "Available"); 
    frm.toggle_display("cover_image", is_available);
}
// دالة لإضافة زر "Mark Out of Stock" في حالة كان الكتاب متوفرًا
function add_out_of_stock_button(frm) {
    if (frm.is_new()) return; 
    if (frm.doc.in_stock === "Unavailable") return; 
    // إضافة الزر المخصص
    frm.add_custom_button(__('Mark Out of Stock'), () => {
        // استدعاء الدالة في الباك إند لتعيين الكتاب غير متوفر
        frappe.call({
            method: 'library_tracker.library_tracker.doctype.book.book.mark_out_of_stock',
            args: {
                book_name: frm.doc.name
            },
            // بعد استدعاء الدالة، تحديث النموذج وإظهار رسالة تأكيد
            callback(r) {
                if (r.message) {
                    frappe.msgprint(r.message);
                    frm.reload_doc();
                }
            }
        });
    });
}