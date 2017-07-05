from ml.vectorizer import fv_davison


# each setting can use a different FeatureVectorizer to create different features. this way we can create a batch of experiments to run
def create_settings():
    sys_out='/home/zqz/Work/chase/output' #where the system will save its required files, such as the trained models
    data_in='/home/zqz/Work/hate-speech-and-offensive-language/data/labeled_data.csv'
    #data_in='/home/zqz/Work/hate-speech-and-offensive-language/data/labeled_data_small.csv'

    settings=[]
    settings.append(['td_original', #just a name to identify this experimental setting
                     'td_original',
                     data_in,
                     fv_davison.FeatureVectorizerDavidson(),
                     True,
                     sys_out])
    settings.append(['td_original_noFS', #just a name to identify this experimental setting
                      'td_original_noFS',
                      data_in,
                      fv_davison.FeatureVectorizerDavidson(),
                      False,
                      sys_out])
    return settings