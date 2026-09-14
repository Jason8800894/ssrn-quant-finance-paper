# ==============================================================================
# PAPER 1: ENGINEERING RISK-REWARD ASYMMETRY VIA DELTA-NEUTRAL FRAMEWORK
# Author: Jason Chan (Form 5 Student-Athlete, Jockey Club Ti-I College)
# Version 1.0 - Initial Core Asset Allocation Scaffolding
# ==============================================================================

def calculate_asymmetric_allocation(total_capital, mmf_yield, duration_years):
    """
    Core math engine designed by Jason Chan.
    Strictly caps the downside risk while safeguarding the initial capital injection
    by calculating the optimal allocation between protective MMF and convex LEAPs.
    """
    # 1. Calculate the Future Value factor of the risk-free cash buffer
    future_value_factor = (1 + mmf_yield) ** duration_years
    
    # 2. Derive the minimum cash ratio required to guarantee: Total Capital >= Principal Floor
    min_mmf_ratio = 1.0 / future_value_factor
    
    # 3. Extract the remaining risk-capital ratio for long-term bond OTM Calls (Convex Upside)
    max_option_ratio = 1.0 - min_mmf_ratio
    
    # Scale allocation based on the $1,000,000 portfolio size
    mmf_cash_allocated = total_capital * min_mmf_ratio
    option_budget_allocated = total_capital * max_option_ratio
    
    return min_mmf_ratio, max_option_ratio

# ------------------------------------------------------------------------------
# SIMULATION ZONE: TARGETING MY US$1,000,000 QUANTITATIVE MODEL ENVIRONMENT
# Setting parameters based on my live macro monitor strategy
# ------------------------------------------------------------------------------
total_portfolio = 1000000
futu_mmf_rate = 0.040  # 4.0% annualized yield floor
duration_horizon = 2   # 2-Year LEAPs to flatten the non-linear Theta decay curve

min_mmf, max_opt = calculate_asymmetric_allocation(total_portfolio, futu_mmf_rate, duration_horizon)

print(">> Jason's Core Portfolio Logic V1.0 initialized successfully.")
print(f">> MMF Protective Floor Allocation: {min_mmf * 100:.2f}%")
print(f">> OTM Call Convex Budget Allocation: {max_opt * 100:.2f}%")
