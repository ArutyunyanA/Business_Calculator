


class BusinessCalculator:

	def __init__(self, gross_profit, rent, salary, supply, consumable, communal_cost):
		self.gross_profit = gross_profit
		self.rent = rent
		self.salary = salary
		self.supply = supply
		self.consumable = consumable
		self.communal_cost = communal_cost
	
	def operating_profit(self):
		self.op_profit = [self.rent, self.salary, self.supply, self.consumable, self.communal_cost]
		self.o_profit = 0
		for x in self.op_profit:
			self.o_profit += x
			self.oper_profit = self.gross_profit - self.o_profit
		return f'This is an operating profit amount::> {self.oper_profit} €'

	def income_tax(self):
		self.in_tax = self.oper_profit * 0.80
		self.tax = self.oper_profit - self.in_tax
		return f'This is income tax 20% amount::> {self.tax} €'

	def outgoing_vat(self):
		self.vat = self.gross_profit * 0.91
		self.vat_ammount = round(self.gross_profit - self.vat)
		return f'This is VAT outgoing tax 9,5% amount::> {self.vat_ammount} €'
		
	def incoming_vat(self):	
		self.incom_vat = (self.supply + self.consumable + self.communal_cost)
		self.in_tax_vat = self.incom_vat * 0.78
		self.vat_tax = round(self.incom_vat - self.in_tax_vat)
		return f'This is incoming VAT 22% ammount::> {self.vat_tax} €'

	def pay_vat(self):
		self.pay_vat = self.vat_ammount - self.vat_tax
		return f'This is a VAT amount for pay or if value is negative, then to return vat_tax {self.pay_vat} €'

	def net_profit(self):
		self.nt_profit = round(self.oper_profit - (self.pay_vat + self.tax))
		return f'This is a net profit::> {self.nt_profit} €'
	
	def corporate_tax(self):
		self.corp_tax = self.nt_profit * 0.84
		self.cp_tax = round(self.nt_profit - self.corp_tax)
		return f'This is corporate tax 16% amount::> {self.cp_tax} €'


if __name__=='__main__':

	business = BusinessCalculator(int(input('<::Pleas insert the gross_profit amount::>\n')), 
	int(input('<::Please insert monthly rent cost::>\n')),
	int(input('<::Please insert monthly bruto salaries amount::>\n')),
	int(input('<::Please insert amount for supplying main goods::>\n')),
	int(input('<::Please insert amount for supplying of consumable goods::>\n')),
	int(input('<::Please insert monthly communal_cost::>\n')))
	print(business.operating_profit())
	print(business.income_tax())
	print(business.outgoing_vat())
	print(business.incoming_vat())
	print(business.pay_vat())
	print(business.net_profit())
	print(business.corporate_tax())
	
