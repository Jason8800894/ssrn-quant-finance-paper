# ==============================================================================
# PAPER 1: ENGINEERING RISK-REWARD ASYMMETRY VIA DELTA-NEUTRAL FRAMEWORK
# Author: Jason Chan (Form 5 Student-Athlete, Jockey Club Ti-I College)
# Version 1.0 - Initial Core Asset Allocation Scaffolding
# ==============================================================================

import math
from scipy.stats import norm

def calculate_asymmetric_allocation(total_capital, mmf_yield_usd, mmf_yield_hkd, duration_years, spot_price, strike_price, volatility):
    """
    Core math engine designed by Jason Chan.
    Strictly caps the downside risk to absolute zero while completely unlocking 
    unlimited convexity upside via continuous compounding OBPI and BSM framework.
    """
    
    # 1. 為了隔離外匯交叉風險 (FX Cross-Currency Contamination)，對無風險利率進行雙因子加權平均
    # 平安美元貨幣基金 (+3.4010%) 與 泰康港元貨幣基金 (+2.1808%)
    r_blended = (mmf_yield_usd * 0.5) + (mmf_yield_hkd * 0.5)
    
    # 2. 核心升級：利用隨機過程與連續複利 (Continuous Compounding) 倒推「本金地板」
    # min_mmf_ratio = e^(-r * T)
    min_mmf_ratio = math.exp(-r_blended * duration_years)
    
    # 3. 精確鎖定本金防線 (Principal Floor) 所需的配置金額
    allocated_to_mmf = total_capital * min_mmf_ratio
    
    # 4. 提取剩餘 Yield 轉化為期權預算 (Option Budget)
    option_budget = total_capital - allocated_to_mmf
    
    # 5. 導入 Black-Scholes-Merton (BSM) 公式，精確計算 Out-of-the-money (OTM) Call 的真實權利金 (Premium)
    T = duration_years
    S = spot_price
    K = strike_price
    r = r_blended
    sigma = volatility
    
    d1 = (math.log(S / K) + (r + (sigma ** 2) / 2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)
    
    # 計算單張標準歐式期權的理論價格 (Premium)
    option_premium = (S * norm.cdf(d1)) - (K * math.exp(-r * T) * norm.cdf(d2))
    
    # 6. 計算在當前預算上限內，實盤能夠精確購買的期權合約手數 (Units Purchased)
    
    if option_premium > 0:
        units_purchased = option_budget / option_premium
    else:
        units_purchased = 0
        
    return {
        "Blended_Risk_Free_Rate": r_blended,
        "Minimum_MMF_Allocation_Ratio": min_mmf_ratio,
        "Capital_in_MMF_Floor": allocated_to_mmf,
        "Option_Budget_Sleeve": option_budget,
        "Single_Option_Premium": option_premium,
        "Max_Purchasable_Option_Units": units_purchased
    }

# ==========================================
# SIMULATION ZONE: TARGETING JASON'S REAL PORTFOLIO PARAMS
# ==========================================
if __name__ == "__main__":
    # 假設初始管理規模 US$1,000,000
    portfolio_size = 1000000 
    
    # 真實富途持倉持倉數據輸入
    pingan_usd_yield = 0.034010   # 平安貨幣基金七日年化
    taikang_hkd_yield = 0.021808   # 泰康貨幣基金七日年化
    time_horizon = 1.0             # 1年期鎖定
    
    # 標的物設定（例如黃金 GLD SPDR 或 標普500 指數）
    current_spot = 400.0           # 假設當前股價/ETF價格 S0
    otm_strike = 440.0             # 設行使價為 10% OTM 向上解鎖 Convexity
    market_vol = 0.16              # 隱含波動率 (IV) 設為 16%
    
    result = calculate_asymmetric_allocation(
        portfolio_size, pingan_usd_yield, taikang_hkd_yield, 
        time_horizon, current_spot, otm_strike, market_vol
    )
    
    print(f"--- JASON'S QUANT ENGINE RECONCILIATION ---")
    print(f"Required MMF Floor Allocation: ${result['Capital_in_MMF_Floor']:,.2f}")
    print(f"Available Option Budget Sleeve: ${result['Option_Budget_Sleeve']:,.2f}")
    print(f"BSM European Call Premium: ${result['Single_Option_Premium']:.4f}")
    print(f"Max Convex Option Units to Long: {result['Max_Purchasable_Option_Units']:,.2f}")
  #=====================================
    Jason's EMPIRICAL VALIDATION ZONE
  #=====================================
    print("\n--- PHASE 1:REAL-MONEY EMPIRICAL EXPOSURE ---")
    #1. Futu Platform live account position
  live_usd_mmf =205.68
  live_hkd_mmf =801.53

    
    
