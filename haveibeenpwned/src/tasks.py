from celery_config import celery_app
import config
import requests
from db_models import db, Accounts, BreachedSites
import traceback
import logging

def update_pwned_accounts(account):
    hibp_res = requests.get(f"{config.hibp_breached_url}/{account}", headers={"Hibp-Api-Key": config.hibp_api_key})

    if hibp_res.status_code != 200:
        logging.debug(f"Haveibeenpwned returned with status code {hibp_res.status_code} with message: {hibp_res.content}")
        return None
    
    pwned_sites = [x["Name"] for x in hibp_res.json()]

    existing_breaches_ob = BreachedSites.query.filter_by(BreachedSites.site.in_(pwned_sites)).all()
    existing_breaches = [ob.site for ob in existing_breaches_ob]
    new_sites = list(set(pwned_sites) - set(existing_breaches))
    [db.session.add(BreachedSites(account_id=account, site=site)) for site in new_sites]
    db.session.commit()

@celery_app.task()
def fetch_new_pwn():
    try:
        accounts_ob = Accounts.query.all()
        accounts = [ob.account_id for ob in accounts_ob]
        for account in accounts:
            update_pwned_accounts(account)
    except Exception as ex:
        traceback.print_exc()