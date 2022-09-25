from odoo import models, fields, _, api


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Page of Patient"
    _rec_name = "patient_name"

    patient_reference = fields.Char(string='Order Reference', required=True, copy=False, readonly=True,
                            default=lambda self: _('New'))
    patient_name = fields.Char(string="Patient Name", required=True, translate=True, tracking=True)
    patient_address = fields.Text(string="Address", tracking=True)
    patient_age = fields.Integer(string="Age", tracking=True)
    patient_gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
    ], required=True, default='male', tracking=True)
    patient_note = fields.Text(string="Note", tracking=True)
    patient_state = fields.Selection(selection=[
        ('draft', 'Draft'),
        ('confirm', 'Confirm'),
        ('done', 'Done'),
        ('cancel', 'Cancelled'),
    ], string='Status', readonly=True, tracking=True,
        default='draft')
    patient_responsible_id = fields.Many2one(string="Responsible", comodel_name='res.partner', tracking=True)

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
        if not vals.get('patient_note'):
            vals["patient_note"] = 'New Patient'
        if vals.get('patient_reference', _('New')) == _('New'):
            vals['patient_reference'] = self.env['ir.sequence'].next_by_code('hospital.patient') or _('New')
        res = super(HospitalPatient, self).create(vals)
        print("RES ===================== >", res)
        print("VALS ===================== >", vals)
        return res
