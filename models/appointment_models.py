from odoo import fields, models, api, _


class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Hospital Appointment"
    _rec_name = 'appt_name'

    appt_name = fields.Char(string='Order Reference', required=True, copy=False, readonly=True,
                            default=lambda self: _('New'))
    patient_id = fields.Many2one('hospital.patient', string="Patient", required=True)
    appt_state = fields.Selection(selection=[
        ('draft', 'Draft'),
        ('confirm', 'Confirm'),
        ('done', 'Done'),
        ('cancel', 'Cancelled'),
    ], string='Status', readonly=True, tracking=True,
        default='draft')
    appt_note = fields.Text(string="Description")
    appt_date = fields.Date(string="Date")
    appt_date_checkup = fields.Datetime(string="Check Up Time")

    appt_age = fields.Integer(string="Age", tracking=True, related='patient_id.patient_age')
    appt_gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
    ], required=True, default='male', tracking=True, string="Patient Gender")

    def act_confirm(self):
        self.patient_state = 'confirm'
        print("BUTTON CONFIRM IS CLICKED !!!")

    def act_done(self):
        self.patient_state = 'done'
        print("BUTTON MARK AS DONE IS CLICKED !!!")

    def act_draft(self):
        self.patient_state = 'draft'
        print("BACK TO DRAFT ?!?!?!")

    def act_cancel(self):
        self.patient_state = 'cancel'
        print("BUTTON CANCEL IS CLICKED !!!")

    @api.model
    def create(self, vals):
        if not vals.get('appt_note'):
            vals['appt_note'] = "New Appointment"
        if vals.get('appt_name', _('New')) == _('New'):
            vals['appt_name'] = self.env['ir.sequence'].next_by_code('hospital.appointment') or _('New')
        res = super(HospitalAppointment, self).create(vals)
        print("RES ===================== >", res)
        print("VALS ===================== >", vals)
        return res

    @api.onchange('patient_id')
    def onchange_patient_id(self):
        if self.patient_id:
            if self.patient_id.patient_gender:
                self.appt_gender = self.patient_id.patient_gender
            if self.patient_id.patient_gender:
                self.appt_note = self.patient_id.patient_note
        else:
            self.appt_gender = ''
            self.appt_note = ''
