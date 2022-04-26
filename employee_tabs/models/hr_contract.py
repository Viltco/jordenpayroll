from odoo import models, fields, api


class employee_tabs(models.Model):
    _inherit = "hr.contract"

    workforce_agility_consulting = fields.Float(string="40102 · Workforce Agility - Consulting")
    workforce_agility_task_based = fields.Float(string="40104 · Workforce Agility - Task Based")
    expense_reimbursement = fields.Float(string="40113 · Expense Reimbursement")
    npo_optimization_drive_Test = fields.Float(string="40114 · NPO - Optimization - Drive Test")
    ni_outdoor = fields.Float(string="40117 · NI Outdoor")
    IP_services_towards = fields.Float(string="40118 · IP Services towards 5G")
    total_income = fields.Float(string="Total Income")

    @api.onchange('workforce_agility_consulting' , 'workforce_agility_task_based','expense_reimbursement','npo_optimization_drive_Test'
                  'ni_outdoor','IP_services_towards')
    def onchange_total_income(self):
        self.total_income = self.workforce_agility_consulting + self.workforce_agility_task_based + self.expense_reimbursement + self.npo_optimization_drive_Test + self.ni_outdoor + self.IP_services_towards




    payroll_taxes = fields.Float(string="51150 · Payroll Taxes")
    Thirteenth_salary = fields.Float(string="51122 · Thirteenth salary")
    Termination_Expense = fields.Float(string="51130 · Termination Expense")
    Fringe_Bennefits_Vacations = fields.Float(string="51140 · Fringe Bennefits - Vacation")
    total_salaries = fields.Float(string="Total Salaries")

    @api.onchange('payroll_taxes', 'Thirteenth_salary', 'Termination_Expense',
                  'Fringe_Bennefits_Vacations')
    def onchange_total_salaries(self):
        self.total_salaries = self.payroll_taxes + self.Thirteenth_salary + self.Termination_Expense + self.Fringe_Bennefits_Vacations

    Air_transport_related = fields.Float(string="51310 · Air transport and related")
    Urban_Transport = fields.Float(string="51321 · Urban Transport")
    Car_rental = fields.Float(string="51322 · Car rental")
    Gasoline = fields.Float(string="51323 · Gasoline")
    Tolls = fields.Float(string="51324 · Tolls")
    Car_Maint_Repair = fields.Float(string="51329 · Car Maint and Repair")
    Office_rent = fields.Float(string="51331 · Office rent")
    Consultant_Housing_Hotel = fields.Float(string="51340 · Consultant Housing (Hotel)")
    Fixed_VOIP_Cell_Phone = fields.Float(string="51351 · Fixed -VOIP-Cell Phone")
    Internet_Service = fields.Float(string="51352 · Internet Service")
    Mail_Courier = fields.Float(string="51353 · Mail & Courier")
    Meals = fields.Float(string="51360 · Meals")
    Prof_Development_Training = fields.Float(string="51370 · Prof Development-Training")
    Safety_Hygiene = fields.Float(string="51380 · Safety and Hygiene")
    total_logistics = fields.Float(string="Total Logistics" )

    @api.onchange('Air_transport_related', 'Urban_Transport', 'Car_rental',
                  'Gasoline'
                  'Tolls', 'Car_Maint_Repair' ,'Office_rent' , 'Consultant_Housing_Hotel','Fixed_VOIP_Cell_Phone',
                  'Internet_Service','Mail_Courier','Meals','Prof_Development_Training','Safety_Hygiene')
    def onchange_total_logistics(self):
        self.total_logistics = self.Air_transport_related + self.Urban_Transport + self.Car_rental + self.Gasoline + self.Tolls + self.Car_Maint_Repair + self.Office_rent
        + self.Consultant_Housing_Hotel  + self.Fixed_VOIP_Cell_Phone  + self.Internet_Service  + self.Mail_Courier  + self.Meals  + self.Prof_Development_Training + self.Safety_Hygiene

    computers = fields.Float(string="51420 · Computers (laptops, netbooks)")
    specialized_equipment = fields.Float(string="51470 · Specialized Equipment")
    specialized_materials = fields.Float(string="51480 · Specialized Materials")
    consultant_health_insurance = fields.Float(string="51530 · Consultant Health Insurance")
    total_materials = fields.Float(string="Total Materiales/Equipos/ HI")

    @api.onchange('computers', 'specialized_equipment', 'specialized_materials',
                  'consultant_health_insurance')
    def onchange_total_materials(self):
        self.total_materials = self.computers + self.specialized_equipment + self.specialized_materials + self.consultant_health_insurance

    visa_processing_fees = fields.Float(string="Visa Processing Fees")
    independent_sub = fields.Float(string="Independent Sub")
    withholding_tax = fields.Float(string="Withholding Tax")
    bank_fees = fields.Float(string="Bank Fees")
    total_others = fields.Float(string="Total")

    @api.onchange('visa_processing_fees', 'independent_sub', 'withholding_tax',
                  'bank_fees')
    def onchange_total_salaries(self):
        self.total_others = self.visa_processing_fees + self.independent_sub + self.withholding_tax + self.bank_fees

