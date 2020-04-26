import json
import shlex
import subprocess
from datetime import datetime

import preferences
from Job import Job

RESULTS_PER_PAGE = '200'
# The word that you would have typed in the search bar on WTTJ
KEYWORD = 'Spring'
LAST_VISIT_DATE = datetime(year=2020, month=4, day=26)

cmd = '''
curl 'https://csekhvms53-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia%20for%20vanilla%20JavaScript%20(lite)%203.24.12%3Breact-instantsearch%205.3.2%3BJS%20Helper%20(2.28.0)&x-algolia-application-id=CSEKHVMS53&x-algolia-api-key=02f0d440abc99cae37e126886438b266'
-H 'Connection: keep-alive'
-H 'accept: application/json'
-H 'Sec-Fetch-Dest: empty'
-H 'content-type: application/x-www-form-urlencoded'
-H 'Origin: https://www.welcometothejungle.com'
-H 'Sec-Fetch-Site: cross-site'
-H 'Sec-Fetch-Mode: cors'
-H 'Referer: https://www.welcometothejungle.com/fr/jobs?page=1&query=''' + KEYWORD + '''&aroundQuery=Paris%2C%20France&aroundLatLng=48.85718%2C2.34141&aroundRadius=20000'
-H 'Accept-Language: fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7'
--data '{"requests":[{"indexName":"wk_cms_jobs_production",\
"params":"query=''' + KEYWORD + '''&hitsPerPage=''' + RESULTS_PER_PAGE + '''\
&maxValuesPerFacet=20\
&page=0\
&restrictSearchableAttributes=%5B%22name%22%2C%22profession.category%22%2C%22profession.name%22%2C%22profile%22%2C%22description%22%2C%22organization.name%22%2C%22office.city%22%2C%22office.district%22%2C%22office.state%22%2C%22office.country%22%2C%22department%22%2C%22contract_type_names.fr%22%2C%22sectors.name.fr%22%2C%22sectors.parent.fr%22%5D\
&highlightPreTag=%3Cais-highlight-0000000000%3E\
&highlightPostTag=%3C%2Fais-highlight-0000000000%3E\
&aroundLatLng=48.85718%2C2.34141\
&aroundRadius=5000\
&aroundPrecision=5000\
&filters=website.reference%3Awttj_fr\
&facets=%5B%22office.country_code%22%2C%22office.state%22%2C%22office.district%22%2C%22office.location%22%2C%22contract_type_names.fr%22%2C%22experience_level_minimum%22%2C%22remote%22%2C%22organization.size.fr%22%2C%22language%22%2C%22sectors_name.fr.Architecture%22%2C%22sectors_name.fr.Association%20%2F%20ONG%22%2C%22sectors_name.fr.Banques%20%2F%20Assurances%20%2F%20Finance%22%2C%22sectors_name.fr.Conseil%20%2F%20Audit%22%2C%22sectors_name.fr.Culture%20%2F%20M%C3%A9dia%20%2F%20Divertissement%22%2C%22sectors_name.fr.Distribution%22%2C%22sectors_name.fr.Education%20%2F%20Formation%20%2F%20Recrutement%22%2C%22sectors_name.fr.Food%20et%20boisson%22%2C%22sectors_name.fr.H%C3%B4tellerie%20%2F%20Tourisme%20%2F%20Loisirs%22%2C%22sectors_name.fr.Immobilier%22%2C%22sectors_name.fr.Industrie%22%2C%22sectors_name.fr.L%C3%A9gal%20%2F%20Justice%22%2C%22sectors_name.fr.Mobilit%C3%A9%20%2F%20Transport%22%2C%22sectors_name.fr.Mode%20%2F%20Luxe%20%2F%20Beaut%C3%A9%20%2F%20Art%20de%20vivre%22%2C%22sectors_name.fr.Publicit%C3%A9%20%2F%20Marketing%20%2F%20Agence%22%2C%22sectors_name.fr.Sant%C3%A9%20%2F%20Social%20%2F%20Environnement%22%2C%22sectors_name.fr.Secteur%20public%20et%20administration%22%2C%22sectors_name.fr.Services%20aux%20entreprises%22%2C%22sectors_name.fr.Tech%22%2C%22profession_name.fr.Audit%20%2F%20Finance%20%2F%20Assurance%22%2C%22profession_name.fr.Business%22%2C%22profession_name.fr.Conseil%22%2C%22profession_name.fr.Cr%C3%A9a%22%2C%22profession_name.fr.H%C3%B4tellerie%20%2F%20Restauration%22%2C%22profession_name.fr.Immobilier%22%2C%22profession_name.fr.Industrie%22%2C%22profession_name.fr.Marketing%20%2F%20Communication%22%2C%22profession_name.fr.Media%22%2C%22profession_name.fr.M%C3%A9tiers%20de%20la%20mode%22%2C%22profession_name.fr.Relation%20client%22%2C%22profession_name.fr.Retail%22%2C%22profession_name.fr.Sant%C3%A9%20%2F%20M%C3%A9dical%20%2F%20Social%22%2C%22profession_name.fr.Support%22%2C%22profession_name.fr.Tech%22%2C%22profession_name.fr.Tourisme%22%5D\
&tagFilters=\
&numericFilters=%5B%22experience_level_minimum%3E%3D0%22%2C%22experience_level_minimum%3C%3D15%22%5D"},{"indexName":"wk_cms_jobs_production","params":"query=''' + KEYWORD + '''\
&hitsPerPage=1\
&maxValuesPerFacet=20\
&page=0\
&restrictSearchableAttributes=%5B%22name%22%2C%22profession.category%22%2C%22profession.name%22%2C%22profile%22%2C%22description%22%2C%22organization.name%22%2C%22office.city%22%2C%22office.district%22%2C%22office.state%22%2C%22office.country%22%2C%22department%22%2C%22contract_type_names.fr%22%2C%22sectors.name.fr%22%2C%22sectors.parent.fr%22%5D\
&highlightPreTag=%3Cais-highlight-0000000000%3E\
&highlightPostTag=%3C%2Fais-highlight-0000000000%3E\
&aroundLatLng=48.85718%2C2.34141\
&aroundRadius=5000\
&aroundPrecision=5000\
&filters=website.reference%3Awttj_fr\
&attributesToRetrieve=%5B%5D\
&attributesToHighlight=%5B%5D\
&attributesToSnippet=%5B%5D\
&tagFilters=\
&analytics=false\
&clickAnalytics=false\
&facets=experience_level_minimum"}]}' --compressed
'''


def run_request():
    args = shlex.split(cmd)

    process = subprocess.Popen(args, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    return json.loads(stdout)['results'][0]


def is_eligible(entry):
    return not entry['contract_type'] in preferences.EXCLUDED_CONTRACT_TYPE


def is_blacklisted_company(entry):
    return not str.lower(entry['organization']['name']) in preferences.EXCLUDED_COMPANY


def is_within_size_range(entry):
    return not entry['organization']['size']['fr'] in preferences.EXCLUDED_COMPANY_SIZE


def is_misleading_java_title(entry):
    job_title = str.lower(entry['name'])
    if "javascript" in job_title:
        job_title = job_title.replace("javascript", "")
        accepted_technology = ['java', 'javaee', 'jee', 'j2e', 'spring']
        for technology in accepted_technology:
            if technology in job_title:
                return False
        return True

    return 'front end developer' in job_title or 'frontend developer' in job_title or 'consultant' in job_title


def is_excluded_reference(entry):
    return entry['reference'] in preferences.EXCLUDED_REFERENCE


def is_relevant(entry):
    return is_eligible(entry) and is_blacklisted_company(entry) and is_within_size_range(entry) \
           and not is_misleading_java_title(entry) and not is_excluded_reference(entry)


def has_been_seen(entry):
    published_at = entry['published_at'][0:10]
    return datetime.strptime(published_at, '%Y-%m-%d') < LAST_VISIT_DATE


def process_request():
    jobs = []
    json_response = run_request()
    print(f"{len(json_response['hits'])} entries before applying filters ...")
    for hit in json_response['hits']:
        if not is_relevant(hit) or has_been_seen(hit):
            continue
        job = Job(hit['reference'], hit['name'], hit['published_at'], hit['organization']['name'],
                  hit['organization']['size']['fr'], hit['contract_type'], hit['slug'], hit['office']['city'])
        jobs.append(job)

    print(f"{len(jobs)} entries after applying filters")
    return jobs
