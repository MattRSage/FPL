# -*- coding: utf-8 -*-
import os
import requests
import logging
import pandas as pd

def extract_data(key, url, file_path):
    response = requests.get(url)
    json = response.json()
    df = pd.DataFrame(json[key])
    df.to_csv(file_path)
       

def main(project_dir):
    # get logger
    logger = logging.getLogger(__name__)
    logger.info('getting raw data')
    
    # key for player elements
    key = 'elements'
    
    # urls
    train_url = 'https://fantasy.premierleague.com/api/bootstrap-static/'
    
    # file paths
    raw_data_path = os.path.join(project_dir,'data','raw')
    train_data_path = os.path.join(raw_data_path,'train.csv')
    
    # extract data
    extract_data(key, train_url, train_data_path)
    logger.info('downloaded raw training data')
    
if __name__ == '__main__':
    # get root directory
    project_dir = os.path.join(os.path.dirname(__file__), os.pardir, os.pardir)
    
    # setup logger
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)
    
    main(project_dir)
    
    
