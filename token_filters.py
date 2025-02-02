def check_token(token):
    metrics = token.get('metrics', {})
    security = token.get('security', {})
    
    filters = {
        'supply': metrics.get('circulatingSupply', 0) <= 1e9,
        'marketcap': metrics.get('marketCap', 0) >= 150000,
        'liquidity': metrics.get('liquidity', 0) >= 70000,
        'liquidity_locked': security.get('liquidityLockedPercent', 0) in [99, 100],
        'dev_holding': security.get('devHoldings', 0) <= 20,
        'top10_holding': security.get('top10Holdings', 0) <= 35,
        'marketers': metrics.get('marketers', 0) >= 500,
        'holders': metrics.get('holders', 0) >= 200,
        'volume': metrics.get('volume24h', 0) >= 200000,
        'dex_listed': token.get('dex', {}).get('name') == 'DexScreener'
    }
    
    return all(filters.values())
