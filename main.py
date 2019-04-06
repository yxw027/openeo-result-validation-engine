import json
import logging

from JobWorker.JobWorker import  JobWorker
from RuleEngine.RuleEngine import RuleEngine
from ValidationEngine.ValidationEngine import ValidationEngine

if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)
    with open('min-time.json', 'r') as referenceJob:
        with open('backendProvider.json', 'r') as backendProvidersFile:
            job = json.loads(referenceJob.read())
            backendProviders = json.loads(backendProvidersFile.read())

            jobWorker = JobWorker(backendProviders, referenceJob)
            jobWorker.start_fetching()
            results = jobWorker.get_results()

            ruleEngine = RuleEngine(job)
            ruleEngine.parse_rules()

            validationEngine = ValidationEngine(ruleEngine, results, backendProviders)
            validationEngine.validate()






