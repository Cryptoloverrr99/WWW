def check_token(token):
    # Ajout de vérifications de structure
    if not isinstance(token, dict):
        return False
        
    # Protection des accès nested
    metrics = token.get('metrics') or {}
    security = token.get('security') or {}
    dex = token.get('dex') or {}

    # Conversion des pourcentages
    liquidity_locked = float(security.get('liquidityLockedPercent', 0))
    dev_holding = float(security.get('devHoldings', 0))
    top10_holding = float(security.get('top10Holdings', 0))

    # Nouveau : gestion des types
    filters = {
        'supply': float(metrics.get('circulatingSupply', 0)) <= 1e9,
        'marketcap': float(metrics.get('marketCap', 0)) >= 150000,
        'liquidity': float(metrics.get('liquidity', 0)) >= 70000,
        'liquidity_locked': liquidity_locked in [99.0, 100.0],
        'dev_holding': dev_holding <= 20.0,
        'top10_holding': top10_holding <= 35.0,
        'marketers': int(metrics.get('marketers', 0)) >= 500,
        'holders': int(metrics.get('holders', 0)) >= 200,
        'volume': float(metrics.get('volume24h', 0)) >= 200000,
        'dex_listed': dex.get('name') == 'DexScreener'
    }
    
    return all(filters.values())
