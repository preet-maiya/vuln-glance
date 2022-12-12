from src.celery_config import celery_app
from src.server import app
import src.config as config
import requests
from src.db_models import db, Accounts, BreachedSites
import traceback
import logging
import time


def update_pwned_accounts(account):
    hibp_res = requests.get(f"{config.hibp_breached_url}/{account}", headers={"Hibp-Api-Key": config.hibp_api_key})

    if hibp_res.status_code != 200:
        logging.debug(f"Haveibeenpwned returned with status code {hibp_res.status_code} with message: {hibp_res.content}")
        return None
    
    pwned_sites = [x["Name"] for x in hibp_res.json()]

    existing_breaches_ob = BreachedSites.query.filter_by(account_id=account).all()
    existing_breaches = [ob.site for ob in existing_breaches_ob]
    new_sites = list(set(pwned_sites) - set(existing_breaches))
    logging.info(f"new sites to insert {new_sites}")
    [db.session.add(BreachedSites(account_id=account, site=site)) for site in new_sites]
    db.session.commit()

@celery_app.task()
def fetch_new_pwn():
    with app.app_context():
        try:
            accounts_ob = Accounts.query.all()
            accounts = [ob.account_id for ob in accounts_ob]
            for account in accounts:
                update_pwned_accounts(account)
                time.sleep(10)
        except Exception as ex:
            traceback.print_exc()