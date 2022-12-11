from db_models import db, Accounts, BreachedSites
import requests
import config
import logging

def get_breached_account_details(account):
    account_ob = Accounts.query.filter_by(account_id=account).first()

    if account_ob is None:
        hibp_res = requests.get(f"{config.hibp_breached_url}/{account}", headers={"Hibp-Api-Key": config.hibp_api_key})

        if hibp_res.status_code != 200:
            logging.debug(f"Haveibeenpwned returned with status code {hibp_res.status_code} with message: {hibp_res.content}")
            return None
        
        pwned_sites = [x["Name"] for x in hibp_res.json()]
    
        db.session.add(Accounts(account_id=account, breached=len(pwned_sites)>0))
        [db.session.add(BreachedSites(account_id=account, site=site)) for site in pwned_sites]
        db.session.commit()
        return pwned_sites
    
    breached_sites = BreachedSites.query.filter_by(account_id=account).all()
    return [breached_site.site for breached_site in breached_sites]