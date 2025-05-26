class SolarCalculator:
    def __init__(self):
        # Updated panel specs and costs for Indian market (2024)
        self.panel_specs = {
            'standard': {'efficiency': 0.18, 'cost_per_m2': 5000},  # ₹/m2
            'premium': {'efficiency': 0.22, 'cost_per_m2': 7000}
        }
        # Example state-wise subsidy (can be expanded)
        self.state_subsidies = {
            'Delhi': 20000,  # ₹/kW
            'Maharashtra': 22000,
            'Karnataka': 18000,
            'Default': 18000
        }
        self.central_subsidy_per_kw = 18000  # PM Surya Ghar (2024)

    def calculate(self, rooftop_data, location_data, panel_type='standard'):
        spec = self.panel_specs[panel_type]
        daily_irradiance = 5.0  # kWh/m2/day (avg for India)
        state = location_data.get('state', 'Default')
        area = rooftop_data['usable_area']
        system_kw = round(area * spec['efficiency'] * daily_irradiance / 4.5, 2)  # 4.5 is avg panel output
        system_kw = min(max(system_kw, 1), 10)  # 1-10kW recommended
        system_cost = system_kw * spec['cost_per_m2'] * 1.1  # 10% for BOS
        central_subsidy = min(system_kw, 3) * self.central_subsidy_per_kw + max(system_kw-3, 0) * 9000
        state_subsidy = self.state_subsidies.get(state, self.state_subsidies['Default']) * system_kw
        total_subsidy = central_subsidy + state_subsidy
        net_cost = system_cost - total_subsidy
        annual_energy = system_kw * 365 * 4.5 * 0.45  # 45% CUF
        payback_years = net_cost / (annual_energy * location_data['energy_rate'])
        return {
            'system_kw': system_kw,
            'annual_energy': round(annual_energy, 2),
            'system_cost': round(system_cost, 0),
            'central_subsidy': round(central_subsidy, 0),
            'state_subsidy': round(state_subsidy, 0),
            'total_subsidy': round(total_subsidy, 0),
            'net_cost': round(net_cost, 0),
            'payback_years': round(payback_years, 1)
        }