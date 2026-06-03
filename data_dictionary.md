# Data Dictionary

## fact_nav
- amfi_code : INTEGER : Unique fund identifier
- date : DATE : NAV date
- nav : FLOAT : Net Asset Value

## fact_transactions
- investor_id : TEXT : Unique investor id
- transaction_date : DATE : Transaction date
- amfi_code : INTEGER : Fund code
- transaction_type : TEXT : SIP/Lumpsum/Redemption
- amount_inr : FLOAT : Transaction amount
- state : TEXT : Investor state
- city : TEXT : Investor city
- kyc_status : TEXT : KYC verification status

## fact_performance
- amfi_code : INTEGER : Fund code
- scheme_name : TEXT : Mutual fund scheme
- return_1yr_pct : FLOAT : 1 year return %
- return_3yr_pct : FLOAT : 3 year return %
- return_5yr_pct : FLOAT : 5 year return %
- expense_ratio_pct : FLOAT : Expense ratio %
- aum_crore : FLOAT : Assets under management