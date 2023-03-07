const [day, month, year] = '01-02-2003'.split("-").map(Number);
const lastDayOfMonth = new Date(year, month, 0).getDate();
console.log(lastDayOfMonth)

if (frm.doc.employee_leaving != undefined) {

      frappe.call({

        method: "library_management.library_management_system.doctype.employee_attrition_details.employee_attrition_details.update_attritionNumber_field",

        args: {
          "employee_leaving": frm.doc.employee_leaving,
          "correction": frm.doc.correction
        },

        callback: function (response) {
          // Update field with new value
          frm.set_value("attrition_number", response.message);
        }

      });
}